from d2.Circle.ImperialCircle import ImperialCircle
from ScadTestCase import ScadTestCase
from super_scad.d2.Circle import Circle
from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad.scad.Unit import Unit


class CircleTestCase(ScadTestCase):
    """
    Testcases for circle.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_radius(self):
        """
        Test for a circle defined by a radius.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        circle = Circle(radius=2.0)

        self.assertAlmostEqual(2.0, circle.radius)
        self.assertAlmostEqual(4.0, circle.diameter)
        self.assertFalse(circle.extend_by_eps_radius)

        scad.run_super_scad(circle, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_diameter(self):
        """
        Test for a circle defined by a diameter.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        circle = Circle(diameter=2.0)

        self.assertAlmostEqual(1.0, circle.radius)
        self.assertAlmostEqual(2.0, circle.diameter)
        self.assertIsNone(circle.fa)
        self.assertIsNone(circle.fs)
        self.assertIsNone(circle.fn)
        self.assertFalse(circle.extend_by_eps_radius)

        scad.run_super_scad(circle, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_auxiliary_parameter(self):
        """
        Test auxiliary parameters.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        circle = Circle(diameter=10.0, fa=12.0, fs=2.0, fn=0)

        self.assertAlmostEqual(5.0, circle.radius)
        self.assertAlmostEqual(10.0, circle.diameter)
        self.assertAlmostEqual(12.0, circle.fa)
        self.assertAlmostEqual(2.0, circle.fs)
        self.assertEqual(0, circle.fn)
        self.assertFalse(circle.fn4n)
        self.assertFalse(circle.extend_by_eps_radius)

        scad.run_super_scad(circle, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle4n(self):
        """
        Test a circle with a multiple of 4 vertices.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        circle = Circle(diameter=10.0, fn4n=True)

        self.assertAlmostEqual(5.0, circle.radius)
        self.assertAlmostEqual(10.0, circle.diameter)
        self.assertTrue(circle.fn4n)
        self.assertFalse(circle.extend_by_eps_radius)

        scad.run_super_scad(circle, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_imperial_metric_circle(self):
        """
        Test for an imperial circle in metric units.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        circle = ImperialCircle(radius=20.0, fa=12.0, fs=2.0, fn=0)
        scad.run_super_scad(circle, path_actual)

        # self.assertAlmostEqual(20.0 * 25.4, circle.imperial_circle.radius)
        # self.assertAlmostEqual(40.0 * 25.4, circle.imperial_circle.diameter)
        # self.assertAlmostEqual(12.0, circle.imperial_circle.fa)
        # self.assertAlmostEqual(2.0 * 25.4, circle.imperial_circle.fs)
        self.assertEqual(0, circle.imperial_circle.fn)
        self.assertFalse(circle.imperial_circle.extend_by_eps_radius)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_imperial_imperial_circle(self):
        """
        Test for an imperial circle in imperial units.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad(unit_length_final=Unit.INCH)
        circle = ImperialCircle(radius=20.0, fa=12.0, fs=2.0, fn=0)
        scad.run_super_scad(circle, path_actual)

        self.assertAlmostEqual(20.0, circle.imperial_circle.radius)
        self.assertAlmostEqual(40.0, circle.imperial_circle.diameter)
        self.assertAlmostEqual(12.0, circle.imperial_circle.fa)
        self.assertAlmostEqual(2.0, circle.imperial_circle.fs)
        self.assertEqual(0, circle.imperial_circle.fn)
        self.assertFalse(circle.imperial_circle.extend_by_eps_radius)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps(self):
        """
        Test extend radius by eps.
        """
        context = Context(eps=1.0)
        scad = Scad(context=context)

        circle = Circle(diameter=10.0, extend_by_eps_radius=True)

        self.assertAlmostEqual(5.0, circle.radius)
        self.assertAlmostEqual(10.0, circle.diameter)
        self.assertTrue(circle.extend_by_eps_radius)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(circle, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
