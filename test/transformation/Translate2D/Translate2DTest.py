from ScadTestCase import ScadTestCase
from super_scad.d2.Circle import Circle
from super_scad.scad.Unit import Unit
from super_scad.transformation.Translate2D import Translate2D
from super_scad.type.Vector2 import Vector2
from transformation.Translate2D.ImperialTranslate2D import ImperialTranslate2D


class Translate2DTest(ScadTestCase):
    """
    Test case for Translate2D.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_translate_by_vector(self):
        """
        Test translate given a vector.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()

        translate = Translate2D(vector=Vector2(10.0, 20.0), child=Circle(radius=10.0))

        self.assertAlmostEqual(10.0, translate.vector.x)
        self.assertAlmostEqual(20.0, translate.vector.y)
        self.assertAlmostEqual(10.0, translate.x)
        self.assertAlmostEqual(20.0, translate.y)

        scad.run_super_scad(translate, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_translate_by_coordinates(self):
        """
        Test translate given coordinates.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()

        translate = Translate2D(x=10.0, child=Circle(radius=10.0))
        self.assertAlmostEqual(10.0, translate.vector.x)
        self.assertAlmostEqual(0.0, translate.vector.y)
        self.assertAlmostEqual(10.0, translate.x)
        self.assertAlmostEqual(0.0, translate.y)

        translate = Translate2D(y=10.0, child=Circle(radius=10.0))
        self.assertAlmostEqual(0.0, translate.vector.x)
        self.assertAlmostEqual(10.0, translate.vector.y)
        self.assertAlmostEqual(0.0, translate.x)
        self.assertAlmostEqual(10.0, translate.y)

        translate = Translate2D(x=10.0, y=20.0, child=Circle(radius=10.0))
        self.assertAlmostEqual(10.0, translate.vector.x)
        self.assertAlmostEqual(20.0, translate.vector.y)
        self.assertAlmostEqual(10.0, translate.x)
        self.assertAlmostEqual(20.0, translate.y)

        scad.run_super_scad(translate, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_imperial_metric_translation(self):
        """
        Test for an imperial translation in metric units.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()

        # Test given a vector.
        translate = ImperialTranslate2D(vector=Vector2(10.0, 20.0), child=Circle(radius=10.0))
        scad.run_super_scad(translate, path_actual)
        self.assertAlmostEqual(25.4 * 10.0, translate.imperial_translate.vector.x)
        self.assertAlmostEqual(25.4 * 20.0, translate.imperial_translate.vector.y)
        self.assertAlmostEqual(25.4 * 10.0, translate.imperial_translate.x)
        self.assertAlmostEqual(25.4 * 20.0, translate.imperial_translate.y)

        # Test given a coordinates.
        translate = ImperialTranslate2D(x=10.0, y=20.0, child=Circle(radius=10.0))
        scad.run_super_scad(translate, path_actual)
        self.assertAlmostEqual(25.4 * 10.0, translate.imperial_translate.vector.x)
        self.assertAlmostEqual(25.4 * 20.0, translate.imperial_translate.vector.y)
        self.assertAlmostEqual(25.4 * 10.0, translate.imperial_translate.x)
        self.assertAlmostEqual(25.4 * 20.0, translate.imperial_translate.y)

        scad.run_super_scad(translate, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_imperial_imperial_translation(self):
        """
        Test for an imperial translation in imperial units.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad(unit_length_final=Unit.INCH)

        # Test given a vector.
        translate = ImperialTranslate2D(vector=Vector2(10.0, 20.0), child=Circle(radius=10.0))
        scad.run_super_scad(translate, path_actual)
        self.assertAlmostEqual(10.0, translate.imperial_translate.vector.x)
        self.assertAlmostEqual(20.0, translate.imperial_translate.vector.y)
        self.assertAlmostEqual(10.0, translate.imperial_translate.x)
        self.assertAlmostEqual(20.0, translate.imperial_translate.y)

        # Test given a coordinates.
        translate = ImperialTranslate2D(x=10.0, y=20.0, child=Circle(radius=10.0))
        scad.run_super_scad(translate, path_actual)
        self.assertAlmostEqual(10.0, translate.imperial_translate.vector.x)
        self.assertAlmostEqual(20.0, translate.imperial_translate.vector.y)
        self.assertAlmostEqual(10.0, translate.imperial_translate.x)
        self.assertAlmostEqual(20.0, translate.imperial_translate.y)

        scad.run_super_scad(translate, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
