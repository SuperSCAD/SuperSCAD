from ScadTestCase import ScadTestCase
from super_scad.boolean.Union import Union
from super_scad.transformation.Flip2D import Flip2D
from transformation.Flip2D.Indicator import Indicator


class Flip2DTest(ScadTestCase):
    """
    Test cases for Flip2D.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testFlipX(self):
        """
        Test flip around x-axis.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        original = Indicator()
        flipped = Flip2D(flip_x=True, child=original)

        self.assertTrue(flipped.flip_x)
        self.assertTrue(flipped.vertical)
        self.assertFalse(flipped.flip_y)
        self.assertFalse(flipped.horizontal)

        union = Union(children=[original, flipped])
        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testFlipY(self):
        """
        Test flip around y-axis.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        original = Indicator()
        flipped = Flip2D(flip_y=True, child=original)

        self.assertFalse(flipped.flip_x)
        self.assertFalse(flipped.vertical)
        self.assertTrue(flipped.flip_y)
        self.assertTrue(flipped.horizontal)

        union = Union(children=[original, flipped])
        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testFlipZ(self):
        """
        Test flip around x and y-axis.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        original = Indicator()
        flipped = Flip2D(flip_x=True, flip_y=True, child=original)

        self.assertTrue(flipped.flip_x)
        self.assertTrue(flipped.vertical)
        self.assertTrue(flipped.flip_y)
        self.assertTrue(flipped.horizontal)

        union = Union(children=[original, flipped])
        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
