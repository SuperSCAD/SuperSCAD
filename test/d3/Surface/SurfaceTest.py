from d3.Surface.SurfaceDat import SurfaceDat
from ScadTestCase import ScadTestCase
from super_scad.d3.Surface import Surface


class SurfaceTest(ScadTestCase):
    """
    Test cases for Surface.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_surface(self):
        """
        The test case for Surface.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        example = SurfaceDat()
        scad.run_super_scad(example, path_actual)

        self.assertEqual('../../surface.dat', str(example.surface.path))
        self.assertEqual(5, example.surface.convexity)
        self.assertTrue(example.surface.center)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_file_not_exists(self):
        """
        Test for non-existent file.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        example = Surface(path='nonexistent.txt')

        self.assertRaises(FileNotFoundError, lambda: scad.run_super_scad(example, path_actual))

# ----------------------------------------------------------------------------------------------------------------------
