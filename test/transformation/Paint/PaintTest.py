from ScadTestCase import ScadTestCase
from super_scad.d3.Sphere import Sphere
from super_scad.transformation.Paint import Paint
from super_scad.type.Color import Color


class PaintTest(ScadTestCase):
    """
    test case for paint.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testPaint(self):
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

# ----------------------------------------------------------------------------------------------------------------------
