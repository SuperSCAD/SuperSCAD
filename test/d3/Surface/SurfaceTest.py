from d3.Surface.SurfaceDat import SurfaceDat
from ScadTestCase import ScadTestCase
from super_scad.Scad import Scad
from super_scad.Unit import Unit


class SurfaceTest(ScadTestCase):
    """
    Test cases for Surface.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testSurface(self):
        """
        The test case for Surface.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        example = SurfaceDat()
        scad.run_super_scad(example, path_actual)

        self.assertEqual('../../surface.dat', str(example.surface.path))
        self.assertEqual(5, example.surface.convexity)
        self.assertTrue(example.surface.center)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
