from d3.LinearExtrude.ImperialUnitCube import ImperialUnitCube
from ScadTestCase import ScadTestCase
from super_scad.d2.Circle import Circle
from super_scad.d2.Polygon import Polygon
from super_scad.d3.LinearExtrude import LinearExtrude
from super_scad.Scad import Scad
from super_scad.transformation.Translate2D import Translate2D
from super_scad.type.Point2 import Point2
from super_scad.Unit import Unit


class LinearExtrudeTest(ScadTestCase):
    """
    Test cases for LinearExtrude.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testSample1(self):
        """
        Test sample 1 from the OpenSCAD cheatsheet.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        extrude = LinearExtrude(height=10.0,
                                center=True,
                                convexity=10,
                                child=Translate2D(x=2.0, child=Circle(radius=1)))

        self.assertAlmostEqual(10.0, extrude.height)
        self.assertTrue(extrude.center)
        self.assertEqual(10, extrude.convexity)
        self.assertAlmostEqual(0.0, extrude.twist)
        self.assertAlmostEqual(1.0, extrude.scale)
        self.assertIsNone(extrude.slices)
        self.assertIsNone(extrude.segments)
        self.assertIsNone(extrude.fa)
        self.assertIsNone(extrude.fs)
        self.assertIsNone(extrude.fn)

        scad.run_super_scad(extrude, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testSample2(self):
        """
        Test sample 2 from the OpenSCAD cheatsheet.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        extrude = LinearExtrude(height=10.0,
                                center=True,
                                convexity=10,
                                twist=-100.0,
                                child=Translate2D(x=2.0, child=Circle(radius=1)))

        self.assertAlmostEqual(10.0, extrude.height)
        self.assertTrue(extrude.center)
        self.assertEqual(10, extrude.convexity)
        self.assertAlmostEqual(-100.0, extrude.twist)
        self.assertAlmostEqual(1.0, extrude.scale)
        self.assertIsNone(extrude.slices)
        self.assertIsNone(extrude.segments)
        self.assertIsNone(extrude.fa)
        self.assertIsNone(extrude.fs)
        self.assertIsNone(extrude.fn)

        scad.run_super_scad(extrude, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testSample3(self):
        """
        Test sample 3 from the OpenSCAD cheatsheet.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        extrude = LinearExtrude(height=10.0,
                                center=True,
                                convexity=10,
                                twist=100.0,
                                child=Translate2D(x=2.0, child=Circle(radius=1)))

        self.assertAlmostEqual(10.0, extrude.height)
        self.assertTrue(extrude.center)
        self.assertEqual(10, extrude.convexity)
        self.assertAlmostEqual(100.0, extrude.twist)
        self.assertAlmostEqual(1.0, extrude.scale)
        self.assertIsNone(extrude.slices)
        self.assertIsNone(extrude.segments)
        self.assertIsNone(extrude.fa)
        self.assertIsNone(extrude.fs)
        self.assertIsNone(extrude.fn)

        scad.run_super_scad(extrude, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testSample4(self):
        """
        Test sample 4 from the OpenSCAD cheatsheet.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        extrude = LinearExtrude(height=10.0,
                                center=True,
                                convexity=10,
                                twist=-500.0,
                                child=Translate2D(x=2.0, child=Circle(radius=1)))

        self.assertAlmostEqual(10.0, extrude.height)
        self.assertTrue(extrude.center)
        self.assertEqual(10, extrude.convexity)
        self.assertAlmostEqual(-500.0, extrude.twist)
        self.assertAlmostEqual(1.0, extrude.scale)
        self.assertIsNone(extrude.slices)
        self.assertIsNone(extrude.segments)
        self.assertIsNone(extrude.fa)
        self.assertIsNone(extrude.fs)
        self.assertIsNone(extrude.fn)

        scad.run_super_scad(extrude, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testSample5(self):
        """
        Test sample 5 from the OpenSCAD cheatsheet.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        extrude = LinearExtrude(height=10.0,
                                convexity=10,
                                twist=-500.0,
                                child=Translate2D(x=2.0, child=Circle(radius=1)))

        self.assertAlmostEqual(10.0, extrude.height)
        self.assertFalse(extrude.center)
        self.assertEqual(10, extrude.convexity)
        self.assertAlmostEqual(-500.0, extrude.twist)
        self.assertAlmostEqual(1.0, extrude.scale)
        self.assertIsNone(extrude.slices)
        self.assertIsNone(extrude.segments)
        self.assertIsNone(extrude.fa)
        self.assertIsNone(extrude.fs)
        self.assertIsNone(extrude.fn)

        scad.run_super_scad(extrude, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testSample6(self):
        """
        Test sample 6 from the OpenSCAD cheatsheet.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        extrude = LinearExtrude(height=10.0,
                                convexity=10,
                                twist=360.0,
                                slices=100,
                                child=Translate2D(x=2.0, child=Circle(radius=1)))

        self.assertAlmostEqual(10.0, extrude.height)
        self.assertFalse(extrude.center)
        self.assertEqual(10, extrude.convexity)
        self.assertAlmostEqual(360.0, extrude.twist)
        self.assertAlmostEqual(1.0, extrude.scale)
        self.assertEqual(100, extrude.slices)
        self.assertIsNone(extrude.segments)
        self.assertIsNone(extrude.fa)
        self.assertIsNone(extrude.fs)
        self.assertIsNone(extrude.fn)

        scad.run_super_scad(extrude, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testSample7(self):
        """
        Test sample 7 from the OpenSCAD cheatsheet.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        extrude = LinearExtrude(height=10.0,
                                convexity=10,
                                twist=-360.0,
                                fn=100,
                                child=Translate2D(x=2.0, child=Circle(radius=1)))

        self.assertAlmostEqual(10.0, extrude.height)
        self.assertFalse(extrude.center)
        self.assertEqual(10, extrude.convexity)
        self.assertAlmostEqual(-360.0, extrude.twist)
        self.assertAlmostEqual(1.0, extrude.scale)
        self.assertIsNone(extrude.slices)
        self.assertIsNone(extrude.segments)
        self.assertIsNone(extrude.fa)
        self.assertIsNone(extrude.fs)
        self.assertEqual(100, extrude.fn)

        scad.run_super_scad(extrude, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testSample8(self):
        """
        Test sample 8 from the OpenSCAD cheatsheet.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        extrude = LinearExtrude(height=10.0,
                                convexity=10,
                                scale=3.0,
                                child=Translate2D(x=2.0, child=Circle(radius=1)))

        self.assertAlmostEqual(10.0, extrude.height)
        self.assertFalse(extrude.center)
        self.assertEqual(10, extrude.convexity)
        self.assertAlmostEqual(0.0, extrude.twist)
        self.assertAlmostEqual(3.0, extrude.scale)
        self.assertIsNone(extrude.slices)
        self.assertIsNone(extrude.segments)
        self.assertIsNone(extrude.fa)
        self.assertIsNone(extrude.fs)
        self.assertIsNone(extrude.fn)

        scad.run_super_scad(extrude, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testSample9(self):
        """
        Test sample 9 from the OpenSCAD cheatsheet.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        polygon = [Point2(0.0, 0.0), Point2(20.0, 10.0), Point2(20.0, -10.0)]
        extrude = LinearExtrude(height=10.0,
                                center=True,
                                convexity=10,
                                scale=Point2(1, 5),
                                slices=20,
                                fn=100,
                                child=Translate2D(x=2.0, child=Circle(radius=1)))

        self.assertAlmostEqual(10.0, extrude.height)
        self.assertTrue(extrude.center)
        self.assertEqual(10, extrude.convexity)
        self.assertAlmostEqual(0.0, extrude.twist)
        self.assertAlmostEqual(1.0, extrude.scale.x)
        self.assertAlmostEqual(5.0, extrude.scale.y)
        self.assertEqual(20, extrude.slices)
        self.assertIsNone(extrude.segments)
        self.assertIsNone(extrude.fa)
        self.assertIsNone(extrude.fs)
        self.assertEqual(100, extrude.fn)

        scad.run_super_scad(extrude, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialMetricLinearExtrude(self):
        """
        Test for an extrude imperial unit cube in metric units.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        extrude = ImperialUnitCube()

        scad.run_super_scad(extrude, path_actual)

        self.assertAlmostEqual(25.4, extrude.imperial_unit_cube.height)
        self.assertFalse(extrude.imperial_unit_cube.center)
        self.assertIsNone(extrude.imperial_unit_cube.convexity)
        self.assertAlmostEqual(0.0, extrude.imperial_unit_cube.twist)
        self.assertAlmostEqual(1.0, extrude.imperial_unit_cube.scale)
        self.assertIsNone(extrude.imperial_unit_cube.slices)
        self.assertIsNone(extrude.imperial_unit_cube.segments)
        self.assertIsNone(extrude.imperial_unit_cube.fa)
        self.assertAlmostEqual(0.254, extrude.imperial_unit_cube.fs)
        self.assertIsNone(extrude.imperial_unit_cube.fn)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialImperialLinearExtrude(self):
        """
        Test for an extruded imperial unit cube in imperial units.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.INCH)
        extrude = ImperialUnitCube()

        scad.run_super_scad(extrude, path_actual)

        self.assertAlmostEqual(1.0, extrude.imperial_unit_cube.height)
        self.assertFalse(extrude.imperial_unit_cube.center)
        self.assertIsNone(extrude.imperial_unit_cube.convexity)
        self.assertAlmostEqual(0.0, extrude.imperial_unit_cube.twist)
        self.assertAlmostEqual(1.0, extrude.imperial_unit_cube.scale)
        self.assertIsNone(extrude.imperial_unit_cube.slices)
        self.assertIsNone(extrude.imperial_unit_cube.segments)
        self.assertIsNone(extrude.imperial_unit_cube.fa)
        self.assertAlmostEqual(0.01, extrude.imperial_unit_cube.fs)
        self.assertIsNone(extrude.imperial_unit_cube.fn)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
