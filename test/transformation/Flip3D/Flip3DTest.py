from ScadTestCase import ScadTestCase
from super_scad.boolean.Union import Union
from super_scad.Scad import Scad
from super_scad.transformation.Flip3D import Flip3D
from super_scad.transformation.Translate3D import Translate3D
from super_scad.Unit import Unit
from transformation.Flip3D.Dice import Dice


class Flip3DTest(ScadTestCase):
    """
    Test cases for Flip3D.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testFlipX(self):
        """
        Test flip around x-axis.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        dice = Dice(size=30.0)
        flip_dice = Flip3D(flip_x=True, child=Dice(size=30.0))
        union = Union(children=[Translate3D(x=-20, child=dice), Translate3D(x=20, child=flip_dice)])

        self.assertTrue(flip_dice.flip_x)
        self.assertTrue(flip_dice.vertical)
        self.assertFalse(flip_dice.flip_y)
        self.assertFalse(flip_dice.horizontal)

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

        scad = Scad(unit=Unit.MM)
        dice = Dice(size=30.0)
        flip_dice = Flip3D(flip_y=True, child=Dice(size=30.0))
        union = Union(children=[Translate3D(x=-20, child=dice), Translate3D(x=20, child=flip_dice)])

        self.assertFalse(flip_dice.flip_x)
        self.assertFalse(flip_dice.vertical)
        self.assertTrue(flip_dice.flip_y)
        self.assertTrue(flip_dice.horizontal)

        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testFlipZ1(self):
        """
        Test flip around z-axis.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        dice = Dice(size=30.0)
        flip_dice = Flip3D(flip_z=True, child=Dice(size=30.0))
        union = Union(children=[Translate3D(x=-20, child=dice), Translate3D(x=20, child=flip_dice)])

        self.assertTrue(flip_dice.flip_x)
        self.assertTrue(flip_dice.vertical)
        self.assertTrue(flip_dice.flip_y)
        self.assertTrue(flip_dice.horizontal)

        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testFlipZ2(self):
        """
        Test flip around z-axis.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        dice = Dice(size=30.0)
        flip_dice = Flip3D(flip_x=True, flip_y=True, child=Dice(size=30.0))
        union = Union(children=[Translate3D(x=-20, child=dice), Translate3D(x=20, child=flip_dice)])

        self.assertTrue(flip_dice.flip_x)
        self.assertTrue(flip_dice.vertical)
        self.assertTrue(flip_dice.flip_y)
        self.assertTrue(flip_dice.horizontal)

        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
