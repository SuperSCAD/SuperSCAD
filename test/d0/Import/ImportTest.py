from d0.Import.Slot2D import Slot2D
from d0.Import.Slot3D import Slot3D
from ScadTestCase import ScadTestCase
from super_scad.d0.Import import Import


class Import3DTest(ScadTestCase):
    """
    Test cases for Import2D.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_import2_d(self):
        """
        The test case for Import2D.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        example = Slot2D()
        scad.run_super_scad(example, path_actual)

        self.assertEqual('../../slot.dxf', str(example.import2d.path))
        self.assertEqual(10, example.import2d.convexity)
        self.assertEqual('Sketch', example.import2d.layer)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_import3_d(self):
        """
        The test case for Import3D.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        example = Slot3D()
        scad.run_super_scad(example, path_actual)

        self.assertEqual('../../slot.stl', str(example.import3d.path))
        self.assertEqual(10, example.import3d.convexity)

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
        example = Import(path='nonexistent.tx')

        self.assertRaises(FileNotFoundError, lambda: scad.run_super_scad(example, path_actual))

# ----------------------------------------------------------------------------------------------------------------------
