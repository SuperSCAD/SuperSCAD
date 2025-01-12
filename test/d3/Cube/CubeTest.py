from ScadTestCase import ScadTestCase
from super_scad.boolean.Union import Union
from super_scad.d3.Cube import Cube
from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad.scad.Unit import Unit
from super_scad.transformation.Paint import Paint
from test.d3.Cube.ImperialUnitCube import ImperialUnitCube


class CubeTestCase(ScadTestCase):
    """
    Testcases for cubes.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_plain_cube(self):
        """
        Plain test for a cube.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        cube = Cube(size=10)

        self.assertAlmostEqual(10.0, cube.size)
        self.assertFalse(cube.center)

        scad.run_super_scad(cube, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_centered_cube(self):
        """
        Plain test for a centered cube.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        cube = Cube(size=10, center=True)

        self.assertAlmostEqual(10.0, cube.size)
        self.assertTrue(cube.center)

        scad.run_super_scad(cube, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_imperial_metric_cube(self):
        """
        Test for an imperial unit cube in metric units.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        cube = ImperialUnitCube()
        scad.run_super_scad(cube, path_actual)

        # self.assertAlmostEqual(25.4, cube.imperial_cube.size)
        self.assertFalse(cube.imperial_cube.center)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_imperial_imperial_cube(self):
        """
        Test for an imperial unit cube in imperial units.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad(unit_length_final=Unit.INCH)
        cube = ImperialUnitCube()
        scad.run_super_scad(cube, path_actual)

        self.assertAlmostEqual(1.0, cube.imperial_cube.size)
        self.assertFalse(cube.imperial_cube.center)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_centered_extend_by_eps_left(self):
        """
        Test for a centered cube extended by eps left.
        """
        scad = Scad(context=Context(eps=1.0))

        cube = Cube(size=10,
                    center=True,
                    extend_by_eps_left=True)

        self.assertAlmostEqual(10.0, cube.size)
        self.assertTrue(cube.center)

        cube = Paint(color='red', child=cube)
        mask = Cube(size=10,
                    center=True,
                    extend_by_eps_front=True,
                    extend_by_eps_back=True,
                    extend_by_eps_top=True,
                    extend_by_eps_bottom=True,
                    extend_by_eps_left=False,
                    extend_by_eps_right=True)
        diff = Union(children=[cube, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_centered_extend_by_eps_right(self):
        """
        Test for a centered cube extended by eps right.
        """
        scad = Scad(context=Context(eps=1.0))

        cube = Cube(size=10,
                    center=True,
                    extend_by_eps_right=True)

        self.assertAlmostEqual(10.0, cube.size)
        self.assertTrue(cube.center)

        cube = Paint(color='red', child=cube)
        mask = Cube(size=10,
                    center=True,
                    extend_by_eps_front=True,
                    extend_by_eps_back=True,
                    extend_by_eps_top=True,
                    extend_by_eps_bottom=True,
                    extend_by_eps_left=True,
                    extend_by_eps_right=False)
        diff = Union(children=[cube, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_centered_extend_by_eps_left_right(self):
        """
        Test for a centered cube extended by eps left and right.
        """
        scad = Scad(context=Context(eps=1.0))

        cube = Cube(size=10,
                    center=True,
                    extend_by_eps_left=True,
                    extend_by_eps_right=True)

        self.assertAlmostEqual(10.0, cube.size)
        self.assertTrue(cube.center)

        cube = Paint(color='red', child=cube)
        mask = Cube(size=10,
                    center=True,
                    extend_by_eps_front=True,
                    extend_by_eps_back=True,
                    extend_by_eps_top=True,
                    extend_by_eps_bottom=True,
                    extend_by_eps_left=False,
                    extend_by_eps_right=False)
        diff = Union(children=[cube, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_centered_extend_by_eps_top(self):
        """
        Test for a centered cube extended by eps top.
        """
        scad = Scad(context=Context(eps=1.0))

        cube = Cube(size=10,
                    center=True,
                    extend_by_eps_top=True)

        self.assertAlmostEqual(10.0, cube.size)
        self.assertTrue(cube.center)

        cube = Paint(color='red', child=cube)
        mask = Cube(size=10,
                    center=True,
                    extend_by_eps_front=True,
                    extend_by_eps_back=True,
                    extend_by_eps_top=False,
                    extend_by_eps_bottom=True,
                    extend_by_eps_left=True,
                    extend_by_eps_right=True)
        diff = Union(children=[cube, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_centered_extend_by_eps_bottom(self):
        """
        Test for a centered cube extended by eps bottom.
        """
        scad = Scad(context=Context(eps=1.0))

        cube = Cube(size=10,
                    center=True,
                    extend_by_eps_bottom=True)

        self.assertAlmostEqual(10.0, cube.size)
        self.assertTrue(cube.center)

        cube = Paint(color='red', child=cube)
        mask = Cube(size=10,
                    center=True,
                    extend_by_eps_front=True,
                    extend_by_eps_back=True,
                    extend_by_eps_top=True,
                    extend_by_eps_bottom=False,
                    extend_by_eps_left=True,
                    extend_by_eps_right=True)
        diff = Union(children=[cube, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_centered_extend_by_eps_top_bottom(self):
        """
        Test for a centered cube extended by eps top and bottom.
        """
        scad = Scad(context=Context(eps=1.0))

        cube = Cube(size=10,
                    center=True,
                    extend_by_eps_top=True,
                    extend_by_eps_bottom=True)

        self.assertAlmostEqual(10.0, cube.size)
        self.assertTrue(cube.center)

        cube = Paint(color='red', child=cube)
        mask = Cube(size=10,
                    center=True,
                    extend_by_eps_front=True,
                    extend_by_eps_back=True,
                    extend_by_eps_top=False,
                    extend_by_eps_bottom=False,
                    extend_by_eps_left=True,
                    extend_by_eps_right=True)
        diff = Union(children=[cube, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_centered_extend_by_eps_front(self):
        """
        Test for a centered cube extended by eps front.
        """
        scad = Scad(context=Context(eps=1.0))

        cube = Cube(size=10,
                    center=True,
                    extend_by_eps_front=True)

        self.assertAlmostEqual(10.0, cube.size)
        self.assertTrue(cube.center)

        cube = Paint(color='red', child=cube)
        mask = Cube(size=10,
                    center=True,
                    extend_by_eps_front=False,
                    extend_by_eps_back=True,
                    extend_by_eps_top=True,
                    extend_by_eps_bottom=True,
                    extend_by_eps_left=True,
                    extend_by_eps_right=True)
        diff = Union(children=[cube, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_centered_extend_by_eps_back(self):
        """
        Test for a centered cube extended by eps back.
        """
        scad = Scad(context=Context(eps=1.0))

        cube = Cube(size=10,
                    center=True,
                    extend_by_eps_back=True)

        self.assertAlmostEqual(10.0, cube.size)
        self.assertTrue(cube.center)

        cube = Paint(color='red', child=cube)
        mask = Cube(size=10,
                    center=True,
                    extend_by_eps_front=True,
                    extend_by_eps_back=False,
                    extend_by_eps_top=True,
                    extend_by_eps_bottom=True,
                    extend_by_eps_left=True,
                    extend_by_eps_right=True)
        diff = Union(children=[cube, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_centered_extend_by_eps_front_back(self):
        """
        Test for a centered cube extended by eps front and back.
        """
        scad = Scad(context=Context(eps=1.0))

        cube = Cube(size=10,
                    center=True,
                    extend_by_eps_front=True,
                    extend_by_eps_back=True)

        self.assertAlmostEqual(10.0, cube.size)
        self.assertTrue(cube.center)

        cube = Paint(color='red', child=cube)
        mask = Cube(size=10,
                    center=True,
                    extend_by_eps_front=False,
                    extend_by_eps_back=False,
                    extend_by_eps_top=True,
                    extend_by_eps_bottom=True,
                    extend_by_eps_left=True,
                    extend_by_eps_right=True)
        diff = Union(children=[cube, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_centered_extend_by_eps_left_front_bottom(self):
        """
        Test for a centered cube extended by eps left, front, and bottom.
        """
        scad = Scad(context=Context(eps=1.0))

        cube = Cube(size=10,
                    center=True,
                    extend_by_eps_front=True,
                    extend_by_eps_bottom=True,
                    extend_by_eps_left=True)

        self.assertAlmostEqual(10.0, cube.size)
        self.assertTrue(cube.center)

        cube = Paint(color='red', child=cube)
        mask = Cube(size=10,
                    center=True,
                    extend_by_eps_front=False,
                    extend_by_eps_back=True,
                    extend_by_eps_top=True,
                    extend_by_eps_bottom=False,
                    extend_by_eps_left=False,
                    extend_by_eps_right=True)
        diff = Union(children=[cube, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_centered_extend_by_eps_right_back_top(self):
        """
        Test for a centered cube extended by eps right, back, and top.
        """
        scad = Scad(context=Context(eps=1.0))

        cube = Cube(size=10,
                    center=True,
                    extend_by_eps_back=True,
                    extend_by_eps_top=True,
                    extend_by_eps_right=True)

        self.assertAlmostEqual(10.0, cube.size)
        self.assertTrue(cube.center)

        cube = Paint(color='red', child=cube)
        mask = Cube(size=10,
                    center=True,
                    extend_by_eps_front=True,
                    extend_by_eps_back=False,
                    extend_by_eps_top=False,
                    extend_by_eps_bottom=True,
                    extend_by_eps_left=True,
                    extend_by_eps_right=False)
        diff = Union(children=[cube, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_left(self):
        """
        Test for a centered cube extended by eps left.
        """
        scad = Scad(context=Context(eps=1.0))

        cube = Cube(size=10,
                    extend_by_eps_left=True)

        self.assertAlmostEqual(10.0, cube.size)
        self.assertFalse(cube.center)

        cube = Paint(color='red', child=cube)
        mask = Cube(size=10,
                    extend_by_eps_front=True,
                    extend_by_eps_back=True,
                    extend_by_eps_top=True,
                    extend_by_eps_bottom=True,
                    extend_by_eps_left=False,
                    extend_by_eps_right=True)
        diff = Union(children=[cube, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_right(self):
        """
        Test for a centered cube extended by eps right.
        """
        scad = Scad(context=Context(eps=1.0))

        cube = Cube(size=10,
                    extend_by_eps_right=True)

        self.assertAlmostEqual(10.0, cube.size)
        self.assertFalse(cube.center)

        cube = Paint(color='red', child=cube)
        mask = Cube(size=10,
                    extend_by_eps_front=True,
                    extend_by_eps_back=True,
                    extend_by_eps_top=True,
                    extend_by_eps_bottom=True,
                    extend_by_eps_left=True,
                    extend_by_eps_right=False)
        diff = Union(children=[cube, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_left_right(self):
        """
        Test for a centered cube extended by eps left and right.
        """
        scad = Scad(context=Context(eps=1.0))

        cube = Cube(size=10,
                    extend_by_eps_left=True,
                    extend_by_eps_right=True)

        self.assertAlmostEqual(10.0, cube.size)
        self.assertFalse(cube.center)

        cube = Paint(color='red', child=cube)
        mask = Cube(size=10,
                    extend_by_eps_front=True,
                    extend_by_eps_back=True,
                    extend_by_eps_top=True,
                    extend_by_eps_bottom=True,
                    extend_by_eps_left=False,
                    extend_by_eps_right=False)
        diff = Union(children=[cube, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_top(self):
        """
        Test for a centered cube extended by eps top.
        """
        scad = Scad(context=Context(eps=1.0))

        cube = Cube(size=10,
                    extend_by_eps_top=True)

        self.assertAlmostEqual(10.0, cube.size)
        self.assertFalse(cube.center)

        cube = Paint(color='red', child=cube)
        mask = Cube(size=10,
                    extend_by_eps_front=True,
                    extend_by_eps_back=True,
                    extend_by_eps_top=False,
                    extend_by_eps_bottom=True,
                    extend_by_eps_left=True,
                    extend_by_eps_right=True)
        diff = Union(children=[cube, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_bottom(self):
        """
        Test for a centered cube extended by eps bottom.
        """
        scad = Scad(context=Context(eps=1.0))

        cube = Cube(size=10,
                    extend_by_eps_bottom=True)

        self.assertAlmostEqual(10.0, cube.size)
        self.assertFalse(cube.center)

        cube = Paint(color='red', child=cube)
        mask = Cube(size=10,
                    extend_by_eps_front=True,
                    extend_by_eps_back=True,
                    extend_by_eps_top=True,
                    extend_by_eps_bottom=False,
                    extend_by_eps_left=True,
                    extend_by_eps_right=True)
        diff = Union(children=[cube, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_top_bottom(self):
        """
        Test for a centered cube extended by eps top and bottom.
        """
        scad = Scad(context=Context(eps=1.0))

        cube = Cube(size=10,
                    extend_by_eps_top=True,
                    extend_by_eps_bottom=True)

        self.assertAlmostEqual(10.0, cube.size)
        self.assertFalse(cube.center)

        cube = Paint(color='red', child=cube)
        mask = Cube(size=10,
                    extend_by_eps_front=True,
                    extend_by_eps_back=True,
                    extend_by_eps_top=False,
                    extend_by_eps_bottom=False,
                    extend_by_eps_left=True,
                    extend_by_eps_right=True)
        diff = Union(children=[cube, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_front(self):
        """
        Test for a centered cube extended by eps front.
        """
        scad = Scad(context=Context(eps=1.0))

        cube = Cube(size=10,
                    extend_by_eps_front=True)

        self.assertAlmostEqual(10.0, cube.size)
        self.assertFalse(cube.center)

        cube = Paint(color='red', child=cube)
        mask = Cube(size=10,
                    extend_by_eps_front=False,
                    extend_by_eps_back=True,
                    extend_by_eps_top=True,
                    extend_by_eps_bottom=True,
                    extend_by_eps_left=True,
                    extend_by_eps_right=True)
        diff = Union(children=[cube, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_back(self):
        """
        Test for a centered cube extended by eps back.
        """
        scad = Scad(context=Context(eps=1.0))

        cube = Cube(size=10,
                    extend_by_eps_back=True)

        self.assertAlmostEqual(10.0, cube.size)
        self.assertFalse(cube.center)

        cube = Paint(color='red', child=cube)
        mask = Cube(size=10,
                    extend_by_eps_front=True,
                    extend_by_eps_back=False,
                    extend_by_eps_top=True,
                    extend_by_eps_bottom=True,
                    extend_by_eps_left=True,
                    extend_by_eps_right=True)
        diff = Union(children=[cube, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_front_back(self):
        """
        Test for a centered cube extended by eps front and back.
        """
        scad = Scad(context=Context(eps=1.0))

        cube = Cube(size=10,
                    extend_by_eps_front=True,
                    extend_by_eps_back=True)

        self.assertAlmostEqual(10.0, cube.size)
        self.assertFalse(cube.center)

        cube = Paint(color='red', child=cube)
        mask = Cube(size=10,
                    extend_by_eps_front=False,
                    extend_by_eps_back=False,
                    extend_by_eps_top=True,
                    extend_by_eps_bottom=True,
                    extend_by_eps_left=True,
                    extend_by_eps_right=True)
        diff = Union(children=[cube, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_left_front_bottom(self):
        """
        Test for a centered cube extended by eps left, front, and bottom.
        """
        scad = Scad(context=Context(eps=1.0))

        cube = Cube(size=10,
                    extend_by_eps_front=True,
                    extend_by_eps_bottom=True,
                    extend_by_eps_left=True)

        self.assertAlmostEqual(10.0, cube.size)
        self.assertFalse(cube.center)

        cube = Paint(color='red', child=cube)
        mask = Cube(size=10,
                    extend_by_eps_front=False,
                    extend_by_eps_back=True,
                    extend_by_eps_top=True,
                    extend_by_eps_bottom=False,
                    extend_by_eps_left=False,
                    extend_by_eps_right=True)
        diff = Union(children=[cube, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_right_back_top(self):
        """
        Test for a centered cube extended by eps right, back, and top.
        """
        scad = Scad(context=Context(eps=1.0))

        cube = Cube(size=10,
                    extend_by_eps_back=True,
                    extend_by_eps_top=True,
                    extend_by_eps_right=True)

        self.assertAlmostEqual(10.0, cube.size)
        self.assertFalse(cube.center)

        cube = Paint(color='red', child=cube)
        mask = Cube(size=10,
                    extend_by_eps_front=True,
                    extend_by_eps_back=False,
                    extend_by_eps_top=False,
                    extend_by_eps_bottom=True,
                    extend_by_eps_left=True,
                    extend_by_eps_right=False)
        diff = Union(children=[cube, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
