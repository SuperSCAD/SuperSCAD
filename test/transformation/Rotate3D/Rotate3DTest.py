import math

from ScadTestCase import ScadTestCase
from super_scad.boolean.Union import Union
from super_scad.d3.Cube import Cube
from super_scad.d3.Cuboid import Cuboid
from super_scad.d3.Cylinder import Cylinder
from super_scad.transformation.Paint import Paint
from super_scad.transformation.Rotate3D import Rotate3D
from super_scad.type.Color import Color
from super_scad.type.Vector3 import Vector3


class Rotate3DTest(ScadTestCase):
    """
    Test case for rotate.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_rotate_point3(self):
        """
        Test case for rotate with Point3.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()

        end_point = Vector3(x=10.0, y=10.0, z=10.0)
        length = end_point.length
        b = math.degrees(math.acos(end_point.z / length))
        c = math.degrees(math.atan2(end_point.y, end_point.x))

        rotate = Rotate3D(angle=Vector3(0.0, b, c), child=Cylinder(height=length, radius=0.5))
        cube = Paint(color=Color('gray', alpha=0.5), child=Cube(size=end_point.x))

        self.assertAlmostEqual(rotate.angle_x, 0.0)
        self.assertAlmostEqual(rotate.angle_y, b)
        self.assertAlmostEqual(rotate.angle_z, c)
        self.assertAlmostEqual(rotate.angle.x, 0.0)
        self.assertAlmostEqual(rotate.angle.y, b)
        self.assertAlmostEqual(rotate.angle.z, c)
        self.assertIsNone(rotate.vector)

        union = Union(children=[rotate, cube])

        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_rotate_angles(self):
        """
        Test case for rotate with angles.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()

        end_point = Vector3(x=10.0, y=10.0, z=10.0)
        length = end_point.length
        b = math.degrees(math.acos(end_point.z / length))
        c = math.degrees(math.atan2(end_point.y, end_point.x))

        rotate = Rotate3D(angle_y=b, angle_z=c, child=Cylinder(height=length, radius=0.5))
        cube = Paint(color=Color('gray', alpha=0.5), child=Cube(size=end_point.x))

        self.assertIsNone(rotate.vector)
        self.assertAlmostEqual(rotate.angle_x, 0.0)
        self.assertAlmostEqual(rotate.angle_y, b)
        self.assertAlmostEqual(rotate.angle_z, c)
        self.assertAlmostEqual(rotate.angle.x, 0.0)
        self.assertAlmostEqual(rotate.angle.y, b)
        self.assertAlmostEqual(rotate.angle.z, c)

        union = Union(children=[rotate, cube])

        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_rotate_vector(self):
        """
        Test case for rotate around a vector.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()

        rotate = Rotate3D(angle=45.0, vector=Vector3(1, 1, 0), child=Cuboid(width=50, depth=30, height=15))

        self.assertIsNone(rotate.angle_x)
        self.assertIsNone(rotate.angle_y)
        self.assertIsNone(rotate.angle_z)
        self.assertAlmostEqual(rotate.angle, 45.0)
        self.assertAlmostEqual(rotate.vector.x, 1.0)
        self.assertAlmostEqual(rotate.vector.y, 1.0)
        self.assertAlmostEqual(rotate.vector.z, 0.0)

        scad.run_super_scad(rotate, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
