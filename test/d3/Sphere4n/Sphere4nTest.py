from d3.Sphere4n.ImperialSphere4n import ImperialSphere4n
from ScadTestCase import ScadTestCase
from super_scad.d3.Sphere4n import Sphere4n
from super_scad.Scad import Scad
from super_scad.Unit import Unit


class Sphere4nTestCase(ScadTestCase):
    """
    Testcases for sphere.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testSphereRadius(self):
        """
        Test for a sphere defined by a radius.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        sphere = Sphere4n(radius=2.0)

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

        scad = Scad(unit=Unit.MM)
        sphere = Sphere4n(diameter=2.0)

        self.assertAlmostEqual(1.0, sphere.radius)
        self.assertAlmostEqual(2.0, sphere.diameter)

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

        scad = Scad(unit=Unit.MM)
        sphere = ImperialSphere4n(radius=20.0, fa=12.0, fs=2.0, fn=0)
        scad.run_super_scad(sphere, path_actual)

        self.assertAlmostEqual(20.0 * 25.4, sphere.imperial_sphere.radius)
        self.assertAlmostEqual(40.0 * 25.4, sphere.imperial_sphere.diameter)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialImperialSphere(self):
        """
        Test for an imperial sphere in imperial units.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.INCH)
        sphere = ImperialSphere4n(radius=20.0, fa=12.0, fs=2.0, fn=0)
        scad.run_super_scad(sphere, path_actual)

        self.assertAlmostEqual(20.0, sphere.imperial_sphere.radius)
        self.assertAlmostEqual(40.0, sphere.imperial_sphere.diameter)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
