from d3.Cylinder.ImperialCylinder import ImperialCylinder
from ScadTestCase import ScadTestCase
from super_scad.d3.Cylinder import Cylinder
from super_scad.scad.Scad import Scad
from super_scad.scad.Unit import Unit


class CylinderTestCase(ScadTestCase):
    """
    Testcases for cylinder.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testCylinderRadius(self):
        """
        Test for a cylinder defined by a radius.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        cylinder = Cylinder(height=10.0, radius=2.0)

        self.assertAlmostEqual(10.0, cylinder.height)
        self.assertAlmostEqual(2.0, cylinder.radius)
        self.assertAlmostEqual(4.0, cylinder.diameter)
        self.assertFalse(cylinder.center)
        self.assertIsNone(cylinder.fa)
        self.assertIsNone(cylinder.fs)
        self.assertIsNone(cylinder.fn)

        scad.run_super_scad(cylinder, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testCylinderDiameter(self):
        """
        Test for a cylinder defined by a diameter.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        cylinder = Cylinder(height=10.0, diameter=2.0, center=True)

        self.assertAlmostEqual(10.0, cylinder.height)
        self.assertAlmostEqual(1.0, cylinder.radius)
        self.assertAlmostEqual(2.0, cylinder.diameter)
        self.assertTrue(cylinder.center)
        self.assertIsNone(cylinder.fa)
        self.assertIsNone(cylinder.fs)
        self.assertIsNone(cylinder.fn)

        scad.run_super_scad(cylinder, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testCylinderAuxiliaryParameter(self):
        """
        Test auxiliary parameters.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        cylinder = Cylinder(height=100.0, diameter=10.0, fa=12.0, fs=2.0, fn=0)

        self.assertAlmostEqual(100.0, cylinder.height)
        self.assertAlmostEqual(5.0, cylinder.radius)
        self.assertAlmostEqual(10.0, cylinder.diameter)
        self.assertFalse(cylinder.center)
        self.assertAlmostEqual(12.0, cylinder.fa)
        self.assertAlmostEqual(2.0, cylinder.fs)
        self.assertEqual(0, cylinder.fn)

        scad.run_super_scad(cylinder, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialMetricCylinder(self):
        """
        Test for an imperial cylinder in metric units.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        cylinder = ImperialCylinder(height=100.0, radius=20.0, fa=12.0, fs=2.0, fn=0)
        scad.run_super_scad(cylinder, path_actual)

        self.assertAlmostEqual(100.0 * 25.4, cylinder.imperial_cylinder.height)
        self.assertAlmostEqual(20.0 * 25.4, cylinder.imperial_cylinder.radius)
        self.assertAlmostEqual(40.0 * 25.4, cylinder.imperial_cylinder.diameter)
        self.assertFalse(cylinder.imperial_cylinder.center)
        self.assertAlmostEqual(12.0, cylinder.imperial_cylinder.fa)
        self.assertAlmostEqual(2.0 * 25.4, cylinder.imperial_cylinder.fs)
        self.assertEqual(0, cylinder.imperial_cylinder.fn)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialImperialCylinder(self):
        """
        Test for an imperial cylinder in imperial units.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.INCH)
        cylinder = ImperialCylinder(height=100.0, radius=20.0, fa=12.0, fs=2.0, fn=0)
        scad.run_super_scad(cylinder, path_actual)

        self.assertAlmostEqual(100.0, cylinder.imperial_cylinder.height)
        self.assertAlmostEqual(20.0, cylinder.imperial_cylinder.radius)
        self.assertAlmostEqual(40.0, cylinder.imperial_cylinder.diameter)
        self.assertFalse(cylinder.imperial_cylinder.center)
        self.assertAlmostEqual(12.0, cylinder.imperial_cylinder.fa)
        self.assertAlmostEqual(2.0, cylinder.imperial_cylinder.fs)
        self.assertEqual(0, cylinder.imperial_cylinder.fn)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
