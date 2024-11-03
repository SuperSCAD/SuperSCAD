import unittest

from super_scad.type.Vector2 import Vector2


class Vector2Test(unittest.TestCase):
    """
    Test cases for Vector2.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testAddition(self):
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
    def testSubtraction(self):
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
    def testDivision(self):
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
    def testMultiplication(self):
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
    def testLength(self):
        """
        Test length of a vector.
        """
        vector = Vector2(3.0, 4.0)
        self.assertAlmostEqual(3.0, vector.x)
        self.assertAlmostEqual(4.0, vector.y)
        self.assertAlmostEqual(5.0, vector.length)

    # ------------------------------------------------------------------------------------------------------------------
    def testNormal(self):
        """
        Test normalized vector of a vector.
        """
        vector = Vector2(3.0, 4.0).normal
        self.assertAlmostEqual(0.6, vector.x)
        self.assertAlmostEqual(0.8, vector.y)
        self.assertAlmostEqual(1.0, vector.length)

        vector = Vector2(-3.0, 4.0).normal
        self.assertAlmostEqual(-0.6, vector.x)
        self.assertAlmostEqual(0.8, vector.y)
        self.assertAlmostEqual(1.0, vector.length)

    # ------------------------------------------------------------------------------------------------------------------
    def testOrigin(self):
        """
        Test the origin is at the origin.
        """
        self.assertEqual(Vector2.origin.x, 0.0)
        self.assertEqual(Vector2.origin.y, 0.0)

    # ------------------------------------------------------------------------------------------------------------------
    def testIsOrigin(self):
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

# ----------------------------------------------------------------------------------------------------------------------
