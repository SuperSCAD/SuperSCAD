from ScadTestCase import ScadTestCase
from super_scad.boolean.Union import Union
from super_scad.d2.Square import Square
from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad.scad.Unit import Unit
from super_scad.transformation.Paint import Paint
from super_scad.type import Vector2
from super_scad.type.Color import Color
from test.d2.Square.ImperialUnitSquare import ImperialUnitSquare


class SquareTestCase(ScadTestCase):
    """
    Testcases for squares.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_plain_square(self):
        """
        Plain test for a square.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        square = Square(size=10)

        self.assertAlmostEqual(10.0, square.size)
        self.assertFalse(square.center)
        self.assertIsNone(square.convexity)

        scad.run_super_scad(square, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_centered_square(self):
        """
        Plain test for a centered square.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        square = Square(size=10, center=True)

        self.assertAlmostEqual(10.0, square.size)
        self.assertTrue(square.center)
        self.assertIsNone(square.convexity)

        scad.run_super_scad(square, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def xtest_imperial_metric_square(self):
        """
        Test for an imperial unit square in metric units.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        square = ImperialUnitSquare()
        scad.run_super_scad(square, path_actual)

        self.assertAlmostEqual(25.4, square.imperial_square.size)
        self.assertFalse(square.imperial_square.center)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_imperial_imperial_square(self):
        """
        Test for an imperial unit square in imperial units.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad(unit_length_final=Unit.INCH)
        square = ImperialUnitSquare()
        scad.run_super_scad(square, path_actual)

        self.assertAlmostEqual(1.0, square.imperial_square.size)
        self.assertFalse(square.imperial_square.center)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_angles(self):
        """
        Test the angles of square.
        """
        context = Context()
        expected_nodes = [Vector2(0.0, 0.0), Vector2(0.0, 10.0), Vector2(10.0, 10.0), Vector2(10.0, 0.0)]
        expected_inner_angles = [90.0, 90.0, 90.0, 90.0]
        expected_normal_angles = [45.0, 315.0, 225.0, 135.0]

        square = Square(size=10)
        self.assertTrue(square.is_clockwise(context))

        nodes = square.nodes
        inner_angles = square.inner_angles(context)
        normal_angles = square.normal_angles(context)
        for index in range(len(nodes)):
            self.assertAlmostEqual(expected_nodes[index].x, nodes[index].x)
            self.assertAlmostEqual(expected_nodes[index].y, nodes[index].y)
            self.assertAlmostEqual(expected_inner_angles[index], inner_angles[index])
            self.assertAlmostEqual(expected_normal_angles[index], normal_angles[index])

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_one_side(self):
        """
        Extend one side by extended by eps.
        """
        context = Context(eps=0.5)
        scad = Scad(context=context)

        square1 = Paint(color=Color('red'),
                        child=Square(size=10.0,
                                     extend_sides_by_eps={1}))
        square2 = Square(size=10.0)
        union = Union(children=[square1, square2])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_two_sides(self):
        """
        Extend two adjacent sides by extended by eps.
        """
        context = Context(eps=0.5)
        scad = Scad(context=context)

        square1 = Paint(color=Color('red'),
                        child=Square(size=10.0,
                                     center=True,
                                     extend_sides_by_eps={1, 2}))
        square2 = Square(size=10.0,
                         center=True)
        union = Union(children=[square1, square2])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_all_sides(self):
        """
        Extend all sides by extended by eps.
        """
        context = Context(eps=0.5)
        scad = Scad(context=context)

        square1 = Paint(color=Color('red'),
                        child=Square(size=10.0,
                                     extend_sides_by_eps=True))
        square2 = Square(size=10.0)
        union = Union(children=[square1, square2])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
