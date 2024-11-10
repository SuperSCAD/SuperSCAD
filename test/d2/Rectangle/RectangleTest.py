from ScadTestCase import ScadTestCase
from super_scad.d2.Rectangle import Rectangle
from super_scad.scad.Context import Context
from super_scad.scad.Unit import Unit
from super_scad.type.Vector2 import Vector2
from test.d2.Rectangle.ImperialUnitRectangle import ImperialUnitRectangle


class RectangleTestCase(ScadTestCase):
    """
    Testcases for rectangles.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_rectangle_by_size(self):
        """
        Test for a rectangle defined by size.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        rectangle = Rectangle(size=Vector2(20, 10))

        self.assertAlmostEqual(20.0, rectangle.width)
        self.assertAlmostEqual(10.0, rectangle.depth)
        self.assertAlmostEqual(20.0, rectangle.size.x)
        self.assertAlmostEqual(10.0, rectangle.size.y)
        self.assertFalse(rectangle.center)
        self.assertIsNone(rectangle.convexity)

        scad.run_super_scad(rectangle, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_rectangle_by_width_and_depth(self):
        """
        Test for a rectangle defined by width and depth.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        rectangle = Rectangle(size=Vector2(20, 10), center=True)

        self.assertAlmostEqual(20.0, rectangle.width)
        self.assertAlmostEqual(10.0, rectangle.depth)
        self.assertAlmostEqual(20.0, rectangle.size.x)
        self.assertAlmostEqual(10.0, rectangle.size.y)
        self.assertTrue(rectangle.center)
        self.assertIsNone(rectangle.convexity)

        scad.run_super_scad(rectangle, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_imperial_metric_rectangle(self):
        """
        Test for an imperial unit rectangle in metric units.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        rectangle = ImperialUnitRectangle()
        scad.run_super_scad(rectangle, path_actual)

        self.assertAlmostEqual(50.8, rectangle.imperial_rectangle.width)
        self.assertAlmostEqual(25.4, rectangle.imperial_rectangle.depth)
        self.assertAlmostEqual(50.8, rectangle.imperial_rectangle.size.x)
        self.assertAlmostEqual(25.4, rectangle.imperial_rectangle.size.y)
        self.assertFalse(rectangle.imperial_rectangle.center)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_imperial_imperial_rectangle(self):
        """
        Test for an imperial unit rectangle in imperial units.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad(unit_length_final=Unit.INCH)
        rectangle = ImperialUnitRectangle()
        scad.run_super_scad(rectangle, path_actual)

        self.assertAlmostEqual(2.0, rectangle.imperial_rectangle.width)
        self.assertAlmostEqual(1.0, rectangle.imperial_rectangle.depth)
        self.assertAlmostEqual(2.0, rectangle.imperial_rectangle.size.x)
        self.assertAlmostEqual(1.0, rectangle.imperial_rectangle.size.y)
        self.assertFalse(rectangle.imperial_rectangle.center)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_angles(self):
        """
        Test the angles of square.
        """
        context = Context()
        expected_nodes = [Vector2(0.0, 0.0), Vector2(0.0, 10.0), Vector2(20.0, 10.0), Vector2(20.0, 0.0)]
        expected_inner_angles = [90.0, 90.0, 90.0, 90.0]
        expected_normal_angles = [45.0, 315.0, 225.0, 135.0]

        square = Rectangle(width=20.0, depth=10.0)
        self.assertTrue(square.is_clockwise(context))

        nodes = square.nodes
        inner_angles = square.inner_angles(context)
        normal_angles = square.normal_angles(context)
        for index in range(len(nodes)):
            self.assertAlmostEqual(expected_nodes[index].x, nodes[index].x)
            self.assertAlmostEqual(expected_nodes[index].y, nodes[index].y)
            self.assertAlmostEqual(expected_inner_angles[index], inner_angles[index])
            self.assertAlmostEqual(expected_normal_angles[index], normal_angles[index])

# ----------------------------------------------------------------------------------------------------------------------
