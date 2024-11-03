import unittest

from super_scad.type.Vector3 import Vector3


class Vector3Test(unittest.TestCase):
    """
    Test cases for Vector3.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testAddition(self):
        """
        Test adding two vectors.
        """
        vector1 = Vector3(1.0, 2.0, 3.0)
        vector2 = Vector3(4.0, 5.0, 6.0)
        vector3 = vector1 + vector2
        self.assertAlmostEqual(1.0, vector1.x)
        self.assertAlmostEqual(2.0, vector1.y)
        self.assertAlmostEqual(3.0, vector1.z)
        self.assertAlmostEqual(4.0, vector2.x)
        self.assertAlmostEqual(5.0, vector2.y)
        self.assertAlmostEqual(6.0, vector2.z)
        self.assertAlmostEqual(5.0, vector3.x)
        self.assertAlmostEqual(7.0, vector3.y)
        self.assertAlmostEqual(9.0, vector3.z)

    # ------------------------------------------------------------------------------------------------------------------
    def testSubtraction(self):
        """
        Test subtraction two vectors.
        """
        vector1 = Vector3(1.0, 2.0, 3.0)
        vector2 = Vector3(4.0, 6.0, 8.0)

        vector3 = vector1 - vector2
        self.assertAlmostEqual(1.0, vector1.x)
        self.assertAlmostEqual(2.0, vector1.y)
        self.assertAlmostEqual(3.0, vector1.z)
        self.assertAlmostEqual(4.0, vector2.x)
        self.assertAlmostEqual(6.0, vector2.y)
        self.assertAlmostEqual(8.0, vector2.z)
        self.assertAlmostEqual(-3.0, vector3.x)
        self.assertAlmostEqual(-4.0, vector3.y)
        self.assertAlmostEqual(-5.0, vector3.z)

        vector3 = vector2 - vector1
        self.assertAlmostEqual(1.0, vector1.x)
        self.assertAlmostEqual(2.0, vector1.y)
        self.assertAlmostEqual(3.0, vector1.z)
        self.assertAlmostEqual(4.0, vector2.x)
        self.assertAlmostEqual(6.0, vector2.y)
        self.assertAlmostEqual(8.0, vector2.z)
        self.assertAlmostEqual(3.0, vector3.x)
        self.assertAlmostEqual(4.0, vector3.y)
        self.assertAlmostEqual(5.0, vector3.z)

    # ------------------------------------------------------------------------------------------------------------------
    def testDivision(self):
        """
        Test division of a vector.
        """
        vector1 = Vector3(1.0, 2.0, 3.0)
        vector2 = vector1 / 2.0
        self.assertAlmostEqual(1.0, vector1.x)
        self.assertAlmostEqual(2.0, vector1.y)
        self.assertAlmostEqual(3.0, vector1.z)
        self.assertAlmostEqual(0.5, vector2.x)
        self.assertAlmostEqual(1.0, vector2.y)
        self.assertAlmostEqual(1.5, vector2.z)

    # ------------------------------------------------------------------------------------------------------------------
    def testMultiplication(self):
        """
        Test multiplication of a vector.
        """
        vector1 = Vector3(1.0, 2.0, 3.0)
        vector2 = vector1 * 4.0
        self.assertAlmostEqual(1.0, vector1.x)
        self.assertAlmostEqual(2.0, vector1.y)
        self.assertAlmostEqual(3.0, vector1.z)
        self.assertAlmostEqual(4.0, vector2.x)
        self.assertAlmostEqual(8.0, vector2.y)
        self.assertAlmostEqual(12.0, vector2.z)

    # ------------------------------------------------------------------------------------------------------------------
    def testLength(self):
        """
        Test length of a vector.
        """
        vector = Vector3(2.0, 3.0, 4.0)
        self.assertAlmostEqual(2.0, vector.x)
        self.assertAlmostEqual(3.0, vector.y)
        self.assertAlmostEqual(4.0, vector.z)
        self.assertAlmostEqual(5.385164807134504, vector.length)

    # ------------------------------------------------------------------------------------------------------------------
    def testNormal(self):
        """
        Test normalized vector of a vector.
        """
        vector = Vector3(2.0, 3.0, 4.0).normal
        self.assertAlmostEqual(0.3713906763541037, vector.x)
        self.assertAlmostEqual(0.5570860145311556, vector.y)
        self.assertAlmostEqual(0.7427813527082074, vector.z)
        self.assertAlmostEqual(1.0, vector.length)

        vector = Vector3(2.0, -3.0, 4.0).normal
        self.assertAlmostEqual(0.3713906763541037, vector.x)
        self.assertAlmostEqual(-0.5570860145311556, vector.y)
        self.assertAlmostEqual(0.7427813527082074, vector.z)
        self.assertAlmostEqual(1.0, vector.length)

    # ------------------------------------------------------------------------------------------------------------------
    def testOrigin(self):
        """
        Test the origin is at the origin.
        """
        self.assertEqual(Vector3.origin.x, 0.0)
        self.assertEqual(Vector3.origin.y, 0.0)
        self.assertEqual(Vector3.origin.z, 0.0)

    # ------------------------------------------------------------------------------------------------------------------
    def testIsOrigin(self):
        """
        Test is_origin.
        """
        self.assertTrue(Vector3.origin.is_origin)
        self.assertFalse(Vector3.origin.is_not_origin)

        vector = Vector3(0.0, 0.0, 0.0)
        self.assertTrue(vector.is_origin)
        self.assertFalse(vector.is_not_origin)

        vector = Vector3(1.0, 0.0, 0.0)
        self.assertFalse(vector.is_origin)
        self.assertTrue(vector.is_not_origin)

        vector = Vector3(0.0, 1.0, 0.0)
        self.assertFalse(vector.is_origin)
        self.assertTrue(vector.is_not_origin)

        vector = Vector3(0.0, 0.0, 1.0)
        self.assertFalse(vector.is_origin)
        self.assertTrue(vector.is_not_origin)


# ----------------------------------------------------------------------------------------------------------------------
