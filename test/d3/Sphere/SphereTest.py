from d3.Sphere.ImperialSphere import ImperialSphere
from ScadTestCase import ScadTestCase
from super_scad.d3.Sphere import Sphere
from super_scad.scad.Scad import Scad
from super_scad.scad.Unit import Unit


class SphereTestCase(ScadTestCase):
    """
    Testcases for sphere.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testSphereRadius(self):
        """
        Test for a sphere defined by a radius.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit_length_final=Unit.MM)
        sphere = Sphere(radius=2.0)

        self.assertAlmostEqual(2.0, sphere.radius)
        self.assertAlmostEqual(4.0, sphere.diameter)

        scad.run_super_scad(sphere, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testSphereDiameter(self):
        """
        Test for a sphere defined by a diameter.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit_length_final=Unit.MM)
        sphere = Sphere(diameter=2.0)

        self.assertAlmostEqual(1.0, sphere.radius)
        self.assertAlmostEqual(2.0, sphere.diameter)
        self.assertIsNone(sphere.fa)
        self.assertIsNone(sphere.fs)
        self.assertIsNone(sphere.fn)

        scad.run_super_scad(sphere, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testSphere4n(self):
        """
        Test for a sphere with a multiple of 4 vertices.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit_length_final=Unit.MM)
        sphere = Sphere(radius=2.0, fn4n=True)

        self.assertAlmostEqual(2.0, sphere.radius)
        self.assertAlmostEqual(4.0, sphere.diameter)
        self.assertIsNone(sphere.fn)
        self.assertTrue(sphere.fn4n)

        scad.run_super_scad(sphere, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testSphereAuxiliaryParameter(self):
        """
        Test auxiliary parameters.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit_length_final=Unit.MM)
        sphere = Sphere(diameter=10.0, fa=12.0, fs=2.0, fn=0)

        self.assertAlmostEqual(5.0, sphere.radius)
        self.assertAlmostEqual(10.0, sphere.diameter)
        self.assertAlmostEqual(12.0, sphere.fa)
        self.assertAlmostEqual(2.0, sphere.fs)
        self.assertEqual(0, sphere.fn)
        self.assertFalse(sphere.fn4n)

        scad.run_super_scad(sphere, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialMetricSphere(self):
        """
        Test for an imperial sphere in metric units.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit_length_final=Unit.MM)
        sphere = ImperialSphere(radius=20.0, fa=12.0, fs=2.0, fn=0)
        scad.run_super_scad(sphere, path_actual)

        self.assertAlmostEqual(20.0 * 25.4, sphere.imperial_sphere.radius)
        self.assertAlmostEqual(40.0 * 25.4, sphere.imperial_sphere.diameter)
        self.assertAlmostEqual(12.0, sphere.imperial_sphere.fa)
        self.assertAlmostEqual(2.0 * 25.4, sphere.imperial_sphere.fs)
        self.assertEqual(0, sphere.imperial_sphere.fn)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialImperialSphere(self):
        """
        Test for an imperial sphere in imperial units.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit_length_final=Unit.INCH)
        sphere = ImperialSphere(radius=20.0, fa=12.0, fs=2.0, fn=0)
        scad.run_super_scad(sphere, path_actual)

        self.assertAlmostEqual(20.0, sphere.imperial_sphere.radius)
        self.assertAlmostEqual(40.0, sphere.imperial_sphere.diameter)
        self.assertAlmostEqual(12.0, sphere.imperial_sphere.fa)
        self.assertAlmostEqual(2.0, sphere.imperial_sphere.fs)
        self.assertEqual(0, sphere.imperial_sphere.fn)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
