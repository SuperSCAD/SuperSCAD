from d2.RightTriangle.ImperialUnitRightTriangle import ImperialUnitRightTriangle
from ScadTestCase import ScadTestCase
from super_scad.d2.RightTriangle import RightTriangle
from super_scad.scad.Scad import Scad
from super_scad.scad.Unit import Unit


class RightTriangleTest(ScadTestCase):
    """
    Test cases for RightTriangle.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testPlainRightTriangle(self):
        """
        Test a plain right triangle.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        triangle = RightTriangle(width=20.0, depth=10.0)

        self.assertAlmostEqual(20.0, triangle.width)
        self.assertAlmostEqual(10.0, triangle.depth)

        scad.run_super_scad(triangle, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialMetricRightTriangle(self):
        """
        Test for an imperial unit rightTriangle in metric units.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        right_triangle = ImperialUnitRightTriangle()
        scad.run_super_scad(right_triangle, path_actual)

        self.assertAlmostEqual(50.8, right_triangle.imperial_right_triangle.width)
        self.assertAlmostEqual(25.4, right_triangle.imperial_right_triangle.depth)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialImperialRightTriangle(self):
        """
        Test for an imperial unit rightTriangle in imperial units.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.INCH)
        right_triangle = ImperialUnitRightTriangle()
        scad.run_super_scad(right_triangle, path_actual)

        self.assertAlmostEqual(2.0, right_triangle.imperial_right_triangle.width)
        self.assertAlmostEqual(1.0, right_triangle.imperial_right_triangle.depth)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
