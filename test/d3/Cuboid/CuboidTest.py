from ScadTestCase import ScadTestCase
from super_scad.boolean.Union import Union
from super_scad.d3.Cuboid import Cuboid
from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad.scad.Unit import Unit
from super_scad.transformation.Paint import Paint
from super_scad.type.Vector3 import Vector3
from test.d3.Cuboid.ImperialUnitCuboid import ImperialUnitCuboid


class CuboidTestCase(ScadTestCase):
    """
    Testcases for cuboids.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_cuboid_by_size(self):
        """
        Test for a cuboid defined by size.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        cuboid = Cuboid(size=Vector3(30, 20, 10))

        self.assertAlmostEqual(30.0, cuboid.width)
        self.assertAlmostEqual(20.0, cuboid.depth)
        self.assertAlmostEqual(10.0, cuboid.height)
        self.assertAlmostEqual(30.0, cuboid.size.x)
        self.assertAlmostEqual(20.0, cuboid.size.y)
        self.assertAlmostEqual(10.0, cuboid.size.z)
        self.assertFalse(cuboid.center)

        scad.run_super_scad(cuboid, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_cuboid_by_width_and_depth(self):
        """
        Test for a cuboid defined by width and depth.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        cuboid = Cuboid(size=Vector3(30, 20, 10), center=True)

        self.assertAlmostEqual(30.0, cuboid.width)
        self.assertAlmostEqual(20.0, cuboid.depth)
        self.assertAlmostEqual(10.0, cuboid.height)
        self.assertAlmostEqual(30.0, cuboid.size.x)
        self.assertAlmostEqual(20.0, cuboid.size.y)
        self.assertAlmostEqual(10.0, cuboid.size.z)
        self.assertTrue(cuboid.center)

        scad.run_super_scad(cuboid, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_imperial_metric_cuboid(self):
        """
        Test for an imperial unit cuboid in metric units.
        """
        path_actual, path_expected = self.paths()
        scad = self.create_scad()
        cuboid = ImperialUnitCuboid()
        scad.run_super_scad(cuboid, path_actual)

        # self.assertAlmostEqual(76.2, cuboid.imperial_cuboid.width)
        # self.assertAlmostEqual(50.8, cuboid.imperial_cuboid.depth)
        # self.assertAlmostEqual(25.4, cuboid.imperial_cuboid.height)
        # self.assertAlmostEqual(76.2, cuboid.imperial_cuboid.size.x)
        # self.assertAlmostEqual(50.8, cuboid.imperial_cuboid.size.y)
        # self.assertAlmostEqual(25.4, cuboid.imperial_cuboid.size.z)
        self.assertFalse(cuboid.imperial_cuboid.center)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_imperial_imperial_cuboid(self):
        """
        Test for an imperial unit cuboid in imperial units.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad(unit_length_final=Unit.INCH)
        cuboid = ImperialUnitCuboid()
        scad.run_super_scad(cuboid, path_actual)

        self.assertAlmostEqual(3.0, cuboid.imperial_cuboid.width)
        self.assertAlmostEqual(2.0, cuboid.imperial_cuboid.depth)
        self.assertAlmostEqual(1.0, cuboid.imperial_cuboid.height)
        self.assertAlmostEqual(3.0, cuboid.imperial_cuboid.size.x)
        self.assertAlmostEqual(2.0, cuboid.imperial_cuboid.size.y)
        self.assertAlmostEqual(1.0, cuboid.imperial_cuboid.size.z)
        self.assertFalse(cuboid.imperial_cuboid.center)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_centered_extend_by_eps_left(self):
        """
        Test for a centered cuboid extended by eps left.
        """
        scad = Scad(context=Context(eps=1.0))

        cuboid = Cuboid(size=Vector3(40, 20, 10),
                        center=True,
                        extend_by_eps_left=True)
        cuboid = Paint(color='red', child=cuboid)
        mask = Cuboid(size=Vector3(40, 20, 10),
                      center=True,
                      extend_by_eps_front=True,
                      extend_by_eps_back=True,
                      extend_by_eps_top=True,
                      extend_by_eps_bottom=True,
                      extend_by_eps_left=False,
                      extend_by_eps_right=True)
        diff = Union(children=[cuboid, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_centered_extend_by_eps_right(self):
        """
        Test for a centered cuboid extended by eps right.
        """
        scad = Scad(context=Context(eps=1.0))

        cuboid = Cuboid(size=Vector3(40, 20, 10),
                        center=True,
                        extend_by_eps_right=True)
        cuboid = Paint(color='red', child=cuboid)
        mask = Cuboid(size=Vector3(40, 20, 10),
                      center=True,
                      extend_by_eps_front=True,
                      extend_by_eps_back=True,
                      extend_by_eps_top=True,
                      extend_by_eps_bottom=True,
                      extend_by_eps_left=True,
                      extend_by_eps_right=False)
        diff = Union(children=[cuboid, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_centered_extend_by_eps_left_right(self):
        """
        Test for a centered cuboid extended by eps left and right.
        """
        scad = Scad(context=Context(eps=1.0))

        cuboid = Cuboid(size=Vector3(40, 20, 10),
                        center=True,
                        extend_by_eps_left=True,
                        extend_by_eps_right=True)
        cuboid = Paint(color='red', child=cuboid)
        mask = Cuboid(size=Vector3(40, 20, 10),
                      center=True,
                      extend_by_eps_front=True,
                      extend_by_eps_back=True,
                      extend_by_eps_top=True,
                      extend_by_eps_bottom=True,
                      extend_by_eps_left=False,
                      extend_by_eps_right=False)
        diff = Union(children=[cuboid, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_centered_extend_by_eps_top(self):
        """
        Test for a centered cuboid extended by eps top.
        """
        scad = Scad(context=Context(eps=1.0))

        cuboid = Cuboid(size=Vector3(40, 20, 10),
                        center=True,
                        extend_by_eps_top=True)
        cuboid = Paint(color='red', child=cuboid)
        mask = Cuboid(size=Vector3(40, 20, 10),
                      center=True,
                      extend_by_eps_front=True,
                      extend_by_eps_back=True,
                      extend_by_eps_top=False,
                      extend_by_eps_bottom=True,
                      extend_by_eps_left=True,
                      extend_by_eps_right=True)
        diff = Union(children=[cuboid, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_centered_extend_by_eps_bottom(self):
        """
        Test for a centered cuboid extended by eps bottom.
        """
        scad = Scad(context=Context(eps=1.0))

        cuboid = Cuboid(size=Vector3(40, 20, 10),
                        center=True,
                        extend_by_eps_bottom=True)
        cuboid = Paint(color='red', child=cuboid)
        mask = Cuboid(size=Vector3(40, 20, 10),
                      center=True,
                      extend_by_eps_front=True,
                      extend_by_eps_back=True,
                      extend_by_eps_top=True,
                      extend_by_eps_bottom=False,
                      extend_by_eps_left=True,
                      extend_by_eps_right=True)
        diff = Union(children=[cuboid, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_centered_extend_by_eps_top_bottom(self):
        """
        Test for a centered cuboid extended by eps top and bottom.
        """
        scad = Scad(context=Context(eps=1.0))

        cuboid = Cuboid(size=Vector3(40, 20, 10),
                        center=True,
                        extend_by_eps_top=True,
                        extend_by_eps_bottom=True)
        cuboid = Paint(color='red', child=cuboid)
        mask = Cuboid(size=Vector3(40, 20, 10),
                      center=True,
                      extend_by_eps_front=True,
                      extend_by_eps_back=True,
                      extend_by_eps_top=False,
                      extend_by_eps_bottom=False,
                      extend_by_eps_left=True,
                      extend_by_eps_right=True)
        diff = Union(children=[cuboid, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_centered_extend_by_eps_front(self):
        """
        Test for a centered cuboid extended by eps front.
        """
        scad = Scad(context=Context(eps=1.0))

        cuboid = Cuboid(size=Vector3(40, 20, 10),
                        center=True,
                        extend_by_eps_front=True)
        cuboid = Paint(color='red', child=cuboid)
        mask = Cuboid(size=Vector3(40, 20, 10),
                      center=True,
                      extend_by_eps_front=False,
                      extend_by_eps_back=True,
                      extend_by_eps_top=True,
                      extend_by_eps_bottom=True,
                      extend_by_eps_left=True,
                      extend_by_eps_right=True)
        diff = Union(children=[cuboid, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_centered_extend_by_eps_back(self):
        """
        Test for a centered cuboid extended by eps back.
        """
        scad = Scad(context=Context(eps=1.0))

        cuboid = Cuboid(size=Vector3(40, 20, 10),
                        center=True,
                        extend_by_eps_back=True)
        cuboid = Paint(color='red', child=cuboid)
        mask = Cuboid(size=Vector3(40, 20, 10),
                      center=True,
                      extend_by_eps_front=True,
                      extend_by_eps_back=False,
                      extend_by_eps_top=True,
                      extend_by_eps_bottom=True,
                      extend_by_eps_left=True,
                      extend_by_eps_right=True)
        diff = Union(children=[cuboid, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_centered_extend_by_eps_front_back(self):
        """
        Test for a centered cuboid extended by eps front and back.
        """
        scad = Scad(context=Context(eps=1.0))

        cuboid = Cuboid(size=Vector3(40, 20, 10),
                        center=True,
                        extend_by_eps_front=True,
                        extend_by_eps_back=True)
        cuboid = Paint(color='red', child=cuboid)
        mask = Cuboid(size=Vector3(40, 20, 10),
                      center=True,
                      extend_by_eps_front=False,
                      extend_by_eps_back=False,
                      extend_by_eps_top=True,
                      extend_by_eps_bottom=True,
                      extend_by_eps_left=True,
                      extend_by_eps_right=True)
        diff = Union(children=[cuboid, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_centered_extend_by_eps_left_front_bottom(self):
        """
        Test for a centered cuboid extended by eps left, front, and bottom.
        """
        scad = Scad(context=Context(eps=1.0))

        cuboid = Cuboid(size=Vector3(40, 20, 10),
                        center=True,
                        extend_by_eps_front=True,
                        extend_by_eps_bottom=True,
                        extend_by_eps_left=True)
        cuboid = Paint(color='red', child=cuboid)
        mask = Cuboid(size=Vector3(40, 20, 10),
                      center=True,
                      extend_by_eps_front=False,
                      extend_by_eps_back=True,
                      extend_by_eps_top=True,
                      extend_by_eps_bottom=False,
                      extend_by_eps_left=False,
                      extend_by_eps_right=True)
        diff = Union(children=[cuboid, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_centered_extend_by_eps_right_back_top(self):
        """
        Test for a centered cuboid extended by eps right, back, and top.
        """
        scad = Scad(context=Context(eps=1.0))

        cuboid = Cuboid(size=Vector3(40, 20, 10),
                        center=True,
                        extend_by_eps_back=True,
                        extend_by_eps_top=True,
                        extend_by_eps_right=True)
        cuboid = Paint(color='red', child=cuboid)
        mask = Cuboid(size=Vector3(40, 20, 10),
                      center=True,
                      extend_by_eps_front=True,
                      extend_by_eps_back=False,
                      extend_by_eps_top=False,
                      extend_by_eps_bottom=True,
                      extend_by_eps_left=True,
                      extend_by_eps_right=False)
        diff = Union(children=[cuboid, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_left(self):
        """
        Test for a centered cuboid extended by eps left.
        """
        scad = Scad(context=Context(eps=1.0))

        cuboid = Cuboid(size=Vector3(40, 20, 10),
                        extend_by_eps_left=True)
        cuboid = Paint(color='red', child=cuboid)
        mask = Cuboid(size=Vector3(40, 20, 10),
                      extend_by_eps_front=True,
                      extend_by_eps_back=True,
                      extend_by_eps_top=True,
                      extend_by_eps_bottom=True,
                      extend_by_eps_left=False,
                      extend_by_eps_right=True)
        diff = Union(children=[cuboid, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_right(self):
        """
        Test for a centered cuboid extended by eps right.
        """
        scad = Scad(context=Context(eps=1.0))

        cuboid = Cuboid(size=Vector3(40, 20, 10),
                        extend_by_eps_right=True)
        cuboid = Paint(color='red', child=cuboid)
        mask = Cuboid(size=Vector3(40, 20, 10),
                      extend_by_eps_front=True,
                      extend_by_eps_back=True,
                      extend_by_eps_top=True,
                      extend_by_eps_bottom=True,
                      extend_by_eps_left=True,
                      extend_by_eps_right=False)
        diff = Union(children=[cuboid, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_left_right(self):
        """
        Test for a centered cuboid extended by eps left and right.
        """
        scad = Scad(context=Context(eps=1.0))

        cuboid = Cuboid(size=Vector3(40, 20, 10),
                        extend_by_eps_left=True,
                        extend_by_eps_right=True)
        cuboid = Paint(color='red', child=cuboid)
        mask = Cuboid(size=Vector3(40, 20, 10),
                      extend_by_eps_front=True,
                      extend_by_eps_back=True,
                      extend_by_eps_top=True,
                      extend_by_eps_bottom=True,
                      extend_by_eps_left=False,
                      extend_by_eps_right=False)
        diff = Union(children=[cuboid, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_top(self):
        """
        Test for a centered cuboid extended by eps top.
        """
        scad = Scad(context=Context(eps=1.0))

        cuboid = Cuboid(size=Vector3(40, 20, 10),
                        extend_by_eps_top=True)
        cuboid = Paint(color='red', child=cuboid)
        mask = Cuboid(size=Vector3(40, 20, 10),
                      extend_by_eps_front=True,
                      extend_by_eps_back=True,
                      extend_by_eps_top=False,
                      extend_by_eps_bottom=True,
                      extend_by_eps_left=True,
                      extend_by_eps_right=True)
        diff = Union(children=[cuboid, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_bottom(self):
        """
        Test for a centered cuboid extended by eps bottom.
        """
        scad = Scad(context=Context(eps=1.0))

        cuboid = Cuboid(size=Vector3(40, 20, 10),
                        extend_by_eps_bottom=True)
        cuboid = Paint(color='red', child=cuboid)
        mask = Cuboid(size=Vector3(40, 20, 10),
                      extend_by_eps_front=True,
                      extend_by_eps_back=True,
                      extend_by_eps_top=True,
                      extend_by_eps_bottom=False,
                      extend_by_eps_left=True,
                      extend_by_eps_right=True)
        diff = Union(children=[cuboid, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_top_bottom(self):
        """
        Test for a centered cuboid extended by eps top and bottom.
        """
        scad = Scad(context=Context(eps=1.0))

        cuboid = Cuboid(size=Vector3(40, 20, 10),
                        extend_by_eps_top=True,
                        extend_by_eps_bottom=True)
        cuboid = Paint(color='red', child=cuboid)
        mask = Cuboid(size=Vector3(40, 20, 10),
                      extend_by_eps_front=True,
                      extend_by_eps_back=True,
                      extend_by_eps_top=False,
                      extend_by_eps_bottom=False,
                      extend_by_eps_left=True,
                      extend_by_eps_right=True)
        diff = Union(children=[cuboid, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_front(self):
        """
        Test for a centered cuboid extended by eps front.
        """
        scad = Scad(context=Context(eps=1.0))

        cuboid = Cuboid(size=Vector3(40, 20, 10),
                        extend_by_eps_front=True)
        cuboid = Paint(color='red', child=cuboid)
        mask = Cuboid(size=Vector3(40, 20, 10),
                      extend_by_eps_front=False,
                      extend_by_eps_back=True,
                      extend_by_eps_top=True,
                      extend_by_eps_bottom=True,
                      extend_by_eps_left=True,
                      extend_by_eps_right=True)
        diff = Union(children=[cuboid, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_back(self):
        """
        Test for a centered cuboid extended by eps back.
        """
        scad = Scad(context=Context(eps=1.0))

        cuboid = Cuboid(size=Vector3(40, 20, 10),
                        extend_by_eps_back=True)
        cuboid = Paint(color='red', child=cuboid)
        mask = Cuboid(size=Vector3(40, 20, 10),
                      extend_by_eps_front=True,
                      extend_by_eps_back=False,
                      extend_by_eps_top=True,
                      extend_by_eps_bottom=True,
                      extend_by_eps_left=True,
                      extend_by_eps_right=True)
        diff = Union(children=[cuboid, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_front_back(self):
        """
        Test for a centered cuboid extended by eps front and back.
        """
        scad = Scad(context=Context(eps=1.0))

        cuboid = Cuboid(size=Vector3(40, 20, 10),
                        extend_by_eps_front=True,
                        extend_by_eps_back=True)
        cuboid = Paint(color='red', child=cuboid)
        mask = Cuboid(size=Vector3(40, 20, 10),
                      extend_by_eps_front=False,
                      extend_by_eps_back=False,
                      extend_by_eps_top=True,
                      extend_by_eps_bottom=True,
                      extend_by_eps_left=True,
                      extend_by_eps_right=True)
        diff = Union(children=[cuboid, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_left_front_bottom(self):
        """
        Test for a centered cuboid extended by eps left, front, and bottom.
        """
        scad = Scad(context=Context(eps=1.0))

        cuboid = Cuboid(size=Vector3(40, 20, 10),
                        extend_by_eps_front=True,
                        extend_by_eps_bottom=True,
                        extend_by_eps_left=True)
        cuboid = Paint(color='red', child=cuboid)
        mask = Cuboid(size=Vector3(40, 20, 10),
                      extend_by_eps_front=False,
                      extend_by_eps_back=True,
                      extend_by_eps_top=True,
                      extend_by_eps_bottom=False,
                      extend_by_eps_left=False,
                      extend_by_eps_right=True)
        diff = Union(children=[cuboid, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_right_back_top(self):
        """
        Test for a centered cuboid extended by eps right, back, and top.
        """
        scad = Scad(context=Context(eps=1.0))

        cuboid = Cuboid(size=Vector3(40, 20, 10),
                        extend_by_eps_back=True,
                        extend_by_eps_top=True,
                        extend_by_eps_right=True)
        cuboid = Paint(color='red', child=cuboid)
        mask = Cuboid(size=Vector3(40, 20, 10),
                      extend_by_eps_front=True,
                      extend_by_eps_back=False,
                      extend_by_eps_top=False,
                      extend_by_eps_bottom=True,
                      extend_by_eps_left=True,
                      extend_by_eps_right=False)
        diff = Union(children=[cuboid, mask])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(diff, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
