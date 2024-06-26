from ScadTestCase import ScadTestCase
from super_scad.d3.Sphere import Sphere
from super_scad.Scad import Scad
from super_scad.transformation.Paint import Paint
from super_scad.type.Color import Color
from super_scad.Unit import Unit


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

        scad = Scad(unit=Unit.MM)
        paint = Paint(color=Color(color='fuchsia'), child=Sphere(radius=10.0))

        scad.run_super_scad(paint, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
