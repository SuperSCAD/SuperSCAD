from d2.Import2D.Slot2D import Slot2D
from ScadTestCase import ScadTestCase
from super_scad.Scad import Scad
from super_scad.Unit import Unit


class Import2DTest(ScadTestCase):
    """
    Test cases for Import2D.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testImport2D(self):
        """
        The test case for Import2D.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        example = Slot2D()
        scad.run_super_scad(example, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
