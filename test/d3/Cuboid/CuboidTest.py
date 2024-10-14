from ScadTestCase import ScadTestCase
from super_scad.d3.Cuboid import Cuboid
from super_scad.scad.Scad import Scad
from super_scad.scad.Unit import Unit
from super_scad.type.Size3 import Size3
from test.d3.Cuboid.ImperialUnitCuboid import ImperialUnitCuboid


class CuboidTestCase(ScadTestCase):
    """
    Testcases for cuboids.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testCuboidBySize(self):
        """
        Test for a cuboid defined by size.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        cuboid = Cuboid(size=Size3(30, 20, 10))

        self.assertAlmostEqual(30.0, cuboid.width)
        self.assertAlmostEqual(20.0, cuboid.depth)
        self.assertAlmostEqual(10.0, cuboid.height)
        self.assertAlmostEqual(30.0, cuboid.size.width)
        self.assertAlmostEqual(20.0, cuboid.size.depth)
        self.assertAlmostEqual(10.0, cuboid.size.height)
        self.assertFalse(cuboid.center)

        scad.run_super_scad(cuboid, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testCuboidByWidthAndDepth(self):
        """
        Test for a cuboid defined by width and depth.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        cuboid = Cuboid(size=Size3(30, 20, 10), center=True)

        self.assertAlmostEqual(30.0, cuboid.width)
        self.assertAlmostEqual(20.0, cuboid.depth)
        self.assertAlmostEqual(10.0, cuboid.height)
        self.assertAlmostEqual(30.0, cuboid.size.width)
        self.assertAlmostEqual(20.0, cuboid.size.depth)
        self.assertAlmostEqual(10.0, cuboid.size.height)
        self.assertTrue(cuboid.center)

        scad.run_super_scad(cuboid, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialMetricCuboid(self):
        """
        Test for an imperial unit cuboid in metric units.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        cuboid = ImperialUnitCuboid()
        scad.run_super_scad(cuboid, path_actual)

        self.assertAlmostEqual(76.2, cuboid.imperial_cuboid.width)
        self.assertAlmostEqual(50.8, cuboid.imperial_cuboid.depth)
        self.assertAlmostEqual(25.4, cuboid.imperial_cuboid.height)
        self.assertAlmostEqual(76.2, cuboid.imperial_cuboid.size.width)
        self.assertAlmostEqual(50.8, cuboid.imperial_cuboid.size.depth)
        self.assertAlmostEqual(25.4, cuboid.imperial_cuboid.size.height)
        self.assertFalse(cuboid.imperial_cuboid.center)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialImperialCuboid(self):
        """
        Test for an imperial unit cuboid in imperial units.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad(unit_length_final=Unit.INCH)
        cuboid = ImperialUnitCuboid()
        scad.run_super_scad(cuboid, path_actual)

        self.assertAlmostEqual(3.0, cuboid.imperial_cuboid.width)
        self.assertAlmostEqual(2.0, cuboid.imperial_cuboid.depth)
        self.assertAlmostEqual(1.0, cuboid.imperial_cuboid.height)
        self.assertAlmostEqual(3.0, cuboid.imperial_cuboid.size.width)
        self.assertAlmostEqual(2.0, cuboid.imperial_cuboid.size.depth)
        self.assertAlmostEqual(1.0, cuboid.imperial_cuboid.size.height)
        self.assertFalse(cuboid.imperial_cuboid.center)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
