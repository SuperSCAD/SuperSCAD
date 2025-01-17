from ScadTestCase import ScadTestCase
from super_scad.d2.Square import Square
from super_scad.transformation.Rotate2D import Rotate2D


class Rotate2DTest(ScadTestCase):
    """
    Test case for Rotate2D.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_rotate(self):
        """
        Test case for Rotate2D.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()

        rotate = Rotate2D(angle=45.0, child=Square(size=10.0))

        self.assertAlmostEqual(rotate.angle, 45.0)

        scad.run_super_scad(rotate, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_no_rotate(self):
        """
        Test case for Rotate2D with angle.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()

        rotate = Rotate2D(child=Square(size=10.0))

        self.assertAlmostEqual(rotate.angle, 0.0)

        scad.run_super_scad(rotate, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
