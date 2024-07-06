from d3.PieSlice3D.ImperialPieSlice3D import ImperialPieSlice3D
from ScadTestCase import ScadTestCase
from super_scad.d3.PieSlice3D import PieSlice3D
from super_scad.scad.Scad import Scad
from super_scad.scad.Unit import Unit


class PieSlice3DTest(ScadTestCase):
    """
    Test case for PieSlice3D.

    Since PieSlice3D is based on PieSlice2D we will not repeat all extensive tests about all angles here.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testPlainPieSlice(self):
        """
        Test case for plain pie slice.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice3D(start_angle=-15.0, end_angle=15.0, radius=30.0, height=10.0)

        self.assertAlmostEqual(30.0, pie_slice.angle)
        self.assertAlmostEqual(345.0, pie_slice.start_angle)
        self.assertAlmostEqual(15.0, pie_slice.end_angle)
        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(0.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(10.0, pie_slice.height)
        self.assertEqual(1, pie_slice.convexity)
        self.assertIsNone(pie_slice.fa)
        self.assertIsNone(pie_slice.fs)
        self.assertIsNone(pie_slice.fn)

        scad.run_super_scad(pie_slice, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testAuxiliaryParameters(self):
        """
        Test auxiliary parameters.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice3D(start_angle=15.0, end_angle=-15.0, radius=30.0, height=10.0, fa=12.0, fs=2.0, fn=0)

        self.assertAlmostEqual(330.0, pie_slice.angle)
        self.assertAlmostEqual(15.0, pie_slice.start_angle)
        self.assertAlmostEqual(345.0, pie_slice.end_angle)
        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(0.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(10.0, pie_slice.height)
        self.assertEqual(2, pie_slice.convexity)
        self.assertAlmostEqual(12.0, pie_slice.fa)
        self.assertAlmostEqual(2.0, pie_slice.fs)
        self.assertEqual(0, pie_slice.fn)

        scad.run_super_scad(pie_slice, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialMetricPieSlice(self):
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = ImperialPieSlice3D(start_angle=15.0,
                                       end_angle=-15.0,
                                       radius=30.0,
                                       height=10.0,
                                       fa=12.0,
                                       fs=2.0,
                                       fn=0)

        scad.run_super_scad(pie_slice, path_actual)

        self.assertAlmostEqual(330.0, pie_slice.imperial_pie_slice.angle)
        self.assertAlmostEqual(15.0, pie_slice.imperial_pie_slice.start_angle)
        self.assertAlmostEqual(345.0, pie_slice.imperial_pie_slice.end_angle)
        self.assertAlmostEqual(30.0 * 25.4, pie_slice.imperial_pie_slice.radius)
        self.assertAlmostEqual(0.0, pie_slice.imperial_pie_slice.inner_radius)
        self.assertAlmostEqual(30.0 * 25.4, pie_slice.imperial_pie_slice.outer_radius)
        self.assertAlmostEqual(10.0 * 25.4, pie_slice.imperial_pie_slice.height)
        self.assertEqual(2, pie_slice.imperial_pie_slice.convexity)
        self.assertAlmostEqual(12.0, pie_slice.imperial_pie_slice.fa)
        self.assertAlmostEqual(2.0 * 25.4, pie_slice.imperial_pie_slice.fs)
        self.assertEqual(0, pie_slice.imperial_pie_slice.fn)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialImperialPieSlice(self):
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.INCH)
        pie_slice = ImperialPieSlice3D(start_angle=15.0,
                                       end_angle=-15.0,
                                       radius=30.0,
                                       height=10.0,
                                       fa=12.0,
                                       fs=2.0,
                                       fn=0)

        scad.run_super_scad(pie_slice, path_actual)

        self.assertAlmostEqual(330.0, pie_slice.imperial_pie_slice.angle)
        self.assertAlmostEqual(15.0, pie_slice.imperial_pie_slice.start_angle)
        self.assertAlmostEqual(345.0, pie_slice.imperial_pie_slice.end_angle)
        self.assertAlmostEqual(30.0, pie_slice.imperial_pie_slice.radius)
        self.assertAlmostEqual(0.0, pie_slice.imperial_pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.imperial_pie_slice.outer_radius)
        self.assertAlmostEqual(10.0, pie_slice.imperial_pie_slice.height)
        self.assertEqual(2, pie_slice.imperial_pie_slice.convexity)
        self.assertAlmostEqual(12.0, pie_slice.imperial_pie_slice.fa)
        self.assertAlmostEqual(2.0, pie_slice.imperial_pie_slice.fs)
        self.assertEqual(0, pie_slice.imperial_pie_slice.fn)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
