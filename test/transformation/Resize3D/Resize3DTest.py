from ScadTestCase import ScadTestCase
from super_scad.d3.Sphere import Sphere
from super_scad.transformation.Resize3D import Resize3D
from super_scad.type.Vector3 import Vector3


class Resize3DTest(ScadTestCase):
    """
    Test cases for Resize3D.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_auto_depth(self):
        """
        Test cases for auto depth.
        """
        resize = Resize3D(new_size=Vector3(30.0, 60.0, 10.0), child=Sphere(radius=10.0))

        self.assertAlmostEqual(resize.new_width, 30.0)
        self.assertAlmostEqual(resize.new_depth, 60.0)
        self.assertAlmostEqual(resize.new_height, 10.0)
        self.assertAlmostEqual(resize.new_size.x, 30.0)
        self.assertAlmostEqual(resize.new_size.y, 60.0)
        self.assertAlmostEqual(resize.new_size.z, 10.0)
        self.assertFalse(resize.auto_width)
        self.assertFalse(resize.auto_depth)
        self.assertFalse(resize.auto_height)

        resize = Resize3D(new_size=Vector3(30.0, 0.0, 0.0), child=Sphere(radius=10.0))

        self.assertAlmostEqual(resize.new_width, 30.0)
        self.assertAlmostEqual(resize.new_depth, 0.0)
        self.assertAlmostEqual(resize.new_height, 0.0)
        self.assertAlmostEqual(resize.new_size.x, 30.0)
        self.assertAlmostEqual(resize.new_size.y, 0.0)
        self.assertAlmostEqual(resize.new_size.z, 0.0)
        self.assertFalse(resize.auto_width)
        self.assertFalse(resize.auto_depth)
        self.assertFalse(resize.auto_height)

        resize = Resize3D(new_size=Vector3(0.0, 0.0, 30.0), auto=True, child=Sphere(radius=10.0))

        self.assertAlmostEqual(resize.new_width, 0.0)
        self.assertAlmostEqual(resize.new_depth, 0.0)
        self.assertAlmostEqual(resize.new_height, 30.0)
        self.assertAlmostEqual(resize.new_size.x, 0.0)
        self.assertAlmostEqual(resize.new_size.y, 0.0)
        self.assertAlmostEqual(resize.new_size.z, 30.0)
        self.assertTrue(resize.auto_width)
        self.assertTrue(resize.auto_depth)
        self.assertFalse(resize.auto_height)

        resize = Resize3D(new_size=Vector3(0.0, 0.0, 30.0), auto=(True, True, False), child=Sphere(radius=10.0))

        self.assertAlmostEqual(resize.new_width, 0.0)
        self.assertAlmostEqual(resize.new_depth, 0.0)
        self.assertAlmostEqual(resize.new_height, 30.0)
        self.assertAlmostEqual(resize.new_size.x, 0.0)
        self.assertAlmostEqual(resize.new_size.y, 0.0)
        self.assertAlmostEqual(resize.new_size.z, 30.0)
        self.assertTrue(resize.auto_width)
        self.assertTrue(resize.auto_depth)
        self.assertFalse(resize.auto_height)

        resize = Resize3D(new_size=Vector3(0.0, 0.0, 30.0), auto_depth=True, child=Sphere(radius=10.0))

        self.assertAlmostEqual(resize.new_width, 0.0)
        self.assertAlmostEqual(resize.new_depth, 0.0)
        self.assertAlmostEqual(resize.new_height, 30.0)
        self.assertAlmostEqual(resize.new_size.x, 0.0)
        self.assertAlmostEqual(resize.new_size.y, 0.0)
        self.assertAlmostEqual(resize.new_size.z, 30.0)
        self.assertFalse(resize.auto_width)
        self.assertTrue(resize.auto_depth)
        self.assertFalse(resize.auto_height)

    # ------------------------------------------------------------------------------------------------------------------
    def test_resize_by_vector(self):
        """
        Test case for resize with 3 explicit sizes.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()

        resize = Resize3D(new_size=Vector3(30.0, 60.0, 10.0), child=Sphere(radius=10.0))

        self.assertAlmostEqual(resize.new_width, 30.0)
        self.assertAlmostEqual(resize.new_depth, 60.0)
        self.assertAlmostEqual(resize.new_height, 10.0)
        self.assertAlmostEqual(resize.new_size.x, 30.0)
        self.assertAlmostEqual(resize.new_size.y, 60.0)
        self.assertAlmostEqual(resize.new_size.z, 10.0)
        self.assertFalse(resize.auto_width)
        self.assertFalse(resize.auto_depth)
        self.assertFalse(resize.auto_height)

        scad.run_super_scad(resize, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_resize_by_sizes(self):
        """
        Test case for resize with 3 explicit sizes.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()

        resize = Resize3D(new_width=30.0, new_depth=60.0, new_height=10.0, child=Sphere(radius=10.0))

        self.assertAlmostEqual(resize.new_width, 30.0)
        self.assertAlmostEqual(resize.new_depth, 60.0)
        self.assertAlmostEqual(resize.new_height, 10.0)
        self.assertAlmostEqual(resize.new_size.x, 30.0)
        self.assertAlmostEqual(resize.new_size.y, 60.0)
        self.assertAlmostEqual(resize.new_size.z, 10.0)
        self.assertFalse(resize.auto_width)
        self.assertFalse(resize.auto_depth)
        self.assertFalse(resize.auto_height)

        scad.run_super_scad(resize, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_resize_by_one_size_and_two_auto_size_as_tuple(self):
        """
        Test case for resize with 1 explicit size (depth) and 2 auto sizes as a tuple.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()

        resize = Resize3D(new_depth=60.0, auto=(True, True, True), child=Sphere(radius=10.0))

        self.assertAlmostEqual(resize.new_width, 0.0)
        self.assertAlmostEqual(resize.new_depth, 60.0)
        self.assertAlmostEqual(resize.new_height, 0.0)
        self.assertAlmostEqual(resize.new_size.x, 0.0)
        self.assertAlmostEqual(resize.new_size.y, 60.0)
        self.assertAlmostEqual(resize.new_size.z, 0.0)
        self.assertTrue(resize.auto_width)
        self.assertFalse(resize.auto_depth)
        self.assertTrue(resize.auto_height)

        scad.run_super_scad(resize, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_resize_by_one_size_and_two_auto_size_as_args(self):
        """
        Test case for resize with 1 explicit size and 2 auto sizes as a tuple.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()

        resize = Resize3D(new_depth=60.0, auto_width=True, auto_depth=True, auto_height=True, child=Sphere(radius=10.0))

        self.assertAlmostEqual(resize.new_width, 0.0)
        self.assertAlmostEqual(resize.new_depth, 60.0)
        self.assertAlmostEqual(resize.new_height, 0.0)
        self.assertAlmostEqual(resize.new_size.x, 0.0)
        self.assertAlmostEqual(resize.new_size.y, 60.0)
        self.assertAlmostEqual(resize.new_size.z, 0.0)
        self.assertTrue(resize.auto_width)
        self.assertFalse(resize.auto_depth)
        self.assertTrue(resize.auto_height)

        scad.run_super_scad(resize, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_resize_by_one_size_and_two_auto_size(self):
        """
        Test case for resize with 1 explicit size and 2 auto sizes.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()

        resize = Resize3D(new_depth=60.0, auto=True, child=Sphere(radius=10.0))

        self.assertAlmostEqual(resize.new_width, 0.0)
        self.assertAlmostEqual(resize.new_depth, 60.0)
        self.assertAlmostEqual(resize.new_height, 0.0)
        self.assertAlmostEqual(resize.new_size.x, 0.0)
        self.assertAlmostEqual(resize.new_size.y, 60.0)
        self.assertAlmostEqual(resize.new_size.z, 0.0)
        self.assertTrue(resize.auto_width)
        self.assertFalse(resize.auto_depth)
        self.assertTrue(resize.auto_height)

        scad.run_super_scad(resize, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
