import math
import random
import unittest

from super_scad.type.Vector2 import Vector2


class Vector2Test(unittest.TestCase):
    """
    Test cases for Vector2.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_addition(self):
        """
        Test adding two vectors.
        """
        vector1 = Vector2(1.0, 2.0)
        vector2 = Vector2(3.0, 4.0)
        vector3 = vector1 + vector2
        self.assertAlmostEqual(1.0, vector1.x)
        self.assertAlmostEqual(2.0, vector1.y)
        self.assertAlmostEqual(3.0, vector2.x)
        self.assertAlmostEqual(4.0, vector2.y)
        self.assertAlmostEqual(4.0, vector3.x)
        self.assertAlmostEqual(6.0, vector3.y)

    # ------------------------------------------------------------------------------------------------------------------
    def test_subtraction(self):
        """
        Test subtraction two vectors.
        """
        vector1 = Vector2(1.0, 2.0)
        vector2 = Vector2(3.0, 5.0)

        vector3 = vector1 - vector2
        self.assertAlmostEqual(1.0, vector1.x)
        self.assertAlmostEqual(2.0, vector1.y)
        self.assertAlmostEqual(3.0, vector2.x)
        self.assertAlmostEqual(5.0, vector2.y)
        self.assertAlmostEqual(-2.0, vector3.x)
        self.assertAlmostEqual(-3.0, vector3.y)

        vector3 = vector2 - vector1
        self.assertAlmostEqual(1.0, vector1.x)
        self.assertAlmostEqual(2.0, vector1.y)
        self.assertAlmostEqual(3.0, vector2.x)
        self.assertAlmostEqual(5.0, vector2.y)
        self.assertAlmostEqual(2.0, vector3.x)
        self.assertAlmostEqual(3.0, vector3.y)

    # ------------------------------------------------------------------------------------------------------------------
    def test_division(self):
        """
        Test division of a vector.
        """
        vector1 = Vector2(1.0, 2.0)
        vector2 = vector1 / 2.0
        self.assertAlmostEqual(1.0, vector1.x)
        self.assertAlmostEqual(2.0, vector1.y)
        self.assertAlmostEqual(0.5, vector2.x)
        self.assertAlmostEqual(1.0, vector2.y)

    # ------------------------------------------------------------------------------------------------------------------
    def test_multiplication(self):
        """
        Test multiplication of a vector.
        """
        vector1 = Vector2(1.0, 2.0)
        vector2 = vector1 * 3.0
        self.assertAlmostEqual(1.0, vector1.x)
        self.assertAlmostEqual(2.0, vector1.y)
        self.assertAlmostEqual(3.0, vector2.x)
        self.assertAlmostEqual(6.0, vector2.y)

    # ------------------------------------------------------------------------------------------------------------------
    def test_length(self):
        """
        Test length of a vector.
        """
        vector = Vector2(3.0, 4.0)
        self.assertAlmostEqual(3.0, vector.x)
        self.assertAlmostEqual(4.0, vector.y)
        self.assertAlmostEqual(5.0, vector.length)

    # ------------------------------------------------------------------------------------------------------------------
    def test_unit(self):
        """
        Test unit vector of a vector.
        """
        vector = Vector2(3.0, 4.0).unit
        self.assertAlmostEqual(0.6, vector.x)
        self.assertAlmostEqual(0.8, vector.y)
        self.assertAlmostEqual(1.0, vector.length)

        vector = Vector2(-3.0, 4.0).unit
        self.assertAlmostEqual(-0.6, vector.x)
        self.assertAlmostEqual(0.8, vector.y)
        self.assertAlmostEqual(1.0, vector.length)

    # ------------------------------------------------------------------------------------------------------------------
    def test_origin(self):
        """
        Test the origin is at the origin.
        """
        self.assertEqual(Vector2.origin.x, 0.0)
        self.assertEqual(Vector2.origin.y, 0.0)

    # ------------------------------------------------------------------------------------------------------------------
    def test_is_origin(self):
        """
        Test is_origin.
        """
        self.assertTrue(Vector2.origin.is_origin)
        self.assertFalse(Vector2.origin.is_not_origin)

        vector = Vector2(0.0, 0.0)
        self.assertTrue(vector.is_origin)
        self.assertFalse(vector.is_not_origin)

        vector = Vector2(1.0, 0.0)
        self.assertFalse(vector.is_origin)
        self.assertTrue(vector.is_not_origin)

        vector = Vector2(0.0, 1.0)
        self.assertFalse(vector.is_origin)
        self.assertTrue(vector.is_not_origin)

    # ------------------------------------------------------------------------------------------------------------------
    def test_distance(self):
        """
        Test distance between two vectors.
        """
        self.assertAlmostEqual(1.0, Vector2.distance(Vector2(0.0, 0.0), Vector2(1.0, 0.0)))
        self.assertAlmostEqual(1.0, Vector2.distance(Vector2(1.0, 0.0), Vector2(0.0, 0.0)))
        self.assertAlmostEqual(5.0, Vector2.distance(Vector2(4.0, 0.0), Vector2(0.0, 3.0)))
        self.assertAlmostEqual(5.0, Vector2.distance(Vector2(-4.0, 0.0), Vector2(0.0, -3.0)))

    # ------------------------------------------------------------------------------------------------------------------
    def test_orientation(self):
        """
        Test the orientation of three vectors.
        """
        p = Vector2(random.uniform(0.0, 100.0), random.uniform(0.0, 100.0))
        q = Vector2(random.uniform(0.0, 100.0), random.uniform(0.0, 100.0))
        r = Vector2(random.uniform(0.0, 100.0), random.uniform(0.0, 100.0))

        self.assertAlmostEqual(Vector2.cross_product(q - p, q - r), Vector2.orientation(p, q, r))

    # ------------------------------------------------------------------------------------------------------------------
    def test_dot_product(self):
        """
        Test the dit product of two vectors.
        """
        p = Vector2(random.uniform(0.0, 100.0), random.uniform(0.0, 100.0))
        self.assertAlmostEqual(Vector2.dot_product(p, p), p.length ** 2)

        p = Vector2(random.uniform(0.0, 100.0), random.uniform(0.0, 100.0))
        q = Vector2.from_polar_coordinates(p.length, p.angle + 90.0)
        self.assertAlmostEqual(Vector2.dot_product(p, q), 0.0)

        p = Vector2(random.uniform(0.0, 100.0), random.uniform(0.0, 100.0))
        q = Vector2.from_polar_coordinates(p.length, p.angle + 45.0)
        self.assertAlmostEqual(Vector2.dot_product(p, q), 1.0 / math.sqrt(2.0) * p.length ** 2)

    # ------------------------------------------------------------------------------------------------------------------
    def test_intermediate(self):
        """
        Test the intermediate of two vectors.
        """
        p = Vector2.origin
        q = Vector2(10.0, 5.0)
        r = Vector2.intermediate(p, q)
        self.assertAlmostEqual(r.x, 5.0)
        self.assertAlmostEqual(r.y, 2.5)

        p = Vector2.origin
        q = Vector2(10.0, 5.0)
        r = Vector2.intermediate(p, q, 0)
        self.assertAlmostEqual(r.x, 0.0)
        self.assertAlmostEqual(r.y, 0.0)

        p = Vector2.origin
        q = Vector2(10.0, 5.0)
        r = Vector2.intermediate(p, q, 1.0)
        self.assertAlmostEqual(r.x, 10.0)
        self.assertAlmostEqual(r.y, 5.0)

# ----------------------------------------------------------------------------------------------------------------------
