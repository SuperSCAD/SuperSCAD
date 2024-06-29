from d2.Semicircle4n.ImperialSemicircle4n import ImperialSemicircle4n
from ScadTestCase import ScadTestCase
from super_scad.d2.Semicircle4n import Semicircle4n
from super_scad.Scad import Scad
from super_scad.Unit import Unit


class Semicircle4nTestCase(ScadTestCase):
    """
    Testcases for Semicircle4n.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testSemicircle4nRadius(self):
        """
        Test for a semi_circle defined by a radius.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        semi_circle = Semicircle4n(radius=2.0)

        self.assertAlmostEqual(2.0, semi_circle.radius)
        self.assertAlmostEqual(4.0, semi_circle.diameter)

        scad.run_super_scad(semi_circle, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testSemicircle4nDiameter(self):
        """
        Test for a semi_circle defined by a diameter.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        semi_circle = Semicircle4n(diameter=20.0)

        self.assertAlmostEqual(10.0, semi_circle.radius)
        self.assertAlmostEqual(20.0, semi_circle.diameter)

        scad.run_super_scad(semi_circle, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialMetricSemicircle4n(self):
        """
        Test for an imperial semi_circle in metric units.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        semi_circle = ImperialSemicircle4n(radius=20.0)
        scad.run_super_scad(semi_circle, path_actual)

        self.assertAlmostEqual(20.0 * 25.4, semi_circle.imperial_semicircle4n.radius)
        self.assertAlmostEqual(40.0 * 25.4, semi_circle.imperial_semicircle4n.diameter)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialImperialSemicircle4n(self):
        """
        Test for an imperial semi_circle in imperial units.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.INCH)
        semi_circle = ImperialSemicircle4n(radius=20.0)
        scad.run_super_scad(semi_circle, path_actual)

        self.assertAlmostEqual(20.0, semi_circle.imperial_semicircle4n.radius)
        self.assertAlmostEqual(40.0, semi_circle.imperial_semicircle4n.diameter)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
