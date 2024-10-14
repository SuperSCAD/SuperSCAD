from ScadTestCase import ScadTestCase
from super_scad.d2.Circle import Circle
from super_scad.scad.Scad import Scad
from super_scad.scad.Unit import Unit
from super_scad.transformation.Resize2D import Resize2D
from super_scad.type.Size2 import Size2


class Resize2DTest(ScadTestCase):
    """
    Test cases for Resize2D.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testAutoDepth(self):
        """
        Test cases for auto depth.
        """
        resize = Resize2D(new_size=Size2(30.0, 60.0), child=Circle(radius=10.0))

        self.assertAlmostEqual(resize.new_width, 30.0)
        self.assertAlmostEqual(resize.new_depth, 60.0)
        self.assertAlmostEqual(resize.new_size.width, 30.0)
        self.assertAlmostEqual(resize.new_size.depth, 60.0)
        self.assertFalse(resize.auto_width)
        self.assertFalse(resize.auto_depth)

        resize = Resize2D(new_size=Size2(30.0, 0.0), child=Circle(radius=10.0))

        self.assertAlmostEqual(resize.new_width, 30.0)
        self.assertAlmostEqual(resize.new_depth, 0.0)
        self.assertAlmostEqual(resize.new_size.width, 30.0)
        self.assertAlmostEqual(resize.new_size.depth, 0.0)
        self.assertFalse(resize.auto_width)
        self.assertFalse(resize.auto_depth)

        resize = Resize2D(new_size=Size2(30.0, 0.0), auto=True, child=Circle(radius=10.0))

        self.assertAlmostEqual(resize.new_width, 30.0)
        self.assertAlmostEqual(resize.new_depth, 0.0)
        self.assertAlmostEqual(resize.new_size.width, 30.0)
        self.assertAlmostEqual(resize.new_size.depth, 0.0)
        self.assertFalse(resize.auto_width)
        self.assertTrue(resize.auto_depth)

        resize = Resize2D(new_size=Size2(30.0, 0.0), auto_depth=True, child=Circle(radius=10.0))

        self.assertAlmostEqual(resize.new_width, 30.0)
        self.assertAlmostEqual(resize.new_depth, 0.0)
        self.assertAlmostEqual(resize.new_size.width, 30.0)
        self.assertAlmostEqual(resize.new_size.depth, 0.0)
        self.assertFalse(resize.auto_width)
        self.assertTrue(resize.auto_depth)

        resize = Resize2D(new_size=Size2(30.0, 0.0), auto=(True, True), child=Circle(radius=10.0))

        self.assertAlmostEqual(resize.new_width, 30.0)
        self.assertAlmostEqual(resize.new_depth, 0.0)
        self.assertAlmostEqual(resize.new_size.width, 30.0)
        self.assertAlmostEqual(resize.new_size.depth, 0.0)
        self.assertFalse(resize.auto_width)
        self.assertTrue(resize.auto_depth)

        resize = Resize2D(new_size=Size2(0.0, 60.0), child=Circle(radius=10.0))

        self.assertAlmostEqual(resize.new_width, 0.0)
        self.assertAlmostEqual(resize.new_depth, 60.0)
        self.assertAlmostEqual(resize.new_size.width, 0.0)
        self.assertAlmostEqual(resize.new_size.depth, 60.0)
        self.assertFalse(resize.auto_width)
        self.assertFalse(resize.auto_depth)

    # ------------------------------------------------------------------------------------------------------------------
    def testResizeByVector(self):
        """
        Test case for resize with 2 explicit sizes.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()

        resize = Resize2D(new_size=Size2(30.0, 60.0), child=Circle(radius=10.0))

        self.assertAlmostEqual(resize.new_width, 30.0)
        self.assertAlmostEqual(resize.new_depth, 60.0)
        self.assertAlmostEqual(resize.new_size.width, 30.0)
        self.assertAlmostEqual(resize.new_size.depth, 60.0)
        self.assertFalse(resize.auto_width)
        self.assertFalse(resize.auto_depth)

        scad.run_super_scad(resize, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testResizeBySizes(self):
        """
        Test case for resize with 2 explicit sizes.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()

        resize = Resize2D(new_width=30.0, new_depth=60.0, child=Circle(radius=10.0))

        self.assertAlmostEqual(resize.new_width, 30.0)
        self.assertAlmostEqual(resize.new_depth, 60.0)
        self.assertAlmostEqual(resize.new_size.width, 30.0)
        self.assertAlmostEqual(resize.new_size.depth, 60.0)
        self.assertFalse(resize.auto_width)
        self.assertFalse(resize.auto_depth)

        scad.run_super_scad(resize, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testResizeByOneSizeAndOneAutoSizeAsTuple(self):
        """
        Test case for resize with 1 explicit size (depth) and 1 auto size as a tuple.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()

        resize = Resize2D(new_depth=60.0, auto=(True, True), child=Circle(radius=10.0))

        self.assertAlmostEqual(resize.new_width, 0.0)
        self.assertAlmostEqual(resize.new_depth, 60.0)
        self.assertAlmostEqual(resize.new_size.width, 0.0)
        self.assertAlmostEqual(resize.new_size.depth, 60.0)
        self.assertTrue(resize.auto_width)
        self.assertFalse(resize.auto_depth)

        scad.run_super_scad(resize, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testResizeByOneSizeAndOneAutoSizeAsArgs(self):
        """
        Test case for resize with 1 explicit size and 1 auto size as a tuple.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()

        resize = Resize2D(new_depth=60.0, auto_width=True, auto_depth=True, child=Circle(radius=10.0))

        self.assertAlmostEqual(resize.new_width, 0.0)
        self.assertAlmostEqual(resize.new_depth, 60.0)
        self.assertAlmostEqual(resize.new_size.width, 0.0)
        self.assertAlmostEqual(resize.new_size.depth, 60.0)
        self.assertTrue(resize.auto_width)
        self.assertFalse(resize.auto_depth)

        scad.run_super_scad(resize, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testResizeByOneSizeAndOneAutoSize(self):
        """
        Test case for resize with 1 explicit size and 1 auto size.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()

        resize = Resize2D(new_depth=60.0, auto=True, child=Circle(radius=10.0))

        self.assertAlmostEqual(resize.new_width, 0.0)
        self.assertAlmostEqual(resize.new_depth, 60.0)
        self.assertAlmostEqual(resize.new_size.width, 0.0)
        self.assertAlmostEqual(resize.new_size.depth, 60.0)
        self.assertTrue(resize.auto_width)
        self.assertFalse(resize.auto_depth)

        scad.run_super_scad(resize, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
