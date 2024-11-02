from d3.Polyhedron.ImperialUnitCube import ImperialUnitCube
from ScadTestCase import ScadTestCase
from super_scad.d3.Polyhedron import Polyhedron
from super_scad.scad.Unit import Unit
from super_scad.type.Vector3 import Vector3


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
        scad = self.create_scad()

        point1 = Vector3(0.0, 0.0, 0.0)
        point2 = Vector3(440.0, 0.0, 0.0)
        point3 = Vector3(440.0, 440.0, 0.0)
        point4 = Vector3(0.0, 440.0, 0.0)
        point5 = Vector3(220.0, 220.0, 280.0)  # apex

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
        scad = self.create_scad()

        point1 = Vector3(0.0, 0.0, 0.0)
        point2 = Vector3(440.0, 0.0, 0.0)
        point3 = Vector3(440.0, 440.0, 0.0)
        point4 = Vector3(0.0, 440.0, 0.0)
        point5 = Vector3(220.0, 220.0, 280.0)  # apex

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
        Test where one face is being highlighted.
        """
        path_actual, path_expected = self.paths()
        scad = self.create_scad(unit_length_final=Unit.ROYAL_CUBIT)

        base = 440.0
        height = 280.0
        point1 = Vector3(0.0, 0.0, 0.0)
        point2 = Vector3(base, 0.0, 0.0)
        point3 = Vector3(base, base, 0.0)
        point4 = Vector3(0.0, base, 0.0)
        point5 = Vector3(base / 2.0, base / 2.0, height)  # apex

        faces = [[point1, point2, point3, point4],  # base plane
                 [point1, point5, point2],  # front
                 [point2, point5, point3],  # right side
                 [point3, point5, point4],  # back
                 [point4, point5, point1]]  # left side

        polyhedron = Polyhedron(faces=faces, highlight_faces=0)

        scad.run_super_scad(polyhedron, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialMetricCube(self):
        """
        Test for an imperial unit cube in metric units.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        cube = ImperialUnitCube()

        scad.run_super_scad(cube, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialImperialCube(self):
        """
        Test for an imperial unit cube in imperial units.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad(unit_length_final=Unit.INCH)
        cube = ImperialUnitCube()

        scad.run_super_scad(cube, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
