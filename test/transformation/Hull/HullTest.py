from ScadTestCase import ScadTestCase
from super_scad.d2.Circle import Circle
from super_scad.transformation.Hull import Hull
from super_scad.transformation.Translate2D import Translate2D


class HullTest(ScadTestCase):
    """
    test case for hull.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_hull(self):
        """
        The test case for hull.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        hull = Hull(children=[Translate2D(x=15, y=10, child=Circle(radius=10)),
                              Circle(radius=10)])

        scad.run_super_scad(hull, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
