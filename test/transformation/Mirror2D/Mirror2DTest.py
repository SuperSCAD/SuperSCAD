import math

from ScadTestCase import ScadTestCase
from super_scad.boolean.Union import Union
from super_scad.scad.Scad import Scad
from super_scad.scad.Unit import Unit
from super_scad.transformation.Mirror2D import Mirror2D
from super_scad.type.Point2 import Point2
from transformation.Mirror2D.Indicator import Indicator


class Mirror2DTest(ScadTestCase):
    """
    Test cases for Mirror2D.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testMirrorHorizontally(self):
        """
        Test mirror horizontally.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        original = Indicator()
        mirrored = Mirror2D(x=2.0, child=original)

        self.assertAlmostEqual(1.0, mirrored.vector.x)
        self.assertAlmostEqual(0.0, mirrored.vector.y)
        self.assertAlmostEqual(1.0, mirrored.vector.length)

        union = Union(children=[original, mirrored])
        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testMirrorVertically(self):
        """
        Test mirror vertically.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        original = Indicator()
        mirrored = Mirror2D(y=1.0, child=original)

        self.assertAlmostEqual(0.0, mirrored.vector.x)
        self.assertAlmostEqual(1.0, mirrored.vector.y)
        self.assertAlmostEqual(1.0, mirrored.vector.length)

        union = Union(children=[original, mirrored])
        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testMirrorByVector(self):
        """
        Test mirror by a vector.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        original = Indicator()
        mirrored = Mirror2D(vector=Point2(1.0, 1.0), child=original)

        self.assertAlmostEqual(math.sqrt(2.0) / 2.0, mirrored.vector.x)
        self.assertAlmostEqual(math.sqrt(2.0) / 2.0, mirrored.vector.y)
        self.assertAlmostEqual(1.0, mirrored.vector.length)

        union = Union(children=[original, mirrored])
        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
