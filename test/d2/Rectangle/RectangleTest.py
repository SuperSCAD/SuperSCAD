from ScadTestCase import ScadTestCase
from super_scad.d2.Rectangle import Rectangle
from super_scad.Scad import Scad
from super_scad.type.Size2 import Size2
from super_scad.Unit import Unit
from test.d2.Rectangle.ImperialUnitRectangle import ImperialUnitRectangle


class RectangleTestCase(ScadTestCase):
    """
    Testcases for rectangles.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testRectangleBySize(self):
        """
        Test for a rectangle defined by size.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        rectangle = Rectangle(size=Size2(20, 10))

        self.assertAlmostEqual(20.0, rectangle.width)
        self.assertAlmostEqual(10.0, rectangle.depth)
        self.assertAlmostEqual(20.0, rectangle.size.width)
        self.assertAlmostEqual(10.0, rectangle.size.depth)
        self.assertFalse(rectangle.center)

        scad.run_super_scad(rectangle, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testRectangleByWidthAndDepth(self):
        """
        Test for a rectangle defined by width and depth.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        rectangle = Rectangle(size=Size2(20, 10), center=True)

        self.assertAlmostEqual(20.0, rectangle.width)
        self.assertAlmostEqual(10.0, rectangle.depth)
        self.assertAlmostEqual(20.0, rectangle.size.width)
        self.assertAlmostEqual(10.0, rectangle.size.depth)
        self.assertTrue(rectangle.center)

        scad.run_super_scad(rectangle, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialMetricRectangle(self):
        """
        Test for an imperial unit rectangle in metric units.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        rectangle = ImperialUnitRectangle()
        scad.run_super_scad(rectangle, path_actual)

        self.assertAlmostEqual(50.8, rectangle.imperial_rectangle.width)
        self.assertAlmostEqual(25.4, rectangle.imperial_rectangle.depth)
        self.assertAlmostEqual(50.8, rectangle.imperial_rectangle.size.width)
        self.assertAlmostEqual(25.4, rectangle.imperial_rectangle.size.depth)
        self.assertFalse(rectangle.imperial_rectangle.center)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialImperialRectangle(self):
        """
        Test for an imperial unit rectangle in imperial units.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.INCH)
        rectangle = ImperialUnitRectangle()
        scad.run_super_scad(rectangle, path_actual)

        self.assertAlmostEqual(2.0, rectangle.imperial_rectangle.width)
        self.assertAlmostEqual(1.0, rectangle.imperial_rectangle.depth)
        self.assertAlmostEqual(2.0, rectangle.imperial_rectangle.size.width)
        self.assertAlmostEqual(1.0, rectangle.imperial_rectangle.size.depth)
        self.assertFalse(rectangle.imperial_rectangle.center)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
