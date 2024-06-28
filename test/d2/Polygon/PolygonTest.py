import unittest
from pathlib import Path

from d2.Polygon.ImperialUnitPolygon import ImperialUnitPolygon
from super_scad.d2.Polygon import Polygon
from super_scad.Scad import Scad
from super_scad.type.Point2 import Point2
from super_scad.Unit import Unit


class PolygonTestCase(unittest.TestCase):
    """
    Testcases for polygons.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testPlainPolygon(self):
        """
        Plain test for a plain polygon.
        """
        path_actual = 'test/d2/Polygon/testPlainPolygon.actual.scad'
        path_expected = 'test/d2/Polygon/testPlainPolygon.expected.scad'

        scad = Scad(unit=Unit.MM)
        scad.run_super_scad(Polygon(primary=[Point2(0.0, 0.0),
                                             Point2(100.0, 0.0),
                                             Point2(130.0, 50.0),
                                             Point2(30.0, 50.0)]),
                            Path(path_actual))

        actual = Path(path_actual).read_text()
        expected = Path(path_expected).read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testOneHolePolygon(self):
        """
        Plain test for a polygon with one hole.
        """
        path_actual = 'test/d2/Polygon/testOneHolePolygon.actual.scad'
        path_expected = 'test/d2/Polygon/testOneHolePolygon.expected.scad'

        scad = Scad(unit=Unit.MM)
        scad.run_super_scad(Polygon(primary=[Point2(0.0, 0.0),
                                             Point2(100.0, 0.0),
                                             Point2(0.0, 100.0)],
                                    secondary=[Point2(10.0, 10.0),
                                               Point2(80.0, 10.0),
                                               Point2(10.0, 80.0)],
                                    convexity=10),
                            Path(path_actual))

        actual = Path(path_actual).read_text()
        expected = Path(path_expected).read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testMultiHolePolygon(self):
        """
        Plain test for a polygon with multiple holes.
        """
        path_actual = 'test/d2/Polygon/testMultiHolePolygon.actual.scad'
        path_expected = 'test/d2/Polygon/testMultiHolePolygon.expected.scad'

        scad = Scad(unit=Unit.MM)
        scad.run_super_scad(Polygon(primary=[Point2(0.0, 0.0),
                                             Point2(100.0, 0.0),
                                             Point2(130.0, 50.0),
                                             Point2(30.0, 50.0)],
                                    secondaries=[[Point2(20.0, 20.0),
                                                  Point2(40.0, 20.0),
                                                  Point2(30.0, 30.0)],
                                                 [Point2(50.0, 20.0),
                                                  Point2(60.0, 20.0),
                                                  Point2(40.0, 30.0)],
                                                 [Point2(65.0, 10.0),
                                                  Point2(80.0, 10.0),
                                                  Point2(80.0, 40.0),
                                                  Point2(65.0, 40.0)],
                                                 [Point2(98.0, 10.0),
                                                  Point2(115.0, 40.0),
                                                  Point2(85.0, 40.0),
                                                  Point2(85.0, 10.0)]]),
                            Path(path_actual))

        actual = Path(path_actual).read_text()
        expected = Path(path_expected).read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialMetricPolygon(self):
        """
        Test for an imperial unit polygon in metric units.
        """
        path_actual = 'test/d2/Polygon/testImperialMetricPolygon.actual.scad'
        path_expected = 'test/d2/Polygon/testImperialMetricPolygon.expected.scad'

        scad = Scad(unit=Unit.MM)
        scad.run_super_scad(ImperialUnitPolygon(), Path(path_actual))

        actual = Path(path_actual).read_text()
        expected = Path(path_expected).read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialImperialPolygon(self):
        """
        Test for an imperial unit polygon in imperial units.
        """
        path_actual = 'test/d2/Polygon/testImperialImperialPolygon.actual.scad'
        path_expected = 'test/d2/Polygon/testImperialImperialPolygon.expected.scad'

        scad = Scad(unit=Unit.INCH)
        scad.run_super_scad(ImperialUnitPolygon(), Path(path_actual))

        actual = Path(path_actual).read_text()
        expected = Path(path_expected).read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
