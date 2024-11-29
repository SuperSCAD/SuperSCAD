import unittest

from super_scad.type import Vector2
from super_scad.util.LineIntersection2D import LineIntersection2D


class LineIntersection2DTest(unittest.TestCase):
    """
    Testcase for the LineIntersection2D class.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_simple(self):
        """
        A simple test case.
        """
        intersection = LineIntersection2D.intersection(Vector2(-1.0, 0.0),
                                                       Vector2(1.0, 0.0),
                                                       Vector2(0.0, 1.0),
                                                       Vector2(0.0, -1.0))
        self.assertEqual(intersection, Vector2.origin)

    # ------------------------------------------------------------------------------------------------------------------
    def test_co_parallel(self):
        """
        Two co-parallel lines.
        """
        intersection = LineIntersection2D.intersection(Vector2(0.0, 0.0),
                                                       Vector2(1.0, 0.0),
                                                       Vector2(2.0, 0.0),
                                                       Vector2(3.0, 0.0))
        self.assertIsNone(intersection)

    # ------------------------------------------------------------------------------------------------------------------
    def test_parallel(self):
        """
        Two parallel lines.
        """
        intersection = LineIntersection2D.intersection(Vector2(0.0, 0.0),
                                                       Vector2(1.0, 0.0),
                                                       Vector2(3.0, 1.0),
                                                       Vector2(4.0, 1.0))
        self.assertIsNone(intersection)

# ----------------------------------------------------------------------------------------------------------------------
