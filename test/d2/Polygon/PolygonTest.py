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
        context = Context()

        normal_angles = polygon.normal_angles(context)
        nodes = polygon.primary
        rectangles = []
        for i in range(len(nodes)):
            rectangle = Rectangle(width=0.5, depth=0.1)
            rectangle = Translate2D(y=-0.05, child=rectangle)
            rectangle = Rotate2D(angle=normal_angles[i], child=rectangle)
            rectangle = Translate2D(vector=nodes[i], child=rectangle)
            rectangle = Paint(color=Color('red'), child=rectangle)
            rectangles.append(rectangle)

        return Union(children=[polygon] + rectangles)

    # ------------------------------------------------------------------------------------------------------------------
    def test_plain_polygon(self):
        """
        Plain test for a plain polygon.
        """
        context = Context()
        scad = Scad(context=context)

        polygon = Polygon(primary=[Vector2(0.0, 0.0), Vector2(100.0, 0.0), Vector2(130.0, 50.0), Vector2(30.0, 50.0)])
        self.assertFalse(polygon.is_clockwise(context))

        path_actual, path_expected = self.paths()
        scad.run_super_scad(polygon, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_one_hole_polygon(self):
        """
        Plain test for a polygon with one hole.
        """
        context = Context()
        scad = Scad(context=context)

        polygon = Polygon(primary=[Vector2(0.0, 0.0), Vector2(100.0, 0.0), Vector2(0.0, 100.0)],
                          secondary=[Vector2(10.0, 10.0), Vector2(80.0, 10.0), Vector2(10.0, 80.0)],
                          convexity=10)
        self.assertFalse(polygon.is_clockwise(context))

        path_actual, path_expected = self.paths()
        scad.run_super_scad(polygon, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_multi_hole_polygon(self):
        """
        Plain test for a polygon with multiple holes.
        """
        context = Context()
        scad = Scad(context=context)

        polygon = Polygon(primary=[Vector2(0.0, 0.0), Vector2(100.0, 0.0), Vector2(130.0, 50.0), Vector2(30.0, 50.0)],
                          secondaries=[[Vector2(20.0, 20.0), Vector2(40.0, 20.0), Vector2(30.0, 30.0)],
                                       [Vector2(50.0, 20.0), Vector2(60.0, 20.0), Vector2(40.0, 30.0)],
                                       [Vector2(65.0, 10.0), Vector2(80.0, 10.0), Vector2(80.0, 40.0),
                                        Vector2(65.0, 40.0)],
                                       [Vector2(98.0, 10.0), Vector2(115.0, 40.0), Vector2(85.0, 40.0),
                                        Vector2(85.0, 10.0)]])
        self.assertFalse(polygon.is_clockwise(context))

        path_actual, path_expected = self.paths()
        scad.run_super_scad(polygon, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_imperial_metric_polygon(self):
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
    def test_imperial_imperial_polygon(self):
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
    def test_angles1(self):
        """
        Test inner and normal angles.
        """
        context = Context()

        points = [Vector2(0.0, 0.0), Vector2(10.0, 0.0), Vector2(0.0, 10.0)]
        expected_inner_angles = [90.0, 45.0, 45.0]
        expected_normal_angles = [45.0, 157.5, 292.5]

        polygon1 = Polygon(points=points)

        self.assertEqual(3, polygon1.sides)
        self.assertFalse(polygon1.is_clockwise(context))

        # First, inner angles.
        actual = polygon1.inner_angles(context)
        self.assertEqual(len(expected_inner_angles), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected_inner_angles[i], actual[i])

        # Second, normal angles.
        actual = polygon1.normal_angles(context)
        self.assertEqual(len(expected_normal_angles), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected_normal_angles[i], actual[i])

        points = points.copy()
        points.reverse()
        polygon2 = Polygon(points=points)

        self.assertEqual(3, polygon2.sides)
        self.assertTrue(polygon2.is_clockwise)

        # First, normal angles.
        actual = polygon2.normal_angles(context)
        expected_normal_angles.reverse()
        self.assertEqual(len(expected_normal_angles), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected_normal_angles[i], actual[i])

        # Second, inner angles.
        actual = polygon2.inner_angles(context)
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
    def test_angles2(self):
        """
        Test inner angles.
        """
        context = Context()

        points = [Vector2(-10.0, 0.0), Vector2(10.0, 0.0), Vector2(0.0, 10.0 * math.sqrt(3.0))]
        expected_inner_angles = [60.0, 60.0, 60.0]
        expected_normal_angles = [30.0, 150.0, 270.0]

        polygon1 = Polygon(points=points)

        self.assertEqual(3, polygon1.sides)
        self.assertFalse(polygon1.is_clockwise(context))

        actual = polygon1.inner_angles(context)
        self.assertEqual(len(expected_inner_angles), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected_inner_angles[i], actual[i])

        actual = polygon1.normal_angles(context)
        self.assertEqual(len(expected_normal_angles), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected_normal_angles[i], actual[i])

        points = points.copy()
        points.reverse()
        polygon2 = Polygon(points=points)

        self.assertEqual(3, polygon2.sides)
        self.assertTrue(polygon2.is_clockwise)

        actual = polygon2.inner_angles(context)
        expected_inner_angles.reverse()
        self.assertEqual(len(expected_inner_angles), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected_inner_angles[i], actual[i])

        actual = polygon2.normal_angles(context)
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
    def test_angles3(self):
        """
        Test inner angles.
        """
        context = Context()

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

        self.assertEqual(16, polygon1.sides)
        self.assertFalse(polygon1.is_clockwise(context))

        actual = polygon1.inner_angles(context)
        self.assertEqual(len(expected_inner_angles), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected_inner_angles[i], actual[i])

        actual = polygon1.normal_angles(context)
        self.assertEqual(len(expected_normal_angles), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected_normal_angles[i], actual[i])

        points = points.copy()
        points.reverse()
        polygon2 = Polygon(points=points)

        self.assertEqual(16, polygon2.sides)
        self.assertTrue(polygon2.is_clockwise)

        actual = polygon2.inner_angles(context)
        expected_inner_angles.reverse()
        self.assertEqual(len(expected_inner_angles), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected_inner_angles[i], actual[i])

        actual = polygon2.normal_angles(context)
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

    # ------------------------------------------------------------------------------------------------------------------
    def test_angles4(self):
        """
        Test inner angles.
        """
        context = Context()

        points = [Vector2(0, 20.0), Vector2(10.0, 0.0), Vector2(0.0, 10.0), Vector2(-10.0, 0.0)]
        expected_inner_angles = [53.1301, 18.4349, 270.0, 18.4349]
        expected_normal_angles = [270.0, 125.7825, 90.0, 54.2175]

        polygon1 = Polygon(points=points)

        self.assertEqual(4, polygon1.sides)
        self.assertTrue(polygon1.is_clockwise(context))

        actual = polygon1.inner_angles(context)
        self.assertEqual(len(expected_inner_angles), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected_inner_angles[i], actual[i], places=4)

        actual = polygon1.normal_angles(context)
        self.assertEqual(len(expected_normal_angles), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected_normal_angles[i], actual[i], places=4)

        points = points.copy()
        points.reverse()
        polygon2 = Polygon(points=points)

        self.assertEqual(4, polygon2.sides)
        self.assertFalse(polygon2.is_clockwise(context))

        actual = polygon2.inner_angles(context)
        expected_inner_angles.reverse()
        self.assertEqual(len(expected_inner_angles), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected_inner_angles[i], actual[i], places=4)

        actual = polygon2.normal_angles(context)
        expected_normal_angles.reverse()
        self.assertEqual(len(expected_normal_angles), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected_normal_angles[i], actual[i], places=4)

        path_actual, path_expected = self.paths()
        scad = Scad(context=Context())
        polygons = Union(children=[Translate2D(x=-11, child=self.normal_angle_arrows(polygon1)),
                                   Translate2D(x=11, child=self.normal_angle_arrows(polygon2))])
        scad.run_super_scad(polygons, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_angles5(self):
        """
        Test inner angles.
        """
        context = Context()

        points = [Vector2(0, 4.999999999999), Vector2(10.0, 0.0), Vector2(-10.0, 0.0)]
        expected_inner_angles = [126.8699, 26.5651, 26.5651]
        expected_normal_angles = [270.0, 166.7175, 13.2825]

        polygon1 = Polygon(points=points)

        self.assertEqual(3, polygon1.sides)
        self.assertTrue(polygon1.is_clockwise(context))

        actual = polygon1.inner_angles(context)
        self.assertEqual(len(expected_inner_angles), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected_inner_angles[i], actual[i], places=4)

        actual = polygon1.normal_angles(context)
        self.assertEqual(len(expected_normal_angles), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected_normal_angles[i], actual[i], places=4)

        points = points.copy()
        points.reverse()
        polygon2 = Polygon(points=points)

        self.assertEqual(3, polygon2.sides)
        self.assertFalse(polygon2.is_clockwise(context))

        actual = polygon2.inner_angles(context)
        expected_inner_angles.reverse()
        self.assertEqual(len(expected_inner_angles), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected_inner_angles[i], actual[i], places=4)

        actual = polygon2.normal_angles(context)
        expected_normal_angles.reverse()
        self.assertEqual(len(expected_normal_angles), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected_normal_angles[i], actual[i], places=4)

        path_actual, path_expected = self.paths()
        scad = Scad(context=Context())
        polygons = Union(children=[Translate2D(x=-11, child=self.normal_angle_arrows(polygon1)),
                                   Translate2D(x=11, child=self.normal_angle_arrows(polygon2))])
        scad.run_super_scad(polygons, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_angles_collinear_points(self):
        """
        Test inner angles with collinear points.
        """
        context = Context()

        points = [Vector2(-10, 0.0),
                  Vector2(-10, 10),
                  Vector2(0, 10),
                  Vector2(10, 10),
                  Vector2(10, 0),
                  Vector2(10, -10),
                  Vector2(0, -10),
                  Vector2(-10, -10)]
        expected_inner_angles = [180.0, 90.0, 180.0, 90.0, 180.0, 90.0, 180.0, 90.0]
        expected_normal_angles = [0.0, 315.0, 270.0, 225.0, 180.0, 135.0, 90.0, 45.0]

        polygon1 = Polygon(points=points)

        self.assertEqual(8, polygon1.sides)
        self.assertTrue(polygon1.is_clockwise(context))

        actual = polygon1.inner_angles(context)
        self.assertEqual(len(expected_inner_angles), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected_inner_angles[i], actual[i], places=4)

        actual = polygon1.normal_angles(context)
        self.assertEqual(len(expected_normal_angles), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected_normal_angles[i], actual[i], places=4)

        points = points.copy()
        points.reverse()
        polygon2 = Polygon(points=points)

        self.assertEqual(8, polygon2.sides)
        self.assertFalse(polygon2.is_clockwise(context))

        actual = polygon2.inner_angles(context)
        expected_inner_angles.reverse()
        self.assertEqual(len(expected_inner_angles), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected_inner_angles[i], actual[i], places=4)

        actual = polygon2.normal_angles(context)
        expected_normal_angles.reverse()
        self.assertEqual(len(expected_normal_angles), len(actual))
        for i in range(len(actual)):
            self.assertAlmostEqual(expected_normal_angles[i], actual[i], places=4)

        path_actual, path_expected = self.paths()
        scad = Scad(context=Context())
        polygons = Union(children=[Translate2D(x=-11, child=self.normal_angle_arrows(polygon1)),
                                   Translate2D(x=11, child=self.normal_angle_arrows(polygon2))])
        scad.run_super_scad(polygons, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_nodes_to_close(self):
        """
        Test polygon with nodes to close to reliable computation of the separation between line segments and nodes.
        """
        context = Context()
        scad = Scad(context=Context())

        points = [Vector2(0.0, 0.0), Vector2(1.0, 0.0), Vector2(1.0, 1.0), Vector2(0.0, 1.0)]
        polygon1 = Polygon(points=points, delta=2.0)

        self.assertRaises(ValueError, lambda: Color(polygon1.is_clockwise(context)))

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_one_side1(self):
        """
        Extend one side by eps.
        """
        points = [Vector2(0, 20.0), Vector2(10.0, 0.0), Vector2(0.0, 10.0), Vector2(-10.0, 0.0)]

        context = Context(eps=0.5)
        scad = Scad(context=context)

        polygon1 = Paint(color=Color('red'),
                         child=Polygon(points=points, extend_sides_by_eps={1}))
        polygon2 = Polygon(points=points)
        union = Union(children=[polygon1, polygon2])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_one_side1_counterclockwise(self):
        """
        Extend one side by eps.
        """
        points = [Vector2(0, 20.0), Vector2(10.0, 0.0), Vector2(0.0, 10.0), Vector2(-10.0, 0.0)]
        points.reverse()

        context = Context(eps=0.5)
        scad = Scad(context=context)

        polygon1 = Paint(color=Color('red'),
                         child=Polygon(points=points, extend_sides_by_eps={1}))
        polygon2 = Polygon(points=points)
        union = Union(children=[polygon1, polygon2])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_one_side2(self):
        """
        Extend one side by eps.
        """
        points = [Vector2(0, 20.0), Vector2(10.0, 0.0), Vector2(0.0, 10.0), Vector2(-10.0, 0.0)]

        context = Context(eps=0.5)
        scad = Scad(context=context)

        polygon1 = Paint(color=Color('red'),
                         child=Polygon(points=points, extend_sides_by_eps={2}))
        polygon2 = Polygon(points=points)
        union = Union(children=[polygon1, polygon2])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_one_side2_counterclockwise(self):
        """
        Extend one side by eps.
        """
        points = [Vector2(0, 20.0), Vector2(10.0, 0.0), Vector2(0.0, 10.0), Vector2(-10.0, 0.0)]
        points.reverse()

        context = Context(eps=0.5)
        scad = Scad(context=context)

        polygon1 = Paint(color=Color('red'),
                         child=Polygon(points=points, extend_sides_by_eps={2}))
        polygon2 = Polygon(points=points)
        union = Union(children=[polygon1, polygon2])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_two_sides1(self):
        """
        Extend two adjacent sides by eps.
        """
        points = [Vector2(0, 20.0), Vector2(10.0, 0.0), Vector2(0.0, 10.0), Vector2(-10.0, 0.0)]

        context = Context(eps=0.5)
        scad = Scad(context=context)

        polygon1 = Paint(color=Color('red'),
                         child=Polygon(points=points, extend_sides_by_eps={1, 2}))
        polygon2 = Polygon(points=points)
        union = Union(children=[polygon1, polygon2])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_two_sides1_counterclockwise(self):
        """
        Extend two adjacent sides by eps.
        """
        points = [Vector2(0, 20.0), Vector2(10.0, 0.0), Vector2(0.0, 10.0), Vector2(-10.0, 0.0)]
        points.reverse()

        context = Context(eps=0.5)
        scad = Scad(context=context)

        polygon1 = Paint(color=Color('red'),
                         child=Polygon(points=points, extend_sides_by_eps={1, 2}))
        polygon2 = Polygon(points=points)
        union = Union(children=[polygon1, polygon2])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_two_sides2(self):
        """
        Extend two adjacent sides by eps.
        """
        points = [Vector2(0, 20.0), Vector2(10.0, 0.0), Vector2(0.0, 10.0), Vector2(-10.0, 0.0)]

        context = Context(eps=0.5)
        scad = Scad(context=context)

        polygon1 = Paint(color=Color('red'),
                         child=Polygon(points=points, extend_sides_by_eps={0, 3}))
        polygon2 = Polygon(points=points)
        union = Union(children=[polygon1, polygon2])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_two_sides2_counterclockwise(self):
        """
        Extend two adjacent sides by eps.
        """
        points = [Vector2(0, 20.0), Vector2(10.0, 0.0), Vector2(0.0, 10.0), Vector2(-10.0, 0.0)]
        points.reverse()

        context = Context(eps=0.5)
        scad = Scad(context=context)

        polygon1 = Paint(color=Color('red'),
                         child=Polygon(points=points, extend_sides_by_eps={0, 3}))
        polygon2 = Polygon(points=points)
        union = Union(children=[polygon1, polygon2])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_two_sides2_shallow(self):
        """
        Extend two adjacent sides with a shallow angle by eps.
        """
        points = [Vector2(0, 4.0), Vector2(10.0, 0.0), Vector2(-10.0, 0.0)]

        context = Context(eps=0.5)
        scad = Scad(context=context)

        polygon1 = Paint(color=Color('red'),
                         child=Polygon(points=points, extend_sides_by_eps={0, 2}))
        polygon2 = Polygon(points=points)
        union = Union(children=[polygon1, polygon2])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_all_sides(self):
        """
        Extend all sides by eps.
        """
        points = [Vector2(0, 20.0), Vector2(10.0, 0.0), Vector2(0.0, 10.0), Vector2(-10.0, 0.0)]

        context = Context(eps=0.5)
        scad = Scad(context=context)

        polygon1 = Paint(color=Color('red'),
                         child=Polygon(points=points, extend_sides_by_eps=True))
        polygon2 = Polygon(points=points)
        union = Union(children=[polygon1, polygon2])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_all_sides_counterclockwise(self):
        """
        Extend all sides by eps.
        """
        points = [Vector2(0, 20.0), Vector2(10.0, 0.0), Vector2(0.0, 10.0), Vector2(-10.0, 0.0)]
        points.reverse()

        context = Context(eps=0.5)
        scad = Scad(context=context)

        polygon1 = Paint(color=Color('red'),
                         child=Polygon(points=points, extend_sides_by_eps=True))
        polygon2 = Polygon(points=points)
        union = Union(children=[polygon1, polygon2])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
