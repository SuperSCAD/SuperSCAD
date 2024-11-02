import math

from d2.Polygon.ImperialUnitPolygon import ImperialUnitPolygon
from ScadTestCase import ScadTestCase
from super_scad.d2.Polygon import Polygon
from super_scad.scad.Unit import Unit
from super_scad.type.Vector2 import Vector2


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
        scad.run_super_scad(Polygon(primary=[Vector2(0.0, 0.0),
                                             Vector2(100.0, 0.0),
                                             Vector2(130.0, 50.0),
                                             Vector2(30.0, 50.0)]),
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
        scad.run_super_scad(Polygon(primary=[Vector2(0.0, 0.0),
                                             Vector2(100.0, 0.0),
                                             Vector2(0.0, 100.0)],
                                    secondary=[Vector2(10.0, 10.0),
                                               Vector2(80.0, 10.0),
                                               Vector2(10.0, 80.0)],
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
        scad.run_super_scad(Polygon(primary=[Vector2(0.0, 0.0),
                                             Vector2(100.0, 0.0),
                                             Vector2(130.0, 50.0),
                                             Vector2(30.0, 50.0)],
                                    secondaries=[[Vector2(20.0, 20.0),
                                                  Vector2(40.0, 20.0),
                                                  Vector2(30.0, 30.0)],
                                                 [Vector2(50.0, 20.0),
                                                  Vector2(60.0, 20.0),
                                                  Vector2(40.0, 30.0)],
                                                 [Vector2(65.0, 10.0),
                                                  Vector2(80.0, 10.0),
                                                  Vector2(80.0, 40.0),
                                                  Vector2(65.0, 40.0)],
                                                 [Vector2(98.0, 10.0),
                                                  Vector2(115.0, 40.0),
                                                  Vector2(85.0, 40.0),
                                                  Vector2(85.0, 10.0)]]),
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

    # ------------------------------------------------------------------------------------------------------------------
    def testInnerAngles1(self):
        """
        Test inner and normal angles.
        """
        polygon = Polygon(primary=[Vector2(0.0, 0.0), Vector2(10.0, 0.0), Vector2(0.0, 10.0)])

        actual = polygon.inner_angels
        expected = [90.0, 45.0, 45.0]
        self.assertEqual(len(expected), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected[i], actual[i])

        actual = polygon.normal_angels
        expected = [45.0, 157.5, 292.5]
        self.assertEqual(len(expected), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected[i], actual[i])

    # ------------------------------------------------------------------------------------------------------------------
    def testInnerAngles2(self):
        """
        Test inner angles.
        """
        polygon = Polygon(primary=[Vector2(-10.0, 0.0), Vector2(10.0, 0.0), Vector2(0.0, 10.0 * math.sqrt(3.0))])

        actual = polygon.inner_angels
        expected = [60.0, 60.0, 60.0]
        self.assertEqual(len(expected), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected[i], actual[i])

        actual = polygon.normal_angels
        expected = [30.0, 150.0, 270.0]
        self.assertEqual(len(expected), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected[i], actual[i])

    # ------------------------------------------------------------------------------------------------------------------
    def testInnerAngles3(self):
        """
        Test inner angles.
        """
        polygon = Polygon(primary=[Vector2(3.0, 0.0),
                                   Vector2(2.0, 1.0),
                                   Vector2(2.0, 2.0),
                                   Vector2(1.0, 2.0),

                                   Vector2(0.0, 3.0),
                                   Vector2(-1.0, 2.0),
                                   Vector2(-2.0, 2.0),
                                   Vector2(-2.0, 1.0),

                                   Vector2(-3.0, 0.0),
                                   Vector2(-2.0, -1.0),
                                   Vector2(-2.0, -2.0),
                                   Vector2(-1.0, -2.0),

                                   Vector2(0.0, -3.0),
                                   Vector2(1.0, -2.0),
                                   Vector2(2.0, -2.0),
                                   Vector2(2.0, -1.0)])

        actual = polygon.inner_angels
        expected = [90.0, 225.0,
                    90.0, 225.0,
                    90.0, 225.0,
                    90.0, 225.0,
                    90.0, 225.0,
                    90.0, 225.0,
                    90.0, 225.0,
                    90.0, 225.0]
        self.assertEqual(len(expected), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected[i], actual[i])

        actual = polygon.normal_angels
        expected = [180.0, 22.5,
                    225.0, 337.5,
                    270.0, 292.5,
                    315.0, 247.5,
                    0.0, 202.5,
                    45.0, 157.5,
                    90.0, 112.5,
                    135.0, 67.5]
        self.assertEqual(len(expected), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(math.fmod(expected[i] - actual[i], 360.0), 0.0,
                                   msg='expected: {}, actual: {}, i: {}'.format(expected[i], actual[i], i))

    # ----------------------------------------------------------------------------------------------------------------------
