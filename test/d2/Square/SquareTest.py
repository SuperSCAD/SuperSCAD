from ScadTestCase import ScadTestCase
from super_scad.d2.Square import Square
from super_scad.scad.Scad import Scad
from super_scad.scad.Unit import Unit
from test.d2.Square.ImperialUnitSquare import ImperialUnitSquare


class SquareTestCase(ScadTestCase):
    """
    Testcases for squares.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testPlainSquare(self):
        """
        Plain test for a square.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        square = Square(size=10)

        self.assertAlmostEqual(10.0, square.size)
        self.assertFalse(square.center)

        scad.run_super_scad(square, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testCenteredSquare(self):
        """
        Plain test for a centered square.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        square = Square(size=10, center=True)

        self.assertAlmostEqual(10.0, square.size)
        self.assertTrue(square.center)

        scad.run_super_scad(square, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialMetricSquare(self):
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
    def testImperialImperialSquare(self):
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

# ----------------------------------------------------------------------------------------------------------------------
