from ScadTestCase import ScadTestCase
from super_scad.d3.Sphere import Sphere
from super_scad.transformation.Paint import Paint
from super_scad.type.Color import Color


class PaintTest(ScadTestCase):
    """
    test case for paint.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_paint(self):
        """
        The test case for paint.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        paint = Paint(color=Color('fuchsia'), child=Sphere(radius=10.0))

        scad.run_super_scad(paint, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_paint_color_as_str(self):
        """
        The test case for paint with color given as str.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        paint = Paint(color='fuchsia', child=Sphere(radius=10.0))

        scad.run_super_scad(paint, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_paint_no_color(self):
        """
        The test case for paint with no color.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        paint = Paint(child=Sphere(radius=10.0))

        scad.run_super_scad(paint, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
