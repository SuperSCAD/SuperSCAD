from ScadTestCase import ScadTestCase
from super_scad.d3.Cube import Cube
from super_scad.scad.Scad import Scad
from super_scad.scad.Unit import Unit
from test.d3.Cube.ImperialUnitCube import ImperialUnitCube


class CubeTestCase(ScadTestCase):
    """
    Testcases for cubes.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testPlainCube(self):
        """
        Plain test for a cube.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        cube = Cube(size=10)

        self.assertAlmostEqual(10.0, cube.size)
        self.assertFalse(cube.center)

        scad.run_super_scad(cube, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testCenteredCube(self):
        """
        Plain test for a centered cube.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        cube = Cube(size=10, center=True)

        self.assertAlmostEqual(10.0, cube.size)
        self.assertTrue(cube.center)

        scad.run_super_scad(cube, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialMetricCube(self):
        """
        Test for an imperial unit cube in metric units.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        cube = ImperialUnitCube()
        scad.run_super_scad(cube, path_actual)

        self.assertAlmostEqual(25.4, cube.imperial_cube.size)
        self.assertFalse(cube.imperial_cube.center)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialImperialCube(self):
        """
        Test for an imperial unit cube in imperial units.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad(unit_length_final=Unit.INCH)
        cube = ImperialUnitCube()
        scad.run_super_scad(cube, path_actual)

        self.assertAlmostEqual(1.0, cube.imperial_cube.size)
        self.assertFalse(cube.imperial_cube.center)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
