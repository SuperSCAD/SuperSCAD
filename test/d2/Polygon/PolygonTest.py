import math

from d2.Polygon.ImperialUnitPolygon import ImperialUnitPolygon
from ScadTestCase import ScadTestCase
from super_scad.boolean.Union import Union
from super_scad.d2.Polygon import Polygon
from super_scad.d2.Rectangle import Rectangle
from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.scad.Unit import Unit
from super_scad.transformation.Paint import Paint
from super_scad.transformation.Rotate2D import Rotate2D
from super_scad.transformation.Translate2D import Translate2D
from super_scad.type.Color import Color
from super_scad.type.Vector2 import Vector2


class PolygonTestCase(ScadTestCase):
    """
    Testcases for polygons.
    """

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def normal_angle_arrows(polygon: Polygon) -> ScadWidget:
        """
        Add arrows to a polygon.
        """
        normal_angel = polygon.normal_angles
        nodes = polygon.primary
        rectangles = []
        for i in range(len(nodes)):
            rectangle = Rectangle(width=0.5, depth=0.1)
            rectangle = Translate2D(y=-0.05, child=rectangle)
            rectangle = Rotate2D(angle=normal_angel[i], child=rectangle)
            rectangle = Translate2D(vector=nodes[i], child=rectangle)
            rectangle = Paint(color=Color('red'), child=rectangle)
            rectangles.append(rectangle)

        return Union(children=[polygon] + rectangles)

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
    def testAngles1(self):
        """
        Test inner and normal angles.
        """
        points = [Vector2(0.0, 0.0), Vector2(10.0, 0.0), Vector2(0.0, 10.0)]
        expected_inner_angles = [90.0, 45.0, 45.0]
        expected_normal_angles = [45.0, 157.5, 292.5]

        polygon1 = Polygon(points=points)

        self.assertEqual(3, polygon1.sides)

        # First, inner angles.
        actual = polygon1.inner_angles
        self.assertEqual(len(expected_inner_angles), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected_inner_angles[i], actual[i])

        # Second, normal angles.
        actual = polygon1.normal_angles
        self.assertEqual(len(expected_normal_angles), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected_normal_angles[i], actual[i])

        points = points.copy()
        points.reverse()
        polygon2 = Polygon(points=points)

        self.assertEqual(3, polygon2.sides)

        # First, normal angles.
        actual = polygon2.normal_angles
        expected_normal_angles.reverse()
        self.assertEqual(len(expected_normal_angles), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected_normal_angles[i], actual[i])

        # Second, inner angles.
        actual = polygon2.inner_angles
        expected_inner_angles.reverse()
        self.assertEqual(len(expected_inner_angles), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected_inner_angles[i], actual[i])

        path_actual, path_expected = self.paths()
        scad = Scad(context=Context())
        polygons = Union(children=[Translate2D(x=-11, child=self.normal_angle_arrows(polygon1)),
                                   Translate2D(x=1, child=self.normal_angle_arrows(polygon2))])
        scad.run_super_scad(polygons, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testAngles2(self):
        """
        Test inner angles.
        """
        points = [Vector2(-10.0, 0.0), Vector2(10.0, 0.0), Vector2(0.0, 10.0 * math.sqrt(3.0))]
        expected_inner_angles = [60.0, 60.0, 60.0]
        expected_normal_angles = [30.0, 150.0, 270.0]

        polygon1 = Polygon(points=points)

        actual = polygon1.inner_angles
        self.assertEqual(len(expected_inner_angles), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected_inner_angles[i], actual[i])

        actual = polygon1.normal_angles
        self.assertEqual(len(expected_normal_angles), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected_normal_angles[i], actual[i])

        points = points.copy()
        points.reverse()
        polygon2 = Polygon(points=points)

        actual = polygon2.inner_angles
        expected_inner_angles.reverse()
        self.assertEqual(len(expected_inner_angles), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected_inner_angles[i], actual[i])

        actual = polygon2.normal_angles
        expected_normal_angles.reverse()
        self.assertEqual(len(expected_normal_angles), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected_normal_angles[i], actual[i])

        path_actual, path_expected = self.paths()
        scad = Scad(context=Context())
        polygons = Union(children=[Translate2D(x=-11, child=self.normal_angle_arrows(polygon1)),
                                   Translate2D(x=11, child=self.normal_angle_arrows(polygon2))])
        scad.run_super_scad(polygons, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testAngles3(self):
        """
        Test inner angles.
        """
        points = [Vector2(3.0, 0.0),
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
                  Vector2(2.0, -1.0)]
        expected_inner_angles = [90.0, 225.0,
                                 90.0, 225.0,
                                 90.0, 225.0,
                                 90.0, 225.0,
                                 90.0, 225.0,
                                 90.0, 225.0,
                                 90.0, 225.0,
                                 90.0, 225.0]
        expected_normal_angles = [180.0, 202.5,
                                  225.0, 247.5,
                                  270.0, 292.5,
                                  315.0, 337.5,
                                  0.0, 22.5,
                                  45.0, 67.5,
                                  90.0, 112.5,
                                  135.0, 157.5]

        polygon1 = Polygon(points=points)

        actual = polygon1.inner_angles
        self.assertEqual(len(expected_inner_angles), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected_inner_angles[i], actual[i])

        actual = polygon1.normal_angles
        self.assertEqual(len(expected_normal_angles), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected_normal_angles[i], actual[i])

        points = points.copy()
        points.reverse()
        polygon2 = Polygon(points=points)

        actual = polygon2.inner_angles
        expected_inner_angles.reverse()
        self.assertEqual(len(expected_inner_angles), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected_inner_angles[i], actual[i])

        actual = polygon2.normal_angles
        expected_normal_angles.reverse()

        self.assertEqual(len(expected_normal_angles), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected_normal_angles[i], actual[i])

        path_actual, path_expected = self.paths()
        scad = Scad(context=Context())
        polygons = Union(children=[Translate2D(x=-4, child=self.normal_angle_arrows(polygon1)),
                                   Translate2D(x=4, child=self.normal_angle_arrows(polygon2))])
        scad.run_super_scad(polygons, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
