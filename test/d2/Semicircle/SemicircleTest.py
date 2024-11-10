from d2.Semicircle.ImperialSemicircle import ImperialSemicircle
from ScadTestCase import ScadTestCase
from super_scad.d2.Semicircle import Semicircle
from super_scad.scad.Unit import Unit


class SemicircleTestCase(ScadTestCase):
    """
    Testcases for Semicircle.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_semicircle_radius(self):
        """
        Test for a semi_circle defined by a radius.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        semi_circle = Semicircle(radius=2.0)

        self.assertAlmostEqual(2.0, semi_circle.radius)
        self.assertAlmostEqual(4.0, semi_circle.diameter)

        scad.run_super_scad(semi_circle, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_semicircle_diameter(self):
        """
        Test for a semi_circle defined by a diameter.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        semi_circle = Semicircle(diameter=20.0)

        self.assertAlmostEqual(10.0, semi_circle.radius)
        self.assertAlmostEqual(20.0, semi_circle.diameter)
        self.assertIsNone(semi_circle.fa)
        self.assertIsNone(semi_circle.fs)
        self.assertIsNone(semi_circle.fn)

        scad.run_super_scad(semi_circle, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_semicircle4n(self):
        """
        Test for a semi_circle based on circle with a multiple of four vertices.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        semi_circle = Semicircle(radius=2.0, fn4n=True)

        self.assertAlmostEqual(2.0, semi_circle.radius)
        self.assertAlmostEqual(4.0, semi_circle.diameter)
        self.assertIsNone(semi_circle.fn)
        self.assertTrue(semi_circle.fn4n)

        scad.run_super_scad(semi_circle, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_semicircle_auxiliary_parameter(self):
        """
        Test auxiliary parameters.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        semi_circle = Semicircle(diameter=20.0, fa=12.0, fs=2.0, fn=0)

        self.assertIsNone(semi_circle.height)
        self.assertAlmostEqual(10.0, semi_circle.radius)
        self.assertAlmostEqual(20.0, semi_circle.diameter)
        self.assertAlmostEqual(12.0, semi_circle.fa)
        self.assertAlmostEqual(2.0, semi_circle.fs)
        self.assertEqual(0, semi_circle.fn)
        self.assertFalse(semi_circle.fn4n)

        scad.run_super_scad(semi_circle, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_imperial_metric_semicircle(self):
        """
        Test for an imperial 2D semi_circle in metric units.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        semi_circle = ImperialSemicircle(radius=20.0, fa=12.0, fs=2.0, fn=0)
        scad.run_super_scad(semi_circle, path_actual)

        self.assertIsNone(semi_circle.imperial_semicircle.height)
        self.assertAlmostEqual(20.0 * 25.4, semi_circle.imperial_semicircle.radius)
        self.assertAlmostEqual(40.0 * 25.4, semi_circle.imperial_semicircle.diameter)
        self.assertAlmostEqual(12.0, semi_circle.imperial_semicircle.fa)
        self.assertAlmostEqual(2.0 * 25.4, semi_circle.imperial_semicircle.fs)
        self.assertEqual(0, semi_circle.imperial_semicircle.fn)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_imperial_imperial_semicircle(self):
        """
        Test for an imperial 2D semi_circle in imperial units.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad(unit_length_final=Unit.INCH)
        semi_circle = ImperialSemicircle(radius=20.0, fa=12.0, fs=2.0, fn=0)
        scad.run_super_scad(semi_circle, path_actual)

        self.assertIsNone(semi_circle.imperial_semicircle.height)
        self.assertAlmostEqual(20.0, semi_circle.imperial_semicircle.radius)
        self.assertAlmostEqual(40.0, semi_circle.imperial_semicircle.diameter)
        self.assertAlmostEqual(12.0, semi_circle.imperial_semicircle.fa)
        self.assertAlmostEqual(2.0, semi_circle.imperial_semicircle.fs)
        self.assertEqual(0, semi_circle.imperial_semicircle.fn)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
