import math

from d2.RegularPolygon.ImperialUnitPentagon import ImperialUnitPentagon
from ScadTestCase import ScadTestCase
from super_scad.boolean.Union import Union
from super_scad.d2.Circle4n import Circle4n
from super_scad.d2.RegularPolygon import RegularPolygon
from super_scad.scad.Scad import Scad
from super_scad.scad.Unit import Unit
from super_scad.transformation.Paint import Paint
from super_scad.type.Color import Color


class RegularPolygonTestCase(ScadTestCase):
    """
    Testcases for regular polygons.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testSquareInnerRadius(self):
        """
        Test for a regular polygon defined by its inner radius.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit_length_final=Unit.MM)
        polygon = RegularPolygon(sides=4, inner_radius=1.0)

        self.assertAlmostEqual(1.0, polygon.inner_radius)
        self.assertAlmostEqual(math.sqrt(2.0), polygon.outer_radius)
        self.assertAlmostEqual(2.0, polygon.size)
        self.assertAlmostEqual(90.0, polygon.inner_angle)
        self.assertAlmostEqual(90.0, polygon.exterior_angle)

        angles = polygon.angles
        self.assertAlmostEqual(45.0, angles[0])
        self.assertAlmostEqual(135.0, angles[1])
        self.assertAlmostEqual(225.0, angles[2])
        self.assertAlmostEqual(315.0, angles[3])

        scad.run_super_scad(polygon, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testSquareOuterRadius(self):
        """
        Test for a regular polygon defined by its outer radius.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit_length_final=Unit.MM)
        polygon = RegularPolygon(sides=4, outer_radius=1.0)

        self.assertAlmostEqual(0.5 * math.sqrt(2.0), polygon.inner_radius)
        self.assertAlmostEqual(1.0, polygon.outer_radius)
        self.assertAlmostEqual(math.sqrt(2.0), polygon.size)
        self.assertAlmostEqual(90.0, polygon.inner_angle)
        self.assertAlmostEqual(90.0, polygon.exterior_angle)

        angles = polygon.angles
        self.assertAlmostEqual(45.0, angles[0])
        self.assertAlmostEqual(135.0, angles[1])
        self.assertAlmostEqual(225.0, angles[2])
        self.assertAlmostEqual(315.0, angles[3])

        scad.run_super_scad(polygon, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testSquareSize(self):
        """
        Test for a regular polygon defined by its size.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit_length_final=Unit.MM)
        polygon = RegularPolygon(sides=4, size=1.0)

        self.assertAlmostEqual(0.5, polygon.inner_radius)
        self.assertAlmostEqual(0.5 * math.sqrt(2.0), polygon.outer_radius)
        self.assertAlmostEqual(1.0, polygon.size)
        self.assertAlmostEqual(90.0, polygon.inner_angle)
        self.assertAlmostEqual(90.0, polygon.exterior_angle)

        angles = polygon.angles
        self.assertAlmostEqual(45.0, angles[0])
        self.assertAlmostEqual(135.0, angles[1])
        self.assertAlmostEqual(225.0, angles[2])
        self.assertAlmostEqual(315.0, angles[3])

        scad.run_super_scad(polygon, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPentagonInnerRadius(self):
        """
        Test for a regular polygon defined by its inner radius.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit_length_final=Unit.MM)
        polygon = RegularPolygon(sides=5, inner_radius=1.0)

        self.assertAlmostEqual(1.0, polygon.inner_radius)
        self.assertAlmostEqual(1.0 / math.cos(math.pi / 5), polygon.outer_radius)
        self.assertAlmostEqual(2 * math.tan(math.pi / 5), polygon.size)
        self.assertAlmostEqual(108.0, polygon.inner_angle)
        self.assertAlmostEqual(72.0, polygon.exterior_angle)

        angles = polygon.angles
        self.assertAlmostEqual(90.0, angles[0])
        self.assertAlmostEqual(162.0, angles[1])
        self.assertAlmostEqual(234.0, angles[2])
        self.assertAlmostEqual(306.0, angles[3])
        self.assertAlmostEqual(378.0, angles[4])

        union = Union(children=[Paint(color=Color(color='blue'), child=Circle4n(radius=polygon.outer_radius)),
                                Paint(color=Color(color='red'), child=polygon),
                                Paint(color=Color(color='green'), child=Circle4n(radius=polygon.inner_radius))])

        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPentagonOuterRadius(self):
        """
        Test for a regular polygon defined by its outer radius.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit_length_final=Unit.MM)
        polygon = RegularPolygon(sides=5, outer_radius=1.0)

        self.assertAlmostEqual(1.0 * math.cos(math.pi / 5), polygon.inner_radius)
        self.assertAlmostEqual(1.0, polygon.outer_radius)
        self.assertAlmostEqual(2 * math.sin(math.pi / 5), polygon.size)
        self.assertAlmostEqual(108.0, polygon.inner_angle)
        self.assertAlmostEqual(72.0, polygon.exterior_angle)

        angles = polygon.angles
        self.assertAlmostEqual(90.0, angles[0])
        self.assertAlmostEqual(162.0, angles[1])
        self.assertAlmostEqual(234.0, angles[2])
        self.assertAlmostEqual(306.0, angles[3])
        self.assertAlmostEqual(378.0, angles[4])

        scad.run_super_scad(polygon, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPentagonSize(self):
        """
        Test for a regular polygon defined by its size.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit_length_final=Unit.MM)
        polygon = RegularPolygon(sides=5, size=1.0)

        self.assertAlmostEqual(1.0 / (2 * math.tan(math.pi / 5)), polygon.inner_radius)
        self.assertAlmostEqual(1.0 / (2 * math.sin(math.pi / 5)), polygon.outer_radius)
        self.assertAlmostEqual(1.0, polygon.size)
        self.assertAlmostEqual(108.0, polygon.inner_angle)
        self.assertAlmostEqual(72.0, polygon.exterior_angle)

        angles = polygon.angles
        self.assertAlmostEqual(90.0, angles[0])
        self.assertAlmostEqual(162.0, angles[1])
        self.assertAlmostEqual(234.0, angles[2])
        self.assertAlmostEqual(306.0, angles[3])
        self.assertAlmostEqual(378.0, angles[4])

        scad.run_super_scad(polygon, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialMetricPentagonSize(self):
        """
        Test for an imperial unit pentagon in metric units.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit_length_final=Unit.MM)
        polygon = ImperialUnitPentagon()
        scad.run_super_scad(polygon, path_actual)

        self.assertAlmostEqual(25.4 / (2 * math.tan(math.pi / 5)), polygon.imperial_pentagon.inner_radius)
        self.assertAlmostEqual(25.4 / (2 * math.sin(math.pi / 5)), polygon.imperial_pentagon.outer_radius)
        self.assertAlmostEqual(25.4, polygon.imperial_pentagon.size)
        self.assertAlmostEqual(polygon.imperial_pentagon.nodes[0].y, polygon.imperial_pentagon.outer_radius)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialImperialPentagonSize(self):
        """
        Test for an imperial unit pentagon in imperial units.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit_length_final=Unit.INCH)
        polygon = ImperialUnitPentagon()

        scad.run_super_scad(polygon, path_actual)

        self.assertAlmostEqual(1.0 / (2 * math.tan(math.pi / 5)), polygon.imperial_pentagon.inner_radius)
        self.assertAlmostEqual(1.0 / (2 * math.sin(math.pi / 5)), polygon.imperial_pentagon.outer_radius)
        self.assertAlmostEqual(1.0, polygon.imperial_pentagon.size)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
