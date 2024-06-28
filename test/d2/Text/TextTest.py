import unittest
from pathlib import Path

from super_scad.d2.Text import Text
from super_scad.Scad import Scad
from super_scad.Unit import Unit


class TextTestCase(unittest.TestCase):
    """
    Testcases for texts.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testPlainText1(self):
        """
        Plain test for plain text.
        """
        path_actual = 'test/d2/Text/testPlainText1.actual.scad'
        path_expected = 'test/d2/Text/testPlainText1.expected.scad'

        scad = Scad(unit=Unit.MM)
        text = Text(text='SupeSCAD')

        self.assertIsNone(text.fn)

        scad.run_super_scad(text, Path(path_actual))

        actual = Path(path_actual).read_text()
        expected = Path(path_expected).read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPlainText2(self):
        """
        Plain test for plain text.
        """
        path_actual = 'test/d2/Text/testPlainText2.actual.scad'
        path_expected = 'test/d2/Text/testPlainText2.expected.scad'

        scad = Scad(unit=Unit.MM)
        text = Text(text='SupeSCAD', halign='center', valign='center', fn=10)

        self.assertEqual(10, text.fn)

        scad.run_super_scad(text, Path(path_actual))

        actual = Path(path_actual).read_text()
        expected = Path(path_expected).read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
