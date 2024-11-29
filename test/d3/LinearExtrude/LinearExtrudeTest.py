from d3.LinearExtrude.ImperialUnitCube import ImperialUnitCube
from ScadTestCase import ScadTestCase
from super_scad.d2.Circle import Circle
from super_scad.d3.LinearExtrude import LinearExtrude
from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad.scad.Unit import Unit
from super_scad.transformation.Translate2D import Translate2D
from super_scad.type.Vector2 import Vector2


class LinearExtrudeTest(ScadTestCase):
    """
    Test cases for LinearExtrude.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_sample1(self):
        """
        Test sample 1 from the OpenSCAD cheatsheet.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
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
    def test_sample2(self):
        """
        Test sample 2 from the OpenSCAD cheatsheet.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
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
    def test_sample3(self):
        """
        Test sample 3 from the OpenSCAD cheatsheet.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
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
    def test_sample4(self):
        """
        Test sample 4 from the OpenSCAD cheatsheet.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
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
    def test_sample5(self):
        """
        Test sample 5 from the OpenSCAD cheatsheet.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
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
    def test_sample6(self):
        """
        Test sample 6 from the OpenSCAD cheatsheet.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
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
    def test_sample7(self):
        """
        Test sample 7 from the OpenSCAD cheatsheet.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
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
    def test_sample8(self):
        """
        Test sample 8 from the OpenSCAD cheatsheet.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
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
    def test_sample9(self):
        """
        Test sample 9 from the OpenSCAD cheatsheet.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        polygon = [Vector2(0.0, 0.0), Vector2(20.0, 10.0), Vector2(20.0, -10.0)]
        extrude = LinearExtrude(height=10.0,
                                center=True,
                                convexity=10,
                                scale=Vector2(1, 5),
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
    def test_imperial_metric_linear_extrude(self):
        """
        Test for an extrude imperial unit cube in metric units.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        extrude = ImperialUnitCube()

        scad.run_super_scad(extrude, path_actual)

        # self.assertAlmostEqual(25.4, extrude.imperial_unit_cube.height)
        self.assertFalse(extrude.imperial_unit_cube.center)
        self.assertIsNone(extrude.imperial_unit_cube.convexity)
        self.assertAlmostEqual(0.0, extrude.imperial_unit_cube.twist)
        self.assertAlmostEqual(1.0, extrude.imperial_unit_cube.scale)
        self.assertIsNone(extrude.imperial_unit_cube.slices)
        self.assertIsNone(extrude.imperial_unit_cube.segments)
        self.assertIsNone(extrude.imperial_unit_cube.fa)
        # self.assertAlmostEqual(0.254, extrude.imperial_unit_cube.fs)
        self.assertIsNone(extrude.imperial_unit_cube.fn)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_imperial_imperial_linear_extrude(self):
        """
        Test for an extruded imperial unit cube in imperial units.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad(unit_length_final=Unit.INCH)
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

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_top_no_center(self):
        """
        Test extend top by eps only.
        """
        context = Context(eps=1.0)
        scad = Scad(context=context)

        extrude = LinearExtrude(height=20.0, extend_by_eps_top=True, child=Circle(radius=1.0))

        self.assertAlmostEqual(20.0, extrude.height)
        self.assertFalse(extrude.center)
        self.assertTrue(extrude.extend_by_eps_top)
        self.assertFalse(extrude.extend_by_eps_bottom)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(extrude, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_top_center(self):
        """
        Test extend top by eps only and center.
        """
        context = Context(eps=1.0)
        scad = Scad(context=context)

        extrude = LinearExtrude(height=20.0, center=True, extend_by_eps_top=True, child=Circle(radius=1.0))

        self.assertAlmostEqual(20.0, extrude.height)
        self.assertTrue(extrude.center)
        self.assertTrue(extrude.extend_by_eps_top)
        self.assertFalse(extrude.extend_by_eps_bottom)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(extrude, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_bottom_no_center(self):
        """
        Test extend bottom by eps only.
        """
        context = Context(eps=1.0)
        scad = Scad(context=context)

        extrude = LinearExtrude(height=20.0, extend_by_eps_bottom=True, child=Circle(radius=1.0))

        self.assertAlmostEqual(20.0, extrude.height)
        self.assertFalse(extrude.center)
        self.assertFalse(extrude.extend_by_eps_top)
        self.assertTrue(extrude.extend_by_eps_bottom)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(extrude, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_bottom_center(self):
        """
        Test extend bottom by eps only and center.
        """
        context = Context(eps=1.0)
        scad = Scad(context=context)

        extrude = LinearExtrude(height=20.0, center=True, extend_by_eps_bottom=True, child=Circle(radius=1.0))

        self.assertAlmostEqual(20.0, extrude.height)
        self.assertTrue(extrude.center)
        self.assertFalse(extrude.extend_by_eps_top)
        self.assertTrue(extrude.extend_by_eps_bottom)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(extrude, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_top_bottom_by_eps_no_center(self):
        """
        Test extend top and bottom by eps.
        """
        context = Context(eps=1.0)
        scad = Scad(context=context)

        extrude = LinearExtrude(height=20.0,
                                extend_by_eps_top=True,
                                extend_by_eps_bottom=True,
                                child=Circle(radius=1.0))

        self.assertAlmostEqual(20.0, extrude.height)
        self.assertFalse(extrude.center)
        self.assertTrue(extrude.extend_by_eps_top)
        self.assertTrue(extrude.extend_by_eps_bottom)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(extrude, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_top_bottom_by_eps_center(self):
        """
        Test extend top and bottom by eps and center.
        """
        context = Context(eps=1.0)
        scad = Scad(context=context)

        extrude = LinearExtrude(height=20.0,
                                center=True,
                                extend_by_eps_top=True,
                                extend_by_eps_bottom=True,
                                child=Circle(radius=1.0))

        self.assertAlmostEqual(20.0, extrude.height)
        self.assertTrue(extrude.center)
        self.assertTrue(extrude.extend_by_eps_top)
        self.assertTrue(extrude.extend_by_eps_bottom)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(extrude, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
