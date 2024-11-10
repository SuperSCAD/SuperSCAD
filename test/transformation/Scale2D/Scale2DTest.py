from ScadTestCase import ScadTestCase
from super_scad.boolean.Union import Union
from super_scad.d2.Square import Square
from super_scad.transformation.Scale2D import Scale2D
from super_scad.transformation.Translate2D import Translate2D
from super_scad.type.Vector2 import Vector2


class Scale2DTest(ScadTestCase):
    """
    Test cases for Scale2D.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_scale_with_vector(self):
        """
        Test scaling with a vector.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()

        square = Square(size=10.0)
        scale = Scale2D(factor=Vector2(x=0.5, y=1.0), child=square)

        self.assertAlmostEqual(scale.factor_x, 0.5)
        self.assertAlmostEqual(scale.factor_y, 1.0)
        self.assertAlmostEqual(scale.factor.x, 0.5)
        self.assertAlmostEqual(scale.factor.y, 1.0)

        union = Union(children=[square, Translate2D(x=15, child=scale)])

        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_scale_with1_factor(self):
        """
        Test scaling with one explicit factor and 1 implicit factor.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()

        square = Square(size=10.0)
        scale = Scale2D(factor_x=0.5, child=square)

        self.assertAlmostEqual(scale.factor_x, 0.5)
        self.assertAlmostEqual(scale.factor_y, 1.0)
        self.assertAlmostEqual(scale.factor.x, 0.5)
        self.assertAlmostEqual(scale.factor.y, 1.0)

        union = Union(children=[square, Translate2D(x=15, child=scale)])

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

        square = Square(size=10.0)
        scale = Scale2D(factor=2.0, child=square)

        self.assertAlmostEqual(scale.factor_x, 2.0)
        self.assertAlmostEqual(scale.factor_y, 2.0)
        self.assertAlmostEqual(scale.factor.x, 2.0)
        self.assertAlmostEqual(scale.factor.y, 2.0)

        union = Union(children=[square, Translate2D(x=15, child=scale)])

        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
