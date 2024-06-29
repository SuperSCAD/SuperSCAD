import unittest

from super_scad.type.Point3 import Point3


class Point3Test(unittest.TestCase):
    """
    Test cases for Point3.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testAddition(self):
        """
        Test adding two points.
        """
        p1 = Point3(1.0, 2.0, 3.0)
        p2 = Point3(4.0, 5.0, 6.0)
        p3 = p1 + p2
        self.assertAlmostEqual(1.0, p1.x)
        self.assertAlmostEqual(2.0, p1.y)
        self.assertAlmostEqual(3.0, p1.z)
        self.assertAlmostEqual(4.0, p2.x)
        self.assertAlmostEqual(5.0, p2.y)
        self.assertAlmostEqual(6.0, p2.z)
        self.assertAlmostEqual(5.0, p3.x)
        self.assertAlmostEqual(7.0, p3.y)
        self.assertAlmostEqual(9.0, p3.z)

    # ------------------------------------------------------------------------------------------------------------------
    def testSubtraction(self):
        """
        Test subtraction two points.
        """
        p1 = Point3(1.0, 2.0, 3.0)
        p2 = Point3(4.0, 6.0, 8.0)

        p3 = p1 - p2
        self.assertAlmostEqual(1.0, p1.x)
        self.assertAlmostEqual(2.0, p1.y)
        self.assertAlmostEqual(3.0, p1.z)
        self.assertAlmostEqual(4.0, p2.x)
        self.assertAlmostEqual(6.0, p2.y)
        self.assertAlmostEqual(8.0, p2.z)
        self.assertAlmostEqual(-3.0, p3.x)
        self.assertAlmostEqual(-4.0, p3.y)
        self.assertAlmostEqual(-5.0, p3.z)

        p3 = p2 - p1
        self.assertAlmostEqual(1.0, p1.x)
        self.assertAlmostEqual(2.0, p1.y)
        self.assertAlmostEqual(3.0, p1.z)
        self.assertAlmostEqual(4.0, p2.x)
        self.assertAlmostEqual(6.0, p2.y)
        self.assertAlmostEqual(8.0, p2.z)
        self.assertAlmostEqual(3.0, p3.x)
        self.assertAlmostEqual(4.0, p3.y)
        self.assertAlmostEqual(5.0, p3.z)

    # ------------------------------------------------------------------------------------------------------------------
    def testDivision(self):
        """
        Test division of a point.
        """
        p1 = Point3(1.0, 2.0, 3.0)
        p2 = p1 / 2.0
        self.assertAlmostEqual(1.0, p1.x)
        self.assertAlmostEqual(2.0, p1.y)
        self.assertAlmostEqual(3.0, p1.z)
        self.assertAlmostEqual(0.5, p2.x)
        self.assertAlmostEqual(1.0, p2.y)
        self.assertAlmostEqual(1.5, p2.z)

    # ------------------------------------------------------------------------------------------------------------------
    def testMultiplication(self):
        """
        Test multiplication of a point.
        """
        p1 = Point3(1.0, 2.0, 3.0)
        p2 = p1 * 4.0
        self.assertAlmostEqual(1.0, p1.x)
        self.assertAlmostEqual(2.0, p1.y)
        self.assertAlmostEqual(3.0, p1.z)
        self.assertAlmostEqual(4.0, p2.x)
        self.assertAlmostEqual(8.0, p2.y)
        self.assertAlmostEqual(12.0, p2.z)

    # ------------------------------------------------------------------------------------------------------------------
    def testLength(self):
        """
        Test length of a point.
        """
        point = Point3(2.0, 3.0, 4.0)
        length = point.length()
        self.assertAlmostEqual(2.0, point.x)
        self.assertAlmostEqual(3.0, point.y)
        self.assertAlmostEqual(4.0, point.z)
        self.assertAlmostEqual(5.385164807134504, length)

# ----------------------------------------------------------------------------------------------------------------------
