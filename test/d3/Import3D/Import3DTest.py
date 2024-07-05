from d3.Import3D.Slot3D import Slot3D
from ScadTestCase import ScadTestCase
from super_scad.d3.Import3D import Import3D
from super_scad.Scad import Scad
from super_scad.Unit import Unit


class Import3DTest(ScadTestCase):
    """
    Test cases for Import2D.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testImport3D(self):
        """
        The test case for Import3D.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        example = Slot3D()
        scad.run_super_scad(example, path_actual)

        self.assertEqual('../../slot.stl', str(example.import3d.path))
        self.assertEqual(10, example.import3d.convexity)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testFileNotExists(self):
        """
        Test for non-existent file.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        example = Import3D(path='nonexistent.stl')

        self.assertRaises(FileNotFoundError, lambda: scad.run_super_scad(example, path_actual))

# ----------------------------------------------------------------------------------------------------------------------
