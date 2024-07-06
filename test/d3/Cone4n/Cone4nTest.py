from d3.Cone4n.ImperialCone4n import ImperialCone4n
from ScadTestCase import ScadTestCase
from super_scad.d3.Cone4n import Cone4n
from super_scad.scad.Scad import Scad
from super_scad.scad.Unit import Unit


class ConeTestCase(ScadTestCase):
    """
    Testcases for cone.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testConeRadius(self):
        """
        Test for a cone defined by radii.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        cone = Cone4n(height=10.0, bottom_radius=3.0, top_radius=2.0)

        self.assertAlmostEqual(10.0, cone.height)
        self.assertAlmostEqual(2.0, cone.top_radius)
        self.assertAlmostEqual(4.0, cone.top_diameter)
        self.assertAlmostEqual(3.0, cone.bottom_radius)
        self.assertAlmostEqual(6.0, cone.bottom_diameter)

        scad.run_super_scad(cone, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testConeDiameter(self):
        """
        Test for a cone defined by a diameter.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        cone = Cone4n(height=10.0, bottom_diameter=3.0, top_diameter=2.0, center=True)

        self.assertAlmostEqual(10.0, cone.height)
        self.assertAlmostEqual(1.0, cone.top_radius)
        self.assertAlmostEqual(2.0, cone.top_diameter)
        self.assertAlmostEqual(1.5, cone.bottom_radius)
        self.assertAlmostEqual(3.0, cone.bottom_diameter)

        scad.run_super_scad(cone, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialMetricCone4n(self):
        """
        Test for an imperial cone in metric units.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        cone = ImperialCone4n(height=100.0, bottom_radius=25.0, top_radius=20.0)
        scad.run_super_scad(cone, path_actual)

        self.assertAlmostEqual(100.0 * 25.4, cone.imperial_cone.height)
        self.assertAlmostEqual(20.0 * 25.4, cone.imperial_cone.top_radius)
        self.assertAlmostEqual(40.0 * 25.4, cone.imperial_cone.top_diameter)
        self.assertAlmostEqual(25.0 * 25.4, cone.imperial_cone.bottom_radius)
        self.assertAlmostEqual(50.0 * 25.4, cone.imperial_cone.bottom_diameter)
        self.assertFalse(cone.imperial_cone.center)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialImperialCone4n(self):
        """
        Test for an imperial cone in imperial units.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.INCH)
        cone = ImperialCone4n(height=100.0, bottom_radius=25.0, top_radius=20.0)
        scad.run_super_scad(cone, path_actual)

        self.assertAlmostEqual(100.0, cone.imperial_cone.height)
        self.assertAlmostEqual(20.0, cone.imperial_cone.top_radius)
        self.assertAlmostEqual(40.0, cone.imperial_cone.top_diameter)
        self.assertAlmostEqual(25.0, cone.imperial_cone.bottom_radius)
        self.assertAlmostEqual(50.0, cone.imperial_cone.bottom_diameter)
        self.assertFalse(cone.imperial_cone.center)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
