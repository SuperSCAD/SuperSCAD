from ScadTestCase import ScadTestCase
from super_scad.d3.Polyhedron import Polyhedron
from super_scad.scad.Scad import Scad
from super_scad.scad.Unit import Unit
from super_scad.type.Point3 import Point3


class PolyhedronTest(ScadTestCase):
    """
    Test cases for Polyhedron.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testWithLists(self):
        """
        Test where all faces are given as lists.
        """
        path_actual, path_expected = self.paths()
        scad = Scad(unit_length_final=Unit.MM)

        point1 = Point3(0.0, 0.0, 0.0)
        point2 = Point3(440.0, 0.0, 0.0)
        point3 = Point3(440.0, 440.0, 0.0)
        point4 = Point3(0.0, 440.0, 0.0)
        point5 = Point3(220.0, 220.0, 280.0)  # apex

        faces = [[point1, point2, point3, point4],  # base plane
                 [point1, point5, point2],  # front
                 [point2, point5, point3],  # right side
                 [point3, point5, point4],  # back
                 [point4, point5, point1]]  # left side

        polyhedron = Polyhedron(faces=faces)

        scad.run_super_scad(polyhedron, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testWithTuples(self):
        """
        Test where all faces are given as tuples.
        """
        path_actual, path_expected = self.paths()
        scad = Scad(unit_length_final=Unit.MM)

        point1 = Point3(0.0, 0.0, 0.0)
        point2 = Point3(440.0, 0.0, 0.0)
        point3 = Point3(440.0, 440.0, 0.0)
        point4 = Point3(0.0, 440.0, 0.0)
        point5 = Point3(220.0, 220.0, 280.0)  # apex

        faces = [(point1, point2, point3, point4),  # base plane
                 (point1, point5, point2),  # front
                 (point2, point5, point3),  # right side
                 (point3, point5, point4),  # back
                 (point4, point5, point1)]  # left side

        polyhedron = Polyhedron(faces=faces, convexity=1)

        scad.run_super_scad(polyhedron, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testDebug(self):
        """
        Test where one face is been highlighted.
        """
        path_actual, path_expected = self.paths()
        scad = Scad(unit_length_final=Unit.ROYAL_CUBIT)

        base = 440.0
        height = 280.0
        point1 = Point3(0.0, 0.0, 0.0)
        point2 = Point3(base, 0.0, 0.0)
        point3 = Point3(base, base, 0.0)
        point4 = Point3(0.0, base, 0.0)
        point5 = Point3(base / 2.0, base / 2.0, height)  # apex

        faces = [[point1, point2, point3, point4],  # base plane
                 [point1, point5, point2],  # front
                 [point2, point5, point3],  # right side
                 [point3, point5, point4],  # back
                 [point4, point5, point1]]  # left side

        polyhedron = Polyhedron(faces=faces, highlight_face=0)

        scad.run_super_scad(polyhedron, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testFusedPoints(self):
        """
        Test where some points are fused.
        """
        path_actual, path_expected = self.paths()
        scad = Scad(unit_length_final=Unit.MM)

        size = 2.0
        height = 2.0

        def p0(h: float) -> Point3:
            return Point3(0.5 * size * h / height, 0.5 * size * h / height, h)

        def p1(h: float) -> Point3:
            return Point3(size - 0.5 * size * h / height, 0.5 * size * h / height, h)

        def p2(h: float) -> Point3:
            return Point3(size - 0.5 * size * h / height, size - 0.5 * size * h / height, h)

        def p3(h: float) -> Point3:
            return Point3(0.5 * size * h / height, size - 0.5 * size * h / height, h)

        faces = []
        current_height = 0.0
        level0 = (p0(current_height), p1(current_height), p2(current_height), p3(current_height))
        faces.append(level0)
        for i in range(0, 16):
            current_height += (height - current_height) / 2.0
            level1 = (p0(current_height), p1(current_height), p2(current_height), p3(current_height))

            faces.append((level0[0], level1[0], level1[1], level0[1]))  # front
            faces.append((level0[1], level1[1], level1[2], level0[2]))  # right
            faces.append((level0[2], level1[2], level1[3], level0[3]))  # back
            faces.append((level0[3], level1[3], level1[0], level0[0]))  # left

            level0 = level1

        # Apex
        apex = Point3(0.5 * size, 0.5 * size, height)
        faces.append((level0[0], apex, level0[1]))  # front
        faces.append((level0[1], apex, level0[2]))  # right
        faces.append((level0[2], apex, level0[3]))  # back
        faces.append((level0[3], apex, level0[0]))  # left

        polyhedron = Polyhedron(faces=faces, highlight_face=len(faces) - 4)

        scad.run_super_scad(polyhedron, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
