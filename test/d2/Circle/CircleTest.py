from d2.Circle.ImperialCircle import ImperialCircle
from ScadTestCase import ScadTestCase
from super_scad.d2.Circle import Circle
from super_scad.Scad import Scad
from super_scad.Unit import Unit


class CircleTestCase(ScadTestCase):
    """
    Testcases for circle.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testCircleRadius(self):
        """
        Test for a circle defined by a radius.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        circle = Circle(radius=2.0)

        self.assertAlmostEqual(2.0, circle.radius)
        self.assertAlmostEqual(4.0, circle.diameter)

        scad.run_super_scad(circle, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testCircleDiameter(self):
        """
        Test for a circle defined by a diameter.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        circle = Circle(diameter=2.0)

        self.assertAlmostEqual(1.0, circle.radius)
        self.assertAlmostEqual(2.0, circle.diameter)
        self.assertIsNone(circle.fa)
        self.assertIsNone(circle.fs)
        self.assertIsNone(circle.fn)

        scad.run_super_scad(circle, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testCircleAuxiliaryParameter(self):
        """
        Test auxiliary parameters.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        circle = Circle(diameter=10.0, fa=12.0, fs=2.0, fn=0)

        self.assertAlmostEqual(5.0, circle.radius)
        self.assertAlmostEqual(10.0, circle.diameter)
        self.assertAlmostEqual(12.0, circle.fa)
        self.assertAlmostEqual(2.0, circle.fs)
        self.assertEqual(0, circle.fn)

        scad.run_super_scad(circle, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialMetricCircle(self):
        """
        Test for an imperial circle in metric units.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        circle = ImperialCircle(radius=20.0, fa=12.0, fs=2.0, fn=0)
        scad.run_super_scad(circle, path_actual)

        self.assertAlmostEqual(20.0 * 25.4, circle.imperial_circle.radius)
        self.assertAlmostEqual(40.0 * 25.4, circle.imperial_circle.diameter)
        self.assertAlmostEqual(12.0, circle.imperial_circle.fa)
        self.assertAlmostEqual(2.0 * 25.4, circle.imperial_circle.fs)
        self.assertEqual(0, circle.imperial_circle.fn)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialImperialCircle(self):
        """
        Test for an imperial circle in imperial units.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.INCH)
        circle = ImperialCircle(radius=20.0, fa=12.0, fs=2.0, fn=0)
        scad.run_super_scad(circle, path_actual)

        self.assertAlmostEqual(20.0, circle.imperial_circle.radius)
        self.assertAlmostEqual(40.0, circle.imperial_circle.diameter)
        self.assertAlmostEqual(12.0, circle.imperial_circle.fa)
        self.assertAlmostEqual(2.0, circle.imperial_circle.fs)
        self.assertEqual(0, circle.imperial_circle.fn)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
