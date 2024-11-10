import math

from ScadTestCase import ScadTestCase
from super_scad.boolean.Union import Union
from super_scad.transformation.Mirror3D import Mirror3D
from super_scad.type.Vector3 import Vector3
from transformation.Mirror3D.Indicator import Indicator


class Mirror3DTest(ScadTestCase):
    """
    Test cases for Mirror3D.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_mirror_horizontally(self):
        """
        Test mirror horizontally.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        original = Indicator()
        mirrored = Mirror3D(x=1.0, child=original)

        self.assertAlmostEqual(1.0, mirrored.vector.x)
        self.assertAlmostEqual(0.0, mirrored.vector.y)
        self.assertAlmostEqual(1.0, mirrored.vector.length)

        union = Union(children=[original, mirrored])
        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_mirror_vertically(self):
        """
        Test mirror vertically.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        original = Indicator()
        mirrored = Mirror3D(y=1.0, child=original)

        self.assertAlmostEqual(0.0, mirrored.vector.x)
        self.assertAlmostEqual(1.0, mirrored.vector.y)
        self.assertAlmostEqual(1.0, mirrored.vector.length)

        union = Union(children=[original, mirrored])
        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_mirror_horizontally_and_vertically(self):
        """
        Test mirror horizontally and vertically.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        original = Indicator()
        mirrored = Mirror3D(z=1.0, child=original)

        self.assertAlmostEqual(0.0, mirrored.vector.x)
        self.assertAlmostEqual(0.0, mirrored.vector.y)
        self.assertAlmostEqual(1.0, mirrored.vector.z)
        self.assertAlmostEqual(1.0, mirrored.vector.length)

        union = Union(children=[original, mirrored])
        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_mirror_by_vector(self):
        """
        Test mirror by a vector.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        original = Indicator()
        mirrored = Mirror3D(vector=Vector3(1.0, 1.0, 1.0), child=original)

        self.assertAlmostEqual(math.sqrt(3.0) / 3.0, mirrored.vector.x)
        self.assertAlmostEqual(math.sqrt(3.0) / 3.0, mirrored.vector.y)
        self.assertAlmostEqual(math.sqrt(3.0) / 3.0, mirrored.vector.z)
        self.assertAlmostEqual(1.0, mirrored.vector.length)

        union = Union(children=[original, mirrored])
        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
