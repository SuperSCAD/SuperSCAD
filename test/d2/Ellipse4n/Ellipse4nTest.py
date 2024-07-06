from d2.Ellipse4n.ImperialUnitEllipse4n import ImperialUnitEllipse4n
from ScadTestCase import ScadTestCase
from super_scad.d2.Ellipse4n import Ellipse4n
from super_scad.scad.Scad import Scad
from super_scad.scad.Unit import Unit


class Ellipse4nTest(ScadTestCase):
    """
    Test cases for Ellipse4n.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testEllipse4nByRadius(self):
        """
        Test a plain ellipse4n defend by radius.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit_length_final=Unit.MM)
        ellipse4n = Ellipse4n(radius_x=20.0, radius_y=10.0)

        self.assertAlmostEqual(20.0, ellipse4n.radius_x)
        self.assertAlmostEqual(10.0, ellipse4n.radius_y)
        self.assertAlmostEqual(40.0, ellipse4n.diameter_x)
        self.assertAlmostEqual(20.0, ellipse4n.diameter_y)

        scad.run_super_scad(ellipse4n, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testEllipse4nByDiameter(self):
        """
        Test a plain ellipse4n defend by diameter.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit_length_final=Unit.MM)
        ellipse4n = Ellipse4n(diameter_x=40.0, diameter_y=20.0)

        self.assertAlmostEqual(20.0, ellipse4n.radius_x)
        self.assertAlmostEqual(10.0, ellipse4n.radius_y)
        self.assertAlmostEqual(40.0, ellipse4n.diameter_x)
        self.assertAlmostEqual(20.0, ellipse4n.diameter_y)

        scad.run_super_scad(ellipse4n, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialMetricEllipse4n(self):
        """
        Test for an imperial unit ellipse4n in metric units.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit_length_final=Unit.MM)
        ellipse4n = ImperialUnitEllipse4n()
        scad.run_super_scad(ellipse4n, path_actual)

        self.assertAlmostEqual(50.8, ellipse4n.imperial_ellipse.radius_x)
        self.assertAlmostEqual(25.4, ellipse4n.imperial_ellipse.radius_y)
        self.assertAlmostEqual(101.6, ellipse4n.imperial_ellipse.diameter_x)
        self.assertAlmostEqual(50.8, ellipse4n.imperial_ellipse.diameter_y)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialImperialEllipse4n(self):
        """
        Test for an imperial unit ellipse4n in imperial units.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit_length_final=Unit.INCH)
        ellipse4n = ImperialUnitEllipse4n()
        scad.run_super_scad(ellipse4n, path_actual)

        self.assertAlmostEqual(2.0, ellipse4n.imperial_ellipse.radius_x)
        self.assertAlmostEqual(1.0, ellipse4n.imperial_ellipse.radius_y)
        self.assertAlmostEqual(4.0, ellipse4n.imperial_ellipse.diameter_x)
        self.assertAlmostEqual(2.0, ellipse4n.imperial_ellipse.diameter_y)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
