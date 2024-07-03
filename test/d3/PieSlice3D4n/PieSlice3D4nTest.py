from d3.PieSlice3D4n.ImperialPieSlice3D4n import ImperialPieSlice3D4n
from ScadTestCase import ScadTestCase
from super_scad.d3.PieSlice3D4n import PieSlice3D4n
from super_scad.Scad import Scad
from super_scad.Unit import Unit


class PieSlice3D4nTest(ScadTestCase):
    """
    Test case for PieSlice3D4n.

    Since PieSlice3D4n is based on PieSlice2D we will not repeat all extensive tests about all angles here.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testPlainPieSlice(self):
        """
        Test case for plain pie slice.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice3D4n(start_angle=-15.0, end_angle=15.0, radius=30.0, height=10.0)

        self.assertAlmostEqual(30.0, pie_slice.angle)
        self.assertAlmostEqual(345.0, pie_slice.start_angle)
        self.assertAlmostEqual(15.0, pie_slice.end_angle)
        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(0.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(10.0, pie_slice.height)

        scad.run_super_scad(pie_slice, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialMetricPieSlice(self):
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = ImperialPieSlice3D4n(start_angle=15.0,
                                         end_angle=-15.0,
                                         radius=30.0,
                                         height=10.0)

        scad.run_super_scad(pie_slice, path_actual)

        self.assertAlmostEqual(330.0, pie_slice.imperial_pie_slice.angle)
        self.assertAlmostEqual(15.0, pie_slice.imperial_pie_slice.start_angle)
        self.assertAlmostEqual(345.0, pie_slice.imperial_pie_slice.end_angle)
        self.assertAlmostEqual(30.0 * 25.4, pie_slice.imperial_pie_slice.radius)
        self.assertAlmostEqual(0.0, pie_slice.imperial_pie_slice.inner_radius)
        self.assertAlmostEqual(30.0 * 25.4, pie_slice.imperial_pie_slice.outer_radius)
        self.assertAlmostEqual(10.0 * 25.4, pie_slice.imperial_pie_slice.height)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialImperialPieSlice(self):
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.INCH)
        pie_slice = ImperialPieSlice3D4n(start_angle=15.0,
                                         end_angle=-15.0,
                                         radius=30.0,
                                         height=10.0)

        scad.run_super_scad(pie_slice, path_actual)

        self.assertAlmostEqual(330.0, pie_slice.imperial_pie_slice.angle)
        self.assertAlmostEqual(15.0, pie_slice.imperial_pie_slice.start_angle)
        self.assertAlmostEqual(345.0, pie_slice.imperial_pie_slice.end_angle)
        self.assertAlmostEqual(30.0, pie_slice.imperial_pie_slice.radius)
        self.assertAlmostEqual(0.0, pie_slice.imperial_pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.imperial_pie_slice.outer_radius)
        self.assertAlmostEqual(10.0, pie_slice.imperial_pie_slice.height)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
