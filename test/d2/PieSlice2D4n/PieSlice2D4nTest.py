from d2.PieSlice2D4n.ImperialPieSlice2D4n import ImperialPieSlice2D4n
from ScadTestCase import ScadTestCase
from super_scad.d2.PieSlice2D4n import PieSlice2D4n
from super_scad.Scad import Scad
from super_scad.Unit import Unit


class PieSlice2D4n4nTest(ScadTestCase):
    """
    Test cases for PieSlice2D4n.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceQ1(self):
        """
        Test a pie slice that start lies quadrant 1.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=10.0, end_angle=80.0, inner_radius=10.0, outer_radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(10.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(70.0, pie_slice.angle)
        self.assertAlmostEqual(10.0, pie_slice.start_angle)
        self.assertAlmostEqual(80.0, pie_slice.end_angle)
        self.assertEqual(1, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceQ2(self):
        """
        Test a pie slice that start lies quadrant 2.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=100.0, end_angle=170.0, inner_radius=10.0, outer_radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(10.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(70.0, pie_slice.angle)
        self.assertAlmostEqual(100.0, pie_slice.start_angle)
        self.assertAlmostEqual(170.0, pie_slice.end_angle)
        self.assertEqual(1, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceQ3(self):
        """
        Test a pie slice that start lies quadrant 3.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=190.0, end_angle=260.0, inner_radius=10.0, outer_radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(10.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(70.0, pie_slice.angle)
        self.assertAlmostEqual(190.0, pie_slice.start_angle)
        self.assertAlmostEqual(260.0, pie_slice.end_angle)
        self.assertEqual(1, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceQ4(self):
        """
        Test a pie slice that start lies quadrant 4.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=280.0, end_angle=350.0, inner_radius=10.0, outer_radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(10.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(70.0, pie_slice.angle)
        self.assertAlmostEqual(280.0, pie_slice.start_angle)
        self.assertAlmostEqual(350.0, pie_slice.end_angle)
        self.assertEqual(1, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceIsQ1(self):
        """
        Test a pie slice that is quadrant 1.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=0.0, end_angle=90.0, radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(0.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(90.0, pie_slice.angle)
        self.assertAlmostEqual(0.0, pie_slice.start_angle)
        self.assertAlmostEqual(90.0, pie_slice.end_angle)
        self.assertEqual(1, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceIsQ2(self):
        """
        Test a pie slice that is quadrant 2.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=90.0, end_angle=180.0, radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(0.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(90.0, pie_slice.angle)
        self.assertAlmostEqual(90.0, pie_slice.start_angle)
        self.assertAlmostEqual(180.0, pie_slice.end_angle)
        self.assertEqual(1, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceIsQ3(self):
        """
        Test a pie slice that is quadrant 3.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=180.0, end_angle=270.0, radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(0.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(90.0, pie_slice.angle)
        self.assertAlmostEqual(180.0, pie_slice.start_angle)
        self.assertAlmostEqual(270.0, pie_slice.end_angle)
        self.assertEqual(1, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceIsQ4(self):
        """
        Test a pie slice that is quadrant 4.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=270.0, end_angle=360.0, radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(0.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(90.0, pie_slice.angle)
        self.assertAlmostEqual(270.0, pie_slice.start_angle)
        self.assertAlmostEqual(0.0, pie_slice.end_angle)
        self.assertEqual(1, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceIsQ1Q2(self):
        """
        Test a pie slice that is quadrant 1 & 2.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=0.0, end_angle=180.0, radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(0.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(180.0, pie_slice.angle)
        self.assertAlmostEqual(0.0, pie_slice.start_angle)
        self.assertAlmostEqual(180.0, pie_slice.end_angle)
        self.assertEqual(2, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceIsQ2Q3(self):
        """
        Test a pie slice that is quadrant 2 & 3.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=90.0, end_angle=270.0, radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(0.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(180.0, pie_slice.angle)
        self.assertAlmostEqual(90.0, pie_slice.start_angle)
        self.assertAlmostEqual(270.0, pie_slice.end_angle)
        self.assertEqual(2, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceIsQ3Q4(self):
        """
        Test a pie slice that is quadrant 3 & 4.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=180.0, end_angle=360.0, radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(0.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(180.0, pie_slice.angle)
        self.assertAlmostEqual(180.0, pie_slice.start_angle)
        self.assertAlmostEqual(0.0, pie_slice.end_angle)
        self.assertEqual(2, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceIsQ4Q1(self):
        """
        Test a pie slice that is quadrant 3 & 4.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=270.0, end_angle=90.0, radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(0.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(180.0, pie_slice.angle)
        self.assertAlmostEqual(270.0, pie_slice.start_angle)
        self.assertAlmostEqual(90.0, pie_slice.end_angle)
        self.assertEqual(2, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceIsQ1Q2Q3(self):
        """
        Test a pie slice that is quadrant 1, 2, & 3.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=0.0, end_angle=270.0, radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(0.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(270.0, pie_slice.angle)
        self.assertAlmostEqual(0.0, pie_slice.start_angle)
        self.assertAlmostEqual(270.0, pie_slice.end_angle)
        self.assertEqual(2, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceIsQ2Q3Q4(self):
        """
        Test a pie slice that is quadrant 2, 3 & 4.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=90.0, end_angle=360.0, radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(0.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(270.0, pie_slice.angle)
        self.assertAlmostEqual(90.0, pie_slice.start_angle)
        self.assertAlmostEqual(0.0, pie_slice.end_angle)
        self.assertEqual(2, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceIsQ3Q4Q1(self):
        """
        Test a pie slice that is quadrant 3, 4 & 1.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=180.0, end_angle=90.0, radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(0.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(270.0, pie_slice.angle)
        self.assertAlmostEqual(180.0, pie_slice.start_angle)
        self.assertAlmostEqual(90.0, pie_slice.end_angle)
        self.assertEqual(2, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceIsQ4Q1Q2(self):
        """
        Test a pie slice that is quadrant 4, 1 & 2.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=270.0, end_angle=180.0, radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(0.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(270.0, pie_slice.angle)
        self.assertAlmostEqual(270.0, pie_slice.start_angle)
        self.assertAlmostEqual(180.0, pie_slice.end_angle)
        self.assertEqual(2, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceIsQ1Q2Q3Q4(self):
        """
        Test a pie slice that is quadrant 1, 2, 3, & 4.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=0.0, end_angle=360.0 - 1e-8, radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(0.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(360.0, pie_slice.angle)
        self.assertAlmostEqual(0.0, pie_slice.start_angle)
        self.assertAlmostEqual(360.0, pie_slice.end_angle)
        self.assertEqual(2, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceQ1Q2(self):
        """
        Test a pie slice that start in quadrant 1 and ends in quadrant 2.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=80.0, end_angle=100.0, inner_radius=10.0, outer_radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(10.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(20.0, pie_slice.angle)
        self.assertAlmostEqual(80.0, pie_slice.start_angle)
        self.assertAlmostEqual(100.0, pie_slice.end_angle)
        self.assertEqual(1, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceQ2Q3(self):
        """
        Test a pie slice that start in quadrant 2 and ends in quadrant 3.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=170.0, end_angle=190.0, inner_radius=10.0, outer_radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(10.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(20.0, pie_slice.angle)
        self.assertAlmostEqual(170.0, pie_slice.start_angle)
        self.assertAlmostEqual(190.0, pie_slice.end_angle)
        self.assertEqual(1, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceQ3Q4(self):
        """
        Test a pie slice that start in quadrant 3 and ends in quadrant 4.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=260.0, end_angle=280.0, inner_radius=10.0, outer_radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(10.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(20.0, pie_slice.angle)
        self.assertAlmostEqual(260.0, pie_slice.start_angle)
        self.assertAlmostEqual(280.0, pie_slice.end_angle)
        self.assertEqual(1, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceQ3Q1b(self):
        """
        Test a pie slice that start in quadrant 3 and ends in quadrant 1.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=180.01, end_angle=89.99, inner_radius=10.0, outer_radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(10.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(269.98, pie_slice.angle)
        self.assertAlmostEqual(180.01, pie_slice.start_angle)
        self.assertAlmostEqual(89.99, pie_slice.end_angle)
        self.assertEqual(2, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceQ3Q1c(self):
        """
        Test a pie slice that start in quadrant 3 and ends in quadrant 1.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=269.99, end_angle=0.01, inner_radius=10.0, outer_radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(10.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(90.02, pie_slice.angle)
        self.assertAlmostEqual(269.99, pie_slice.start_angle)
        self.assertAlmostEqual(0.01, pie_slice.end_angle)
        self.assertEqual(1, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceQ4Q1a(self):
        """
        Test a pie slice that start in quadrant 4 and ends in quadrant 1.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=350.0, end_angle=370.0, inner_radius=10.0, outer_radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(10.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(20.0, pie_slice.angle)
        self.assertAlmostEqual(350.0, pie_slice.start_angle)
        self.assertAlmostEqual(10.0, pie_slice.end_angle)
        self.assertEqual(1, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceQ4Q1b(self):
        """
        Test a pie slice that start in quadrant 4 and ends in quadrant 1.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=270.01, end_angle=89.99, inner_radius=10.0, outer_radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(10.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(179.98, pie_slice.angle)
        self.assertAlmostEqual(270.01, pie_slice.start_angle)
        self.assertAlmostEqual(89.99, pie_slice.end_angle)
        self.assertEqual(1, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceQ1Q3a(self):
        """
        Test a pie slice that start in quadrant 1 and ends in quadrant 3.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=15.0, end_angle=265.0, inner_radius=10.0, outer_radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(10.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(250.0, pie_slice.angle)
        self.assertAlmostEqual(15.0, pie_slice.start_angle)
        self.assertAlmostEqual(265.0, pie_slice.end_angle)
        self.assertEqual(2, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceQ1Q3b(self):
        """
        Test a pie slice that start in quadrant 1 and ends in quadrant 3.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=0.01, end_angle=269.99, inner_radius=10.0, outer_radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(10.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(269.98, pie_slice.angle)
        self.assertAlmostEqual(0.01, pie_slice.start_angle)
        self.assertAlmostEqual(269.99, pie_slice.end_angle)
        self.assertEqual(2, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceQ1Q3c(self):
        """
        Test a pie slice that start in quadrant 1 and ends in quadrant 3.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=89.99, end_angle=180.01, inner_radius=10.0, outer_radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(10.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(90.02, pie_slice.angle)
        self.assertAlmostEqual(89.99, pie_slice.start_angle)
        self.assertAlmostEqual(180.01, pie_slice.end_angle)
        self.assertEqual(1, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceQ2Q4a(self):
        """
        Test a pie slice that start in quadrant 2 and ends in quadrant 4.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=105, end_angle=355.0, inner_radius=10.0, outer_radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(10.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(250.0, pie_slice.angle)
        self.assertAlmostEqual(105.0, pie_slice.start_angle)
        self.assertAlmostEqual(355.0, pie_slice.end_angle)
        self.assertEqual(2, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceQ2Q4b(self):
        """
        Test a pie slice that start in quadrant 2 and ends in quadrant 4.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=90.01, end_angle=-0.01, inner_radius=10.0, outer_radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(10.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(269.98, pie_slice.angle)
        self.assertAlmostEqual(90.01, pie_slice.start_angle)
        self.assertAlmostEqual(359.99, pie_slice.end_angle)
        self.assertEqual(2, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceQ2Q4c(self):
        """
        Test a pie slice that start in quadrant 2 and ends in quadrant 4.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=179.99, end_angle=-89.99, inner_radius=10.0, outer_radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(10.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(90.02, pie_slice.angle)
        self.assertAlmostEqual(179.99, pie_slice.start_angle)
        self.assertAlmostEqual(270.01, pie_slice.end_angle)
        self.assertEqual(1, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceNegative(self):
        """
        Test a pie slice with a negative angle.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(angle=-20, radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(0.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(20.0, pie_slice.angle)
        self.assertAlmostEqual(340.0, pie_slice.start_angle)
        self.assertAlmostEqual(0.0, pie_slice.end_angle)
        self.assertEqual(1, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSlicePositive(self):
        """
        Test a pie slice with a positive angle.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(angle=20, radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(0.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(20.0, pie_slice.angle)
        self.assertAlmostEqual(0.0, pie_slice.start_angle)
        self.assertAlmostEqual(20.0, pie_slice.end_angle)
        self.assertEqual(1, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceMissingSliceQ1a(self):
        """
        Test a pie slice with a positive angle.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=25, end_angle=15, radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(0.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(350.0, pie_slice.angle)
        self.assertAlmostEqual(25.0, pie_slice.start_angle)
        self.assertAlmostEqual(15.0, pie_slice.end_angle)
        self.assertEqual(2, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceMissingSliceQ1b(self):
        """
        Test a pie slice with a positive angle.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=25, end_angle=0.0, radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(0.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(335.0, pie_slice.angle)
        self.assertAlmostEqual(25.0, pie_slice.start_angle)
        self.assertAlmostEqual(0.0, pie_slice.end_angle)
        self.assertEqual(2, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceMissingSliceQ2(self):
        """
        Test a pie slice with a positive angle.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=110, end_angle=95, radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(0.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(345.0, pie_slice.angle)
        self.assertAlmostEqual(110.0, pie_slice.start_angle)
        self.assertAlmostEqual(95.0, pie_slice.end_angle)
        self.assertEqual(2, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceMissingSliceQ3(self):
        """
        Test a pie slice with a positive angle.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=269, end_angle=181, radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(0.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(272.0, pie_slice.angle)
        self.assertAlmostEqual(269.0, pie_slice.start_angle)
        self.assertAlmostEqual(181.0, pie_slice.end_angle)
        self.assertEqual(2, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceMissingSliceQ4a(self):
        """
        Test a pie slice with a positive angle.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=-30, end_angle=-40, radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(0.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(350.0, pie_slice.angle)
        self.assertAlmostEqual(330.0, pie_slice.start_angle)
        self.assertAlmostEqual(320.0, pie_slice.end_angle)
        self.assertEqual(2, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPieSliceMissingSliceQ4b(self):
        """
        Test a pie slice with a positive angle.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = PieSlice2D4n(start_angle=0.0, end_angle=-40, radius=30.0)

        self.assertAlmostEqual(30.0, pie_slice.radius)
        self.assertAlmostEqual(0.0, pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.outer_radius)
        self.assertAlmostEqual(320.0, pie_slice.angle)
        self.assertAlmostEqual(0.0, pie_slice.start_angle)
        self.assertAlmostEqual(320.0, pie_slice.end_angle)
        self.assertEqual(2, pie_slice.convexity)

        scad.run_super_scad(pie_slice, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialMetricPieSlice(self):
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        pie_slice = ImperialPieSlice2D4n(start_angle=15.0,
                                         end_angle=-15.0,
                                         radius=30.0)

        scad.run_super_scad(pie_slice, path_actual)

        self.assertAlmostEqual(330.0, pie_slice.imperial_pie_slice.angle)
        self.assertAlmostEqual(15.0, pie_slice.imperial_pie_slice.start_angle)
        self.assertAlmostEqual(345.0, pie_slice.imperial_pie_slice.end_angle)
        self.assertAlmostEqual(30.0 * 25.4, pie_slice.imperial_pie_slice.radius)
        self.assertAlmostEqual(0.0, pie_slice.imperial_pie_slice.inner_radius)
        self.assertAlmostEqual(30.0 * 25.4, pie_slice.imperial_pie_slice.outer_radius)
        self.assertEqual(2, pie_slice.imperial_pie_slice.convexity)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialImperialPieSlice(self):
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.INCH)
        pie_slice = ImperialPieSlice2D4n(start_angle=15.0,
                                         end_angle=-15.0,
                                         radius=30.0)

        scad.run_super_scad(pie_slice, path_actual)

        self.assertAlmostEqual(330.0, pie_slice.imperial_pie_slice.angle)
        self.assertAlmostEqual(15.0, pie_slice.imperial_pie_slice.start_angle)
        self.assertAlmostEqual(345.0, pie_slice.imperial_pie_slice.end_angle)
        self.assertAlmostEqual(30.0, pie_slice.imperial_pie_slice.radius)
        self.assertAlmostEqual(0.0, pie_slice.imperial_pie_slice.inner_radius)
        self.assertAlmostEqual(30.0, pie_slice.imperial_pie_slice.outer_radius)
        self.assertEqual(2, pie_slice.imperial_pie_slice.convexity)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
