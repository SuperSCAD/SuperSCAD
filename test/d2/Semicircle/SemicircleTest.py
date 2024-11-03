from d2.Semicircle.ImperialSemicircle import ImperialSemicircle
from ScadTestCase import ScadTestCase
from super_scad.d2.Semicircle import Semicircle
from super_scad.scad.Unit import Unit
from super_scad.type.Vector2 import Vector2


class SemicircleTestCase(ScadTestCase):
    """
    Testcases for Semicircle.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testSemicircleRadius(self):
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
    def testSemicircleDiameter(self):
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
    def testSemicircle4n(self):
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
    def testSemicircleAuxiliaryParameter(self):
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
    def testImperialMetricSemicircle(self):
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
    def testImperialImperialSemicircle(self):
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

    # ------------------------------------------------------------------------------------------------------------------
    def testSemicirclePosition(self):
        """
        Test the position of a semicircle.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        rectangle =  Semicircle(radius=10.0, position=Vector2(30.0, 20.0))
        scad.run_super_scad(rectangle, path_actual)

        self.assertAlmostEqual(10.0, rectangle.radius)
        self.assertEqual(Vector2(30.0, 20.0), rectangle.position)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
