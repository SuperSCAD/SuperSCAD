from ScadTestCase import ScadTestCase
from super_scad.d2.Text import Text


class TextTestCase(ScadTestCase):
    """
    Testcases for texts.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_plain_text1(self):
        """
        Plain test for plain text.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        text = Text(text='SuperSCAD')

        self.assertEqual('SuperSCAD', text.text)
        self.assertEqual(10, text.size)
        self.assertIsNone(text.font)
        self.assertEqual('left', text.halign)
        self.assertEqual('baseline', text.valign)
        self.assertEqual(1.0, text.spacing)
        self.assertEqual('ltr', text.direction)
        self.assertEqual('en', text.language)
        self.assertEqual('latin', text.script)
        self.assertIsNone(text.fn)

        scad.run_super_scad(text, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_plain_text2(self):
        """
        Plain test for plain text.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        text = Text(text='SuperSCAD', halign='center', valign='center', fn=10)

        self.assertEqual('SuperSCAD', text.text)
        self.assertEqual(10, text.size)
        self.assertIsNone(text.font)
        self.assertEqual('center', text.halign)
        self.assertEqual('center', text.valign)
        self.assertEqual(1.0, text.spacing)
        self.assertEqual('ltr', text.direction)
        self.assertEqual('en', text.language)
        self.assertEqual('latin', text.script)
        self.assertEqual(10, text.fn)

        scad.run_super_scad(text, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
