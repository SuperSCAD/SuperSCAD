from d2.Polygon.ImperialUnitPolygon import ImperialUnitPolygon
from ScadTestCase import ScadTestCase
from super_scad.d2.Polygon import Polygon
from super_scad.scad.Scad import Scad
from super_scad.scad.Unit import Unit
from super_scad.type.Point2 import Point2


class PolygonTestCase(ScadTestCase):
    """
    Testcases for polygons.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testPlainPolygon(self):
        """
        Plain test for a plain polygon.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        scad.run_super_scad(Polygon(primary=[Point2(0.0, 0.0),
                                             Point2(100.0, 0.0),
                                             Point2(130.0, 50.0),
                                             Point2(30.0, 50.0)]),
                            path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testOneHolePolygon(self):
        """
        Plain test for a polygon with one hole.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        scad.run_super_scad(Polygon(primary=[Point2(0.0, 0.0),
                                             Point2(100.0, 0.0),
                                             Point2(0.0, 100.0)],
                                    secondary=[Point2(10.0, 10.0),
                                               Point2(80.0, 10.0),
                                               Point2(10.0, 80.0)],
                                    convexity=10),
                            path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testMultiHolePolygon(self):
        """
        Plain test for a polygon with multiple holes.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
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
                            path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialMetricPolygon(self):
        """
        Test for an imperial unit polygon in metric units.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        scad.run_super_scad(ImperialUnitPolygon(), path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialImperialPolygon(self):
        """
        Test for an imperial unit polygon in imperial units.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad(unit_length_final=Unit.INCH)
        scad.run_super_scad(ImperialUnitPolygon(), path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
