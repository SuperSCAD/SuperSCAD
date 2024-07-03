from d3.Cylinder4n.ImperialCylinder4n import ImperialCylinder4n
from ScadTestCase import ScadTestCase
from super_scad.d3.Cylinder4n import Cylinder4n
from super_scad.Scad import Scad
from super_scad.Unit import Unit


class Cylinder4nTestCase(ScadTestCase):
    """
    Testcases for Cylinder4n.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testCylinder4nRadius(self):
        """
        Test for a cylinder defined by a radius.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        cylinder = Cylinder4n(height=10.0, radius=2.0)

        self.assertAlmostEqual(10.0, cylinder.height)
        self.assertAlmostEqual(2.0, cylinder.radius)
        self.assertAlmostEqual(4.0, cylinder.diameter)
        self.assertFalse(cylinder.center)

        scad.run_super_scad(cylinder, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testCylinder4nDiameter(self):
        """
        Test for a cylinder defined by a diameter.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        cylinder = Cylinder4n(height=10.0, diameter=2.0, center=True)

        self.assertAlmostEqual(10.0, cylinder.height)
        self.assertAlmostEqual(1.0, cylinder.radius)
        self.assertAlmostEqual(2.0, cylinder.diameter)
        self.assertTrue(cylinder.center)

        scad.run_super_scad(cylinder, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialMetricCylinder4n(self):
        """
        Test for an imperial cylinder in metric units.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        cylinder = ImperialCylinder4n(height=100.0, radius=20.0)
        scad.run_super_scad(cylinder, path_actual)

        self.assertAlmostEqual(100.0 * 25.4, cylinder.imperial_cylinder.height)
        self.assertAlmostEqual(20.0 * 25.4, cylinder.imperial_cylinder.radius)
        self.assertAlmostEqual(40.0 * 25.4, cylinder.imperial_cylinder.diameter)
        self.assertFalse(cylinder.imperial_cylinder.center)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialImperialCylinder4n(self):
        """
        Test for an imperial cylinder in imperial units.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.INCH)
        cylinder = ImperialCylinder4n(height=100.0, radius=20.0)
        scad.run_super_scad(cylinder, path_actual)

        self.assertAlmostEqual(100.0, cylinder.imperial_cylinder.height)
        self.assertAlmostEqual(20.0, cylinder.imperial_cylinder.radius)
        self.assertAlmostEqual(40.0, cylinder.imperial_cylinder.diameter)
        self.assertFalse(cylinder.imperial_cylinder.center)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
