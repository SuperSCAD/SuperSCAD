from ScadTestCase import ScadTestCase
from super_scad.d3.Sphere import Sphere
from super_scad.scad.Unit import Unit
from super_scad.transformation.Translate3D import Translate3D
from super_scad.type.Vector3 import Vector3
from transformation.Translate3D.ImperialTranslate3D import ImperialTranslate3D


class Translate3DTest(ScadTestCase):
    """
    Test case for Translate3D.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_translate_by_vector(self):
        """
        Test translate given a vector.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()

        translate = Translate3D(vector=Vector3(10.0, 20.0, 30.0), child=Sphere(radius=10.0))

        self.assertAlmostEqual(10.0, translate.vector.x)
        self.assertAlmostEqual(20.0, translate.vector.y)
        self.assertAlmostEqual(30.0, translate.vector.z)
        self.assertAlmostEqual(10.0, translate.x)
        self.assertAlmostEqual(20.0, translate.y)
        self.assertAlmostEqual(30.0, translate.z)

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

        translate = Translate3D(x=10.0, child=Sphere(radius=10.0))
        self.assertAlmostEqual(10.0, translate.vector.x)
        self.assertAlmostEqual(0.0, translate.vector.y)
        self.assertAlmostEqual(0.0, translate.vector.z)
        self.assertAlmostEqual(10.0, translate.x)
        self.assertAlmostEqual(0.0, translate.y)
        self.assertAlmostEqual(0.0, translate.z)

        translate = Translate3D(y=10.0, child=Sphere(radius=10.0))
        self.assertAlmostEqual(0.0, translate.vector.x)
        self.assertAlmostEqual(10.0, translate.vector.y)
        self.assertAlmostEqual(0.0, translate.vector.z)
        self.assertAlmostEqual(0.0, translate.x)
        self.assertAlmostEqual(10.0, translate.y)
        self.assertAlmostEqual(0.0, translate.z)

        translate = Translate3D(z=10.0, child=Sphere(radius=10.0))
        self.assertAlmostEqual(0.0, translate.vector.x)
        self.assertAlmostEqual(0.0, translate.vector.y)
        self.assertAlmostEqual(10.0, translate.vector.z)
        self.assertAlmostEqual(0.0, translate.x)
        self.assertAlmostEqual(0.0, translate.y)
        self.assertAlmostEqual(10.0, translate.z)

        translate = Translate3D(x=10.0, y=20.0, z=30.0, child=Sphere(radius=10.0))
        self.assertAlmostEqual(10.0, translate.vector.x)
        self.assertAlmostEqual(20.0, translate.vector.y)
        self.assertAlmostEqual(30.0, translate.vector.z)
        self.assertAlmostEqual(10.0, translate.x)
        self.assertAlmostEqual(20.0, translate.y)
        self.assertAlmostEqual(30.0, translate.z)

        scad.run_super_scad(translate, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def xtest_imperial_metric_translation(self):
        """
        Test for an imperial translation in metric units.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()

        # Test given a vector.
        translate = ImperialTranslate3D(vector=Vector3(10.0, 20.0, 30.0), child=Sphere(radius=10.0))
        scad.run_super_scad(translate, path_actual)
        self.assertAlmostEqual(25.4 * 10.0, translate.imperial_translate.vector.x)
        self.assertAlmostEqual(25.4 * 20.0, translate.imperial_translate.vector.y)
        self.assertAlmostEqual(25.4 * 30.0, translate.imperial_translate.vector.z)
        self.assertAlmostEqual(25.4 * 10.0, translate.imperial_translate.x)
        self.assertAlmostEqual(25.4 * 20.0, translate.imperial_translate.y)
        self.assertAlmostEqual(25.4 * 30.0, translate.imperial_translate.z)

        # Test given a coordinates.
        translate = ImperialTranslate3D(x=10.0, y=20.0, z=30.0, child=Sphere(radius=10.0))
        scad.run_super_scad(translate, path_actual)
        self.assertAlmostEqual(25.4 * 10.0, translate.imperial_translate.vector.x)
        self.assertAlmostEqual(25.4 * 20.0, translate.imperial_translate.vector.y)
        self.assertAlmostEqual(25.4 * 30.0, translate.imperial_translate.vector.z)
        self.assertAlmostEqual(25.4 * 10.0, translate.imperial_translate.x)
        self.assertAlmostEqual(25.4 * 20.0, translate.imperial_translate.y)
        self.assertAlmostEqual(25.4 * 30.0, translate.imperial_translate.z)

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
        translate = ImperialTranslate3D(vector=Vector3(10.0, 20.0, 30.0), child=Sphere(radius=10.0))
        scad.run_super_scad(translate, path_actual)
        self.assertAlmostEqual(10.0, translate.imperial_translate.vector.x)
        self.assertAlmostEqual(20.0, translate.imperial_translate.vector.y)
        self.assertAlmostEqual(30.0, translate.imperial_translate.vector.z)
        self.assertAlmostEqual(10.0, translate.imperial_translate.x)
        self.assertAlmostEqual(20.0, translate.imperial_translate.y)
        self.assertAlmostEqual(30.0, translate.imperial_translate.z)

        # Test given a coordinates.
        translate = ImperialTranslate3D(x=10.0, y=20.0, z=30.0, child=Sphere(radius=10.0))
        scad.run_super_scad(translate, path_actual)
        self.assertAlmostEqual(10.0, translate.imperial_translate.vector.x)
        self.assertAlmostEqual(20.0, translate.imperial_translate.vector.y)
        self.assertAlmostEqual(30.0, translate.imperial_translate.vector.z)
        self.assertAlmostEqual(10.0, translate.imperial_translate.x)
        self.assertAlmostEqual(20.0, translate.imperial_translate.y)
        self.assertAlmostEqual(30.0, translate.imperial_translate.z)

        scad.run_super_scad(translate, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
