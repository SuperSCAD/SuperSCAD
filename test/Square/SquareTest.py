import unittest
from pathlib import Path

from super_scad.d2.Square import Square
from super_scad.Scad import Scad
from super_scad.Unit import Unit
from test.Square.ImperialUnitSquare import ImperialUnitSquare


class StratumTestCase(unittest.TestCase):
    """
    Testcases for squares.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def testPlainSquare(self):
        """
        Plain test for a square.
        """
        path_actual = 'test/Square/testPlainSquare.actual.scad'
        path_expected = 'test/Square/testPlainSquare.expected.scad'

        scad = Scad(unit=Unit.MM)
        scad.run_super_scad(Square(size=10), Path(path_actual))

        actual = Path(path_actual).read_text()
        expected = Path(path_expected).read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testCenteredSquare(self):
        """
        Plain test for a centered square.
        """
        path_actual = 'test/Square/testCenteredSquare.actual.scad'
        path_expected = 'test/Square/testCenteredSquare.expected.scad'

        scad = Scad(unit=Unit.MM)
        scad.run_super_scad(Square(size=10, center=True), Path(path_actual))

        actual = Path(path_actual).read_text()
        expected = Path(path_expected).read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialMetricSquare(self):
        """
        Test for an imperial unit square in metric units.
        """
        path_actual = 'test/Square/testImperialMetricSquare.actual.scad'
        path_expected = 'test/Square/testImperialMetricSquare.expected.scad'

        scad = Scad(unit=Unit.MM)
        scad.run_super_scad(ImperialUnitSquare(), Path(path_actual))

        actual = Path(path_actual).read_text()
        expected = Path(path_expected).read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialImperialSquare(self):
        """
        Test for an imperial unit square in imperial units.
        """
        path_actual = 'test/Square/testImperialImperialSquare.actual.scad'
        path_expected = 'test/Square/testImperialImperialSquare.expected.scad'

        scad = Scad(unit=Unit.INCH)
        scad.run_super_scad(ImperialUnitSquare(), Path(path_actual))

        actual = Path(path_actual).read_text()
        expected = Path(path_expected).read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
