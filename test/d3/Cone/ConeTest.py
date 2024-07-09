from d3.Cone.ImperialCone import ImperialCone
from ScadTestCase import ScadTestCase
from super_scad.d3.Cone import Cone
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

        scad = Scad(unit_length_final=Unit.MM)
        cone = Cone(height=10.0, top_radius=2.0, bottom_radius=3.0)

        self.assertAlmostEqual(10.0, cone.height)
        self.assertAlmostEqual(2.0, cone.top_radius)
        self.assertAlmostEqual(4.0, cone.top_diameter)
        self.assertAlmostEqual(3.0, cone.bottom_radius)
        self.assertAlmostEqual(6.0, cone.bottom_diameter)
        self.assertFalse(cone.center)
        self.assertIsNone(cone.fa)
        self.assertIsNone(cone.fs)
        self.assertIsNone(cone.fn)

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

        scad = Scad(unit_length_final=Unit.MM)
        cone = Cone(height=10.0, bottom_diameter=3.0, top_diameter=2.0, center=True)

        self.assertAlmostEqual(10.0, cone.height)
        self.assertAlmostEqual(1.0, cone.top_radius)
        self.assertAlmostEqual(2.0, cone.top_diameter)
        self.assertAlmostEqual(1.5, cone.bottom_radius)
        self.assertAlmostEqual(3.0, cone.bottom_diameter)
        self.assertTrue(cone.center)
        self.assertIsNone(cone.fa)
        self.assertIsNone(cone.fs)
        self.assertIsNone(cone.fn)

        scad.run_super_scad(cone, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testCone4n(self):
        """
        Test for a cone with a multiple of 4 vertices.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit_length_final=Unit.MM)
        cone = Cone(height=10.0, bottom_radius=3.0, top_radius=2.0, fn4n=True)

        self.assertAlmostEqual(10.0, cone.height)
        self.assertAlmostEqual(2.0, cone.top_radius)
        self.assertAlmostEqual(4.0, cone.top_diameter)
        self.assertAlmostEqual(3.0, cone.bottom_radius)
        self.assertAlmostEqual(6.0, cone.bottom_diameter)
        self.assertIsNone(cone.fn)
        self.assertTrue(cone.fn4n)

        scad.run_super_scad(cone, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testConeAuxiliaryParameter(self):
        """
        Test auxiliary parameters.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit_length_final=Unit.MM)
        cone = Cone(height=100.0, bottom_diameter=15.0, top_diameter=10.0, fa=12.0, fs=2.0, fn=0)

        self.assertAlmostEqual(100.0, cone.height)
        self.assertAlmostEqual(5.0, cone.top_radius)
        self.assertAlmostEqual(10.0, cone.top_diameter)
        self.assertAlmostEqual(7.5, cone.bottom_radius)
        self.assertAlmostEqual(15.0, cone.bottom_diameter)
        self.assertFalse(cone.center)
        self.assertAlmostEqual(12.0, cone.fa)
        self.assertAlmostEqual(2.0, cone.fs)
        self.assertEqual(0, cone.fn)
        self.assertFalse(cone.fn4n)

        scad.run_super_scad(cone, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialMetricCone(self):
        """
        Test for an imperial cone in metric units.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit_length_final=Unit.MM)
        cone = ImperialCone(height=100.0, bottom_radius=25.0, top_radius=20.0, fa=12.0, fs=2.0, fn=0)
        scad.run_super_scad(cone, path_actual)

        self.assertAlmostEqual(100.0 * 25.4, cone.imperial_cone.height)
        self.assertAlmostEqual(20.0 * 25.4, cone.imperial_cone.top_radius)
        self.assertAlmostEqual(40.0 * 25.4, cone.imperial_cone.top_diameter)
        self.assertAlmostEqual(25.0 * 25.4, cone.imperial_cone.bottom_radius)
        self.assertAlmostEqual(50.0 * 25.4, cone.imperial_cone.bottom_diameter)
        self.assertFalse(cone.imperial_cone.center)
        self.assertAlmostEqual(12.0, cone.imperial_cone.fa)
        self.assertAlmostEqual(2.0 * 25.4, cone.imperial_cone.fs)
        self.assertEqual(0, cone.imperial_cone.fn)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialImperialCone(self):
        """
        Test for an imperial cone in imperial units.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit_length_final=Unit.INCH)
        cone = ImperialCone(height=100.0, bottom_radius=25.0, top_radius=20.0, fa=12.0, fs=2.0, fn=0)
        scad.run_super_scad(cone, path_actual)

        self.assertAlmostEqual(100.0, cone.imperial_cone.height)
        self.assertAlmostEqual(20.0, cone.imperial_cone.top_radius)
        self.assertAlmostEqual(40.0, cone.imperial_cone.top_diameter)
        self.assertAlmostEqual(25.0, cone.imperial_cone.bottom_radius)
        self.assertAlmostEqual(50.0, cone.imperial_cone.bottom_diameter)
        self.assertFalse(cone.imperial_cone.center)
        self.assertAlmostEqual(12.0, cone.imperial_cone.fa)
        self.assertAlmostEqual(2.0, cone.imperial_cone.fs)
        self.assertEqual(0, cone.imperial_cone.fn)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
