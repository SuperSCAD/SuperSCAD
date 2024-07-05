from ScadTestCase import ScadTestCase
from super_scad.d3.Sphere import Sphere
from super_scad.Scad import Scad
from super_scad.transformation.Resize3D import Resize3D
from super_scad.type.Size3 import Size3
from super_scad.Unit import Unit


class Resize3DTest(ScadTestCase):
    """
    Test cases for Resize3D.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testAutoDepth(self):
        """
        Test cases for auto depth.
        """
        resize = Resize3D(new_size=Size3(30.0, 60.0, 10.0), child=Sphere(radius=10.0))

        self.assertAlmostEqual(resize.new_width, 30.0)
        self.assertAlmostEqual(resize.new_depth, 60.0)
        self.assertAlmostEqual(resize.new_height, 10.0)
        self.assertAlmostEqual(resize.new_size.width, 30.0)
        self.assertAlmostEqual(resize.new_size.depth, 60.0)
        self.assertAlmostEqual(resize.new_size.height, 10.0)
        self.assertFalse(resize.auto_width)
        self.assertFalse(resize.auto_depth)
        self.assertFalse(resize.auto_height)

        resize = Resize3D(new_size=Size3(30.0, 0.0, 0.0), child=Sphere(radius=10.0))

        self.assertAlmostEqual(resize.new_width, 30.0)
        self.assertAlmostEqual(resize.new_depth, 0.0)
        self.assertAlmostEqual(resize.new_height, 0.0)
        self.assertAlmostEqual(resize.new_size.width, 30.0)
        self.assertAlmostEqual(resize.new_size.depth, 0.0)
        self.assertAlmostEqual(resize.new_size.height, 0.0)
        self.assertFalse(resize.auto_width)
        self.assertFalse(resize.auto_depth)
        self.assertFalse(resize.auto_height)

        resize = Resize3D(new_size=Size3(0.0, 0.0, 30.0), auto=True, child=Sphere(radius=10.0))

        self.assertAlmostEqual(resize.new_width, 0.0)
        self.assertAlmostEqual(resize.new_depth, 0.0)
        self.assertAlmostEqual(resize.new_height, 30.0)
        self.assertAlmostEqual(resize.new_size.width, 0.0)
        self.assertAlmostEqual(resize.new_size.depth, 0.0)
        self.assertAlmostEqual(resize.new_size.height, 30.0)
        self.assertTrue(resize.auto_width)
        self.assertTrue(resize.auto_depth)
        self.assertFalse(resize.auto_height)

        resize = Resize3D(new_size=Size3(0.0, 0.0, 30.0), auto=(True, True, False), child=Sphere(radius=10.0))

        self.assertAlmostEqual(resize.new_width, 0.0)
        self.assertAlmostEqual(resize.new_depth, 0.0)
        self.assertAlmostEqual(resize.new_height, 30.0)
        self.assertAlmostEqual(resize.new_size.width, 0.0)
        self.assertAlmostEqual(resize.new_size.depth, 0.0)
        self.assertAlmostEqual(resize.new_size.height, 30.0)
        self.assertTrue(resize.auto_width)
        self.assertTrue(resize.auto_depth)
        self.assertFalse(resize.auto_height)

        resize = Resize3D(new_size=Size3(0.0, 0.0, 30.0), auto_depth=True, child=Sphere(radius=10.0))

        self.assertAlmostEqual(resize.new_width, 0.0)
        self.assertAlmostEqual(resize.new_depth, 0.0)
        self.assertAlmostEqual(resize.new_height, 30.0)
        self.assertAlmostEqual(resize.new_size.width, 0.0)
        self.assertAlmostEqual(resize.new_size.depth, 0.0)
        self.assertAlmostEqual(resize.new_size.height, 30.0)
        self.assertFalse(resize.auto_width)
        self.assertTrue(resize.auto_depth)
        self.assertFalse(resize.auto_height)

    # ------------------------------------------------------------------------------------------------------------------
    def testResizeByVector(self):
        """
        Test case for resize with 3 explicit sizes.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)

        resize = Resize3D(new_size=Size3(30.0, 60.0, 10.0), child=Sphere(radius=10.0))

        self.assertAlmostEqual(resize.new_width, 30.0)
        self.assertAlmostEqual(resize.new_depth, 60.0)
        self.assertAlmostEqual(resize.new_height, 10.0)
        self.assertAlmostEqual(resize.new_size.width, 30.0)
        self.assertAlmostEqual(resize.new_size.depth, 60.0)
        self.assertAlmostEqual(resize.new_size.height, 10.0)
        self.assertFalse(resize.auto_width)
        self.assertFalse(resize.auto_depth)
        self.assertFalse(resize.auto_height)

        scad.run_super_scad(resize, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testResizeBySizes(self):
        """
        Test case for resize with 3 explicit sizes.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)

        resize = Resize3D(new_width=30.0, new_depth=60.0, new_height=10.0, child=Sphere(radius=10.0))

        self.assertAlmostEqual(resize.new_width, 30.0)
        self.assertAlmostEqual(resize.new_depth, 60.0)
        self.assertAlmostEqual(resize.new_height, 10.0)
        self.assertAlmostEqual(resize.new_size.width, 30.0)
        self.assertAlmostEqual(resize.new_size.depth, 60.0)
        self.assertAlmostEqual(resize.new_size.height, 10.0)
        self.assertFalse(resize.auto_width)
        self.assertFalse(resize.auto_depth)
        self.assertFalse(resize.auto_height)

        scad.run_super_scad(resize, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testResizeByOneSizeAndTwoAutoSizeAsTuple(self):
        """
        Test case for resize with 1 explicit size (depth) and 2 auto sizes as a tuple.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)

        resize = Resize3D(new_depth=60.0, auto=(True, True, True), child=Sphere(radius=10.0))

        self.assertAlmostEqual(resize.new_width, 0.0)
        self.assertAlmostEqual(resize.new_depth, 60.0)
        self.assertAlmostEqual(resize.new_height, 0.0)
        self.assertAlmostEqual(resize.new_size.width, 0.0)
        self.assertAlmostEqual(resize.new_size.depth, 60.0)
        self.assertAlmostEqual(resize.new_size.height, 0.0)
        self.assertTrue(resize.auto_width)
        self.assertFalse(resize.auto_depth)
        self.assertTrue(resize.auto_height)

        scad.run_super_scad(resize, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testResizeByOneSizeAndTwoAutoSizeAsArgs(self):
        """
        Test case for resize with 1 explicit size and 2 auto sizes as a tuple.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)

        resize = Resize3D(new_depth=60.0, auto_width=True, auto_depth=True, auto_height=True, child=Sphere(radius=10.0))

        self.assertAlmostEqual(resize.new_width, 0.0)
        self.assertAlmostEqual(resize.new_depth, 60.0)
        self.assertAlmostEqual(resize.new_height, 0.0)
        self.assertAlmostEqual(resize.new_size.width, 0.0)
        self.assertAlmostEqual(resize.new_size.depth, 60.0)
        self.assertAlmostEqual(resize.new_size.height, 0.0)
        self.assertTrue(resize.auto_width)
        self.assertFalse(resize.auto_depth)
        self.assertTrue(resize.auto_height)

        scad.run_super_scad(resize, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testResizeByOneSizeAndTwoAutoSize(self):
        """
        Test case for resize with 1 explicit size and 2 auto sizes.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)

        resize = Resize3D(new_depth=60.0, auto=True, child=Sphere(radius=10.0))

        self.assertAlmostEqual(resize.new_width, 0.0)
        self.assertAlmostEqual(resize.new_depth, 60.0)
        self.assertAlmostEqual(resize.new_height, 0.0)
        self.assertAlmostEqual(resize.new_size.width, 0.0)
        self.assertAlmostEqual(resize.new_size.depth, 60.0)
        self.assertAlmostEqual(resize.new_size.height, 0.0)
        self.assertTrue(resize.auto_width)
        self.assertFalse(resize.auto_depth)
        self.assertTrue(resize.auto_height)

        scad.run_super_scad(resize, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
