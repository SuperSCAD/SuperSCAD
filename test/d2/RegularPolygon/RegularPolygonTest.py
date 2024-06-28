import math
import unittest
from pathlib import Path

from d2.RegularPolygon.ImperialUnitPentagon import ImperialUnitPentagon
from super_scad.boolean.Union import Union
from super_scad.d2.Circle4n import Circle4n
from super_scad.d2.RegularPolygon import RegularPolygon
from super_scad.Scad import Scad
from super_scad.transformation.Paint import Paint
from super_scad.type.Color import Color
from super_scad.Unit import Unit


class RegularPolygonTestCase(unittest.TestCase):
    """
    Testcases for regular polygons.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testSquareInnerRadius(self):
        """
        Test for a regular polygon defined by its inner radius.
        """
        path_actual = 'test/d2/RegularPolygon/testSquareInnerRadius.actual.scad'
        path_expected = 'test/d2/RegularPolygon/testSquareInnerRadius.expected.scad'

        scad = Scad(unit=Unit.MM)
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

        scad.run_super_scad(polygon, Path(path_actual))
        actual = Path(path_actual).read_text()
        expected = Path(path_expected).read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testSquareOuterRadius(self):
        """
        Test for a regular polygon defined by its outer radius.
        """
        path_actual = 'test/d2/RegularPolygon/testSquareOuterRadius.actual.scad'
        path_expected = 'test/d2/RegularPolygon/testSquareOuterRadius.expected.scad'

        scad = Scad(unit=Unit.MM)
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

        scad.run_super_scad(polygon, Path(path_actual))
        actual = Path(path_actual).read_text()
        expected = Path(path_expected).read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testSquareSize(self):
        """
        Test for a regular polygon defined by its size.
        """
        path_actual = 'test/d2/RegularPolygon/testSquareSize.actual.scad'
        path_expected = 'test/d2/RegularPolygon/testSquareSize.expected.scad'

        scad = Scad(unit=Unit.MM)
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

        scad.run_super_scad(polygon, Path(path_actual))
        actual = Path(path_actual).read_text()
        expected = Path(path_expected).read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPentagonInnerRadius(self):
        """
        Test for a regular polygon defined by its inner radius.
        """
        path_actual = 'test/d2/RegularPolygon/testPentagonInnerRadius.actual.scad'
        path_expected = 'test/d2/RegularPolygon/testPentagonInnerRadius.expected.scad'

        scad = Scad(unit=Unit.MM)
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

        scad.run_super_scad(union, Path(path_actual))
        actual = Path(path_actual).read_text()
        expected = Path(path_expected).read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPentagonOuterRadius(self):
        """
        Test for a regular polygon defined by its outer radius.
        """
        path_actual = 'test/d2/RegularPolygon/testPentagonOuterRadius.actual.scad'
        path_expected = 'test/d2/RegularPolygon/testPentagonOuterRadius.expected.scad'

        scad = Scad(unit=Unit.MM)
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

        scad.run_super_scad(polygon, Path(path_actual))
        actual = Path(path_actual).read_text()
        expected = Path(path_expected).read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPentagonSize(self):
        """
        Test for a regular polygon defined by its size.
        """
        path_actual = 'test/d2/RegularPolygon/testPentagonSize.actual.scad'
        path_expected = 'test/d2/RegularPolygon/testPentagonSize.expected.scad'

        scad = Scad(unit=Unit.MM)
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

        scad.run_super_scad(polygon, Path(path_actual))
        actual = Path(path_actual).read_text()
        expected = Path(path_expected).read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialMetricPentagonSize(self):
        """
        Test for an imperial unit pentagon in metric units.
        """
        path_actual = 'test/d2/RegularPolygon/testImperialMetricPentagonSize.actual.scad'
        path_expected = 'test/d2/RegularPolygon/testImperialMetricPentagonSize.expected.scad'

        scad = Scad(unit=Unit.MM)
        polygon = ImperialUnitPentagon()

        scad.run_super_scad(polygon, Path(path_actual))

        self.assertAlmostEqual(25.4 / (2 * math.tan(math.pi / 5)), polygon.inner_radius)
        self.assertAlmostEqual(25.4 / (2 * math.sin(math.pi / 5)), polygon.outer_radius)
        self.assertAlmostEqual(25.4, polygon.size)
        self.assertAlmostEqual(polygon.nodes[0].y, polygon.outer_radius)

        actual = Path(path_actual).read_text()
        expected = Path(path_expected).read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialImperialPentagonSize(self):
        """
        Test for an imperial unit pentagon in imperial units.
        """
        path_actual = 'test/d2/RegularPolygon/testImperialImperialPentagonSize.actual.scad'
        path_expected = 'test/d2/RegularPolygon/testImperialImperialPentagonSize.expected.scad'

        scad = Scad(unit=Unit.INCH)
        polygon = ImperialUnitPentagon()

        scad.run_super_scad(polygon, Path(path_actual))

        self.assertAlmostEqual(1.0 / (2 * math.tan(math.pi / 5)), polygon.inner_radius)
        self.assertAlmostEqual(1.0 / (2 * math.sin(math.pi / 5)), polygon.outer_radius)
        self.assertAlmostEqual(1.0, polygon.size)

        actual = Path(path_actual).read_text()
        expected = Path(path_expected).read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
