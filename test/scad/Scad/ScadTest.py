import math

from ScadTestCase import ScadTestCase
from super_scad.d2.Circle import Circle
from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad


class ScadTest(ScadTestCase):
    """
    Text cases for Scad.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testNonDefaultFa(self):
        """
        Test non default value for $fa.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fa=2.0))

        scad.run_super_scad(Circle(diameter=10.0), path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testNonDefaultFs(self):
        """
        Test non default value for $fs.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fs=math.pi))

        scad.run_super_scad(Circle(diameter=10.0), path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testNonDefaultFn(self):
        """
        Test non default value for $fn.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=359))

        scad.run_super_scad(Circle(diameter=10.0), path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testNonDefaultFaFsFn(self):
        """
        Test non default value for $fa, $fs, and $fn.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fa=2, fs=0.1, fn=60))

        scad.run_super_scad(Circle(diameter=10.0), path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
