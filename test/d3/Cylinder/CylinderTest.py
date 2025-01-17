from d3.Cylinder.ImperialCylinder import ImperialCylinder
from ScadTestCase import ScadTestCase
from super_scad.boolean.Compound import Compound
from super_scad.boolean.Union import Union
from super_scad.d3.Cuboid import Cuboid
from super_scad.d3.Cylinder import Cylinder
from super_scad.other.Modify import Modify
from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad.scad.Unit import Unit
from super_scad.transformation.Translate3D import Translate3D
from super_scad.type.Vector3 import Vector3


class CylinderTestCase(ScadTestCase):
    """
    Testcases for cylinder.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_cylinder_radius(self):
        """
        Test for a cylinder defined by a radius.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        cylinder = Cylinder(height=10.0, radius=2.0)

        self.assertAlmostEqual(10.0, cylinder.height)
        self.assertEqual(0.0, cylinder.start_point.x)
        self.assertEqual(0.0, cylinder.start_point.y)
        self.assertEqual(0.0, cylinder.start_point.z)
        self.assertEqual(0.0, cylinder.end_point.x)
        self.assertEqual(0.0, cylinder.end_point.y)
        self.assertAlmostEqual(10.0, cylinder.end_point.z)
        self.assertAlmostEqual(2.0, cylinder.radius)
        self.assertAlmostEqual(4.0, cylinder.diameter)
        self.assertFalse(cylinder.center)
        self.assertIsNone(cylinder.fa)
        self.assertIsNone(cylinder.fs)
        self.assertIsNone(cylinder.fn)

        scad.run_super_scad(cylinder, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_cylinder_diameter(self):
        """
        Test for a cylinder defined by a diameter.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        cylinder = Cylinder(height=10.0, diameter=2.0, center=True)

        self.assertAlmostEqual(10.0, cylinder.height)
        self.assertEqual(0.0, cylinder.start_point.x)
        self.assertEqual(0.0, cylinder.start_point.y)
        self.assertAlmostEqual(-5.0, cylinder.start_point.z)
        self.assertEqual(0.0, cylinder.end_point.x)
        self.assertEqual(0.0, cylinder.end_point.y)
        self.assertAlmostEqual(5.0, cylinder.end_point.z)
        self.assertAlmostEqual(1.0, cylinder.radius)
        self.assertAlmostEqual(2.0, cylinder.diameter)
        self.assertTrue(cylinder.center)
        self.assertIsNone(cylinder.fa)
        self.assertIsNone(cylinder.fs)
        self.assertIsNone(cylinder.fn)

        scad.run_super_scad(cylinder, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_cylinder_start_end_point(self):
        """
        Test for a cylinder defined by a start and end point.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        start_point = Vector3(3.0, 2.0, 1.0)
        end_point = Vector3(30.0, 20.0, 10.0)
        diff = end_point - start_point
        cylinder = Cylinder(start_point=start_point, end_point=end_point, diameter=0.1, fn=64)
        cuboid = Modify(transparent=True,
                        child=Translate3D(vector=start_point,
                                          child=Cuboid(width=diff.x, depth=diff.y, height=diff.z)))

        self.assertAlmostEqual(diff.length, cylinder.height)
        self.assertAlmostEqual(3.0, cylinder.start_point.x)
        self.assertAlmostEqual(2.0, cylinder.start_point.y)
        self.assertAlmostEqual(1.0, cylinder.start_point.z)
        self.assertAlmostEqual(30.0, cylinder.end_point.x)
        self.assertAlmostEqual(20.0, cylinder.end_point.y)
        self.assertAlmostEqual(10.0, cylinder.end_point.z)
        self.assertAlmostEqual(0.05, cylinder.radius)
        self.assertAlmostEqual(0.1, cylinder.diameter)
        self.assertFalse(cylinder.center)
        self.assertIsNone(cylinder.fa)
        self.assertIsNone(cylinder.fs)
        self.assertEqual(64, cylinder.fn)

        scad.run_super_scad(Union(children=[cylinder, cuboid]), path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_cylinder4n(self):
        """
        Test for a cylinder with a multiple of 4 vertices.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        cylinder = Cylinder(height=10.0, radius=2.0, fn4n=True)

        self.assertAlmostEqual(10.0, cylinder.height)
        self.assertEqual(0.0, cylinder.start_point.x)
        self.assertEqual(0.0, cylinder.start_point.y)
        self.assertEqual(0.0, cylinder.start_point.z)
        self.assertEqual(0.0, cylinder.end_point.x)
        self.assertEqual(0.0, cylinder.end_point.y)
        self.assertAlmostEqual(10.0, cylinder.end_point.z)
        self.assertAlmostEqual(2.0, cylinder.radius)
        self.assertAlmostEqual(4.0, cylinder.diameter)
        self.assertFalse(cylinder.center)
        self.assertIsNone(cylinder.fn)
        self.assertTrue(cylinder.fn4n)

        scad.run_super_scad(cylinder, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_cylinder_auxiliary_parameter(self):
        """
        Test auxiliary parameters.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        cylinder = Cylinder(height=100.0, diameter=10.0, fa=12.0, fs=2.0, fn=0)

        self.assertAlmostEqual(100.0, cylinder.height)
        self.assertEqual(0.0, cylinder.start_point.x)
        self.assertEqual(0.0, cylinder.start_point.y)
        self.assertEqual(0.0, cylinder.start_point.z)
        self.assertEqual(0.0, cylinder.end_point.x)
        self.assertEqual(0.0, cylinder.end_point.y)
        self.assertAlmostEqual(100.0, cylinder.end_point.z)
        self.assertAlmostEqual(5.0, cylinder.radius)
        self.assertAlmostEqual(10.0, cylinder.diameter)
        self.assertFalse(cylinder.center)
        self.assertAlmostEqual(12.0, cylinder.fa)
        self.assertAlmostEqual(2.0, cylinder.fs)
        self.assertEqual(0, cylinder.fn)
        self.assertFalse(cylinder.fn4n)

        scad.run_super_scad(cylinder, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_imperial_metric_cylinder(self):
        """
        Test for an imperial cylinder in metric units.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        cylinder = ImperialCylinder(height=100.0, radius=20.0, fa=12.0, fs=2.0, fn=0)
        scad.run_super_scad(cylinder, path_actual)

        # self.assertAlmostEqual(100.0 * 25.4, cylinder.imperial_cylinder.height)
        self.assertEqual(0.0, cylinder.imperial_cylinder.start_point.x)
        # self.assertEqual(0.0, cylinder.imperial_cylinder.start_point.y)
        # self.assertEqual(0.0, cylinder.imperial_cylinder.start_point.z)
        # self.assertEqual(0.0, cylinder.imperial_cylinder.end_point.x)
        # self.assertEqual(0.0, cylinder.imperial_cylinder.end_point.y)
        # self.assertAlmostEqual(100.0 * 25.4, cylinder.imperial_cylinder.end_point.z)
        # self.assertAlmostEqual(20.0 * 25.4, cylinder.imperial_cylinder.radius)
        # self.assertAlmostEqual(40.0 * 25.4, cylinder.imperial_cylinder.diameter)
        self.assertFalse(cylinder.imperial_cylinder.center)
        self.assertAlmostEqual(12.0, cylinder.imperial_cylinder.fa)
        # self.assertAlmostEqual(2.0 * 25.4, cylinder.imperial_cylinder.fs)
        self.assertEqual(0, cylinder.imperial_cylinder.fn)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_imperial_imperial_cylinder(self):
        """
        Test for an imperial cylinder in imperial units.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad(unit_length_final=Unit.INCH)
        cylinder = ImperialCylinder(height=100.0, radius=20.0, fa=12.0, fs=2.0, fn=0)
        scad.run_super_scad(cylinder, path_actual)

        self.assertAlmostEqual(100.0, cylinder.imperial_cylinder.height)
        self.assertEqual(0.0, cylinder.imperial_cylinder.start_point.x)
        self.assertEqual(0.0, cylinder.imperial_cylinder.start_point.y)
        self.assertEqual(0.0, cylinder.imperial_cylinder.start_point.z)
        self.assertEqual(0.0, cylinder.imperial_cylinder.end_point.x)
        self.assertEqual(0.0, cylinder.imperial_cylinder.end_point.y)
        self.assertAlmostEqual(100.0, cylinder.imperial_cylinder.end_point.z)
        self.assertAlmostEqual(20.0, cylinder.imperial_cylinder.radius)
        self.assertAlmostEqual(40.0, cylinder.imperial_cylinder.diameter)
        self.assertFalse(cylinder.imperial_cylinder.center)
        self.assertAlmostEqual(12.0, cylinder.imperial_cylinder.fa)
        self.assertAlmostEqual(2.0, cylinder.imperial_cylinder.fs)
        self.assertEqual(0, cylinder.imperial_cylinder.fn)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_centered(self):
        """
        Test extend by eps for a centered cylinders.
        """
        scad = Scad(context=Context(fn=60, eps=1.0))

        cylinder0 = Cylinder(height=10.0, diameter=1.0, center=True)
        cylinder1 = Cylinder(height=10.0, diameter=1.0, center=True, extend_by_eps_top=True)
        cylinder2 = Cylinder(height=10.0, diameter=1.0, center=True, extend_by_eps_bottom=True)
        cylinder3 = Cylinder(height=10.0, diameter=1.0, center=True, extend_by_eps_top=True, extend_by_eps_bottom=True)
        cylinder4 = Cylinder(height=10.0, diameter=1.0, center=True, extend_by_eps_radius=True)

        cylinders = Compound(children=[cylinder0,
                                       Translate3D(x=2.0, child=cylinder1),
                                       Translate3D(x=4.0, child=cylinder2),
                                       Translate3D(x=6.0, child=cylinder3),
                                       Translate3D(x=9.0, child=cylinder4)])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(cylinders, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_not_centered(self):
        """
        Test extend by eps for a not centered cylinders.
        """
        scad = Scad(context=Context(fn=60, eps=1.0))

        cylinder0 = Cylinder(height=10.0, diameter=1.0, center=False)
        cylinder1 = Cylinder(height=10.0, diameter=1.0, center=False, extend_by_eps_top=True)
        cylinder2 = Cylinder(height=10.0, diameter=1.0, center=False, extend_by_eps_bottom=True)
        cylinder3 = Cylinder(height=10.0, diameter=1.0, center=False, extend_by_eps_top=True, extend_by_eps_bottom=True)
        cylinder4 = Cylinder(height=10.0, diameter=1.0, center=False, extend_by_eps_radius=True)

        cylinders = Compound(children=[cylinder0,
                                       Translate3D(x=2.0, child=cylinder1),
                                       Translate3D(x=4.0, child=cylinder2),
                                       Translate3D(x=6.0, child=cylinder3),
                                       Translate3D(x=9.0, child=cylinder4)])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(cylinders, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_extend_by_eps_start_end_point(self):
        """
        Test extend by eps for a cylinder defined by a start and end point.
        """
        scad = Scad(context=Context(fn=60, eps=1.0))

        start_point = Vector3.origin
        end_point = Vector3(10.0, 10.0, 10.0)
        diff = end_point - start_point

        cylinder0 = Cylinder(start_point=start_point, end_point=end_point, diameter=1.0)
        cylinder1 = Cylinder(start_point=start_point, end_point=end_point, diameter=1.0, extend_by_eps_top=True)
        cylinder2 = Cylinder(start_point=start_point, end_point=end_point, diameter=1.0, extend_by_eps_bottom=True)
        cylinder3 = Cylinder(start_point=start_point, end_point=end_point, diameter=1.0, extend_by_eps_top=True,
                             extend_by_eps_bottom=True)
        cylinder4 = Cylinder(start_point=start_point, end_point=end_point, diameter=1.0, extend_by_eps_radius=True)

        cuboid0 = Modify(transparent=True,
                         child=Translate3D(vector=start_point,
                                           child=Cuboid(width=diff.x, depth=diff.y, height=diff.z)))
        cuboid1 = Translate3D(x=10.0, child=cuboid0)
        cuboid2 = Translate3D(x=20.0, child=cuboid0)
        cuboid3 = Translate3D(x=30.0, child=cuboid0)
        cuboid4 = Translate3D(x=40.0, child=cuboid0)

        cylinders = Compound(children=[cylinder0,
                                       Translate3D(x=10.0, child=cylinder1),
                                       Translate3D(x=20.0, child=cylinder2),
                                       Translate3D(x=30.0, child=cylinder3),
                                       Translate3D(x=40.0, child=cylinder4),
                                       cuboid0,
                                       cuboid1,
                                       cuboid2,
                                       cuboid3,
                                       cuboid4])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(cylinders, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
