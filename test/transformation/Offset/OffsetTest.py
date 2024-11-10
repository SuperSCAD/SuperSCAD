from ScadTestCase import ScadTestCase
from super_scad.d2.Polygon import Polygon
from super_scad.transformation.Offset import Offset
from super_scad.type.Vector2 import Vector2


class OffsetTest(ScadTestCase):
    """
    Test cases for Offset.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_positive_radius(self):
        """
        Test with a positive radius
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        points = [Vector2(0.0, 0.0), Vector2(0.0, 15.0), Vector2(5.0, 5.0), Vector2(10.0, 10.0), Vector2(10.0, 0.0)]
        offset = Offset(radius=1.0, fn=100, child=Polygon(points=points))

        self.assertAlmostEqual(1.0, offset.radius)
        self.assertIsNone(offset.delta)
        self.assertIsNone(offset.chamfer)
        self.assertIsNone(offset.fa)
        self.assertIsNone(offset.fs)
        self.assertEqual(100, offset.fn)

        scad.run_super_scad(offset, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_negative_radius(self):
        """
        Test with a positive radius
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        points = [Vector2(0.0, 0.0), Vector2(0.0, 15.0), Vector2(5.0, 5.0), Vector2(10.0, 10.0), Vector2(10.0, 0.0)]
        offset = Offset(radius=-1.0, chamfer=True, fn=100, child=Polygon(points=points))

        self.assertAlmostEqual(-1.0, offset.radius)
        self.assertIsNone(offset.delta)
        self.assertIsNone(offset.chamfer)
        self.assertIsNone(offset.fa)
        self.assertIsNone(offset.fs)
        self.assertEqual(100, offset.fn)

        scad.run_super_scad(offset, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_positive_delta_no_chamfer(self):
        """
        Test with a positive delta and no chamfer.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        points = [Vector2(0.0, 0.0), Vector2(0.0, 15.0), Vector2(5.0, 5.0), Vector2(10.0, 10.0), Vector2(10.0, 0.0)]
        offset = Offset(delta=1.0, fn=100, child=Polygon(points=points))

        self.assertIsNone(offset.radius)
        self.assertAlmostEqual(1.0, offset.delta)
        self.assertFalse(offset.chamfer)
        self.assertIsNone(offset.fa)
        self.assertIsNone(offset.fs)
        self.assertEqual(100, offset.fn)

        scad.run_super_scad(offset, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_negative_delta_no_chamfer(self):
        """
        Test with a negative delta and no chamfer.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        points = [Vector2(0.0, 0.0), Vector2(0.0, 15.0), Vector2(5.0, 5.0), Vector2(10.0, 10.0), Vector2(10.0, 0.0)]
        offset = Offset(delta=-1.0, fn=100, child=Polygon(points=points))

        self.assertIsNone(offset.radius)
        self.assertAlmostEqual(-1.0, offset.delta)
        self.assertFalse(offset.chamfer)
        self.assertIsNone(offset.fa)
        self.assertIsNone(offset.fs)
        self.assertEqual(100, offset.fn)

        scad.run_super_scad(offset, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_positive_delta_chamfer(self):
        """
        Test with a positive delta and with chamfer.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        points = [Vector2(0.0, 0.0), Vector2(0.0, 15.0), Vector2(5.0, 5.0), Vector2(10.0, 10.0), Vector2(10.0, 0.0)]
        offset = Offset(delta=1.0, chamfer=True, fn=100, child=Polygon(points=points))

        self.assertIsNone(offset.radius)
        self.assertAlmostEqual(1.0, offset.delta)
        self.assertTrue(offset.chamfer)
        self.assertIsNone(offset.fa)
        self.assertIsNone(offset.fs)
        self.assertEqual(100, offset.fn)

        scad.run_super_scad(offset, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_negative_delta_chamfer(self):
        """
        Test with a negative delta and with chamfer.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        points = [Vector2(0.0, 0.0), Vector2(0.0, 15.0), Vector2(5.0, 5.0), Vector2(10.0, 10.0), Vector2(10.0, 0.0)]
        offset = Offset(delta=-1.0, chamfer=True, fn=100, child=Polygon(points=points))

        self.assertIsNone(offset.radius)
        self.assertAlmostEqual(-1.0, offset.delta)
        self.assertTrue(offset.chamfer)
        self.assertIsNone(offset.fa)
        self.assertIsNone(offset.fs)
        self.assertEqual(100, offset.fn)

        scad.run_super_scad(offset, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
