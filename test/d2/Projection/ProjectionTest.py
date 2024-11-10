from ScadTestCase import ScadTestCase
from super_scad.boolean.Difference import Difference
from super_scad.boolean.Intersection import Intersection
from super_scad.boolean.Union import Union
from super_scad.d2.Projection import Projection
from super_scad.d3.Cone import Cone
from super_scad.d3.Cube import Cube
from super_scad.d3.Cuboid import Cuboid
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.transformation.Rotate3D import Rotate3D
from super_scad.transformation.Translate3D import Translate3D
from super_scad.type.Vector3 import Vector3


class ProjectionTest(ScadTestCase):
    """
    Test case for Projection.
    """

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def example002() -> ScadWidget:
        """
        Returns the object from example002.
        """
        body = Union(children=[Cube(size=30, center=True),
                               Translate3D(z=-25, child=Cuboid(size=Vector3(15, 15, 50), center=True))])

        cross = Union(children=[Cuboid(size=Vector3(50, 10, 10), center=True),
                                Cuboid(size=Vector3(10, 50, 10), center=True),
                                Cuboid(size=Vector3(10, 10, 50), center=True)])

        cone = Translate3D(z=5, child=Cone(height=50, top_radius=5, bottom_radius=20, center=True))

        return Intersection(children=[Difference(children=[body, cross]), cone])

    # ------------------------------------------------------------------------------------------------------------------
    def test_projection_with_cut(self):
        """
        Test with a cut.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        projection = Projection(cut=True, child=self.example002())

        self.assertTrue(20.0, projection.cut)
        self.assertTrue(projection.cut)
        self.assertAlmostEqual(0.0, projection.z)

        scad.run_super_scad(projection, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_projection_with_cut_at_height(self):
        """
        Test with a cut at a specified height.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        projection = Projection(cut=True, z=-20, child=self.example002())

        self.assertTrue(20.0, projection.cut)
        self.assertTrue(projection.cut)
        self.assertAlmostEqual(-20.0, projection.z)

        scad.run_super_scad(projection, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_projection_without_cut(self):
        """
        Test with a cut.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        projection = Projection(cut=False, child=self.example002())

        self.assertTrue(20.0, projection.cut)
        self.assertFalse(projection.cut)
        self.assertIsNone(projection.z)

        scad.run_super_scad(projection, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_projection_side_view(self):
        """
        Test without a cut.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        projection = Projection(child=Translate3D(z=25, child=Rotate3D(angle_x=90, child=self.example002())))

        self.assertTrue(20.0, projection.cut)
        self.assertFalse(projection.cut)
        self.assertIsNone(projection.z)

        scad.run_super_scad(projection, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
