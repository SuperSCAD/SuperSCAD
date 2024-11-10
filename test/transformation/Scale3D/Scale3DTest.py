from ScadTestCase import ScadTestCase
from super_scad.boolean.Union import Union
from super_scad.d3.Cube import Cube
from super_scad.transformation.Scale3D import Scale3D
from super_scad.transformation.Translate3D import Translate3D
from super_scad.type.Vector3 import Vector3


class Scale3DTest(ScadTestCase):
    """
    Test cases for Scale3D.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_scale_with_vector(self):
        """
        Test scaling with a vector.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()

        cube = Cube(size=10.0)
        scale = Scale3D(factor=Vector3(x=0.5, y=1.0, z=2.0), child=cube)

        self.assertAlmostEqual(scale.factor_x, 0.5)
        self.assertAlmostEqual(scale.factor_y, 1.0)
        self.assertAlmostEqual(scale.factor_z, 2.0)
        self.assertAlmostEqual(scale.factor.x, 0.5)
        self.assertAlmostEqual(scale.factor.y, 1.0)
        self.assertAlmostEqual(scale.factor.z, 2.0)

        union = Union(children=[cube, Translate3D(x=15, child=scale)])

        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_scale_with2_factors(self):
        """
        Test scaling with two explicit factors and 1 implicit factor.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()

        cube = Cube(size=10.0)
        scale = Scale3D(factor_x=0.5, factor_z=2.0, child=cube)

        self.assertAlmostEqual(scale.factor_x, 0.5)
        self.assertAlmostEqual(scale.factor_y, 1.0)
        self.assertAlmostEqual(scale.factor_z, 2.0)
        self.assertAlmostEqual(scale.factor.x, 0.5)
        self.assertAlmostEqual(scale.factor.y, 1.0)
        self.assertAlmostEqual(scale.factor.z, 2.0)

        union = Union(children=[cube, Translate3D(x=15, child=scale)])

        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_scale_with_factor(self):
        """
        Test scaling with one factor for all axis.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()

        cube = Cube(size=10.0)
        scale = Scale3D(factor=2.0, child=cube)

        self.assertAlmostEqual(scale.factor_x, 2.0)
        self.assertAlmostEqual(scale.factor_y, 2.0)
        self.assertAlmostEqual(scale.factor_z, 2.0)
        self.assertAlmostEqual(scale.factor.x, 2.0)
        self.assertAlmostEqual(scale.factor.y, 2.0)
        self.assertAlmostEqual(scale.factor.z, 2.0)

        union = Union(children=[cube, Translate3D(x=15, child=scale)])

        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
