import unittest

from super_scad.type.Point2 import Point2


class Point2Test(unittest.TestCase):
    """
    Test cases for Point2.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testAddition(self):
        """
        Test adding two points.
        """
        p1 = Point2(1.0, 2.0)
        p2 = Point2(3.0, 4.0)
        p3 = p1 + p2
        self.assertAlmostEqual(1.0, p1.x)
        self.assertAlmostEqual(2.0, p1.y)
        self.assertAlmostEqual(3.0, p2.x)
        self.assertAlmostEqual(4.0, p2.y)
        self.assertAlmostEqual(4.0, p3.x)
        self.assertAlmostEqual(6.0, p3.y)

    # ------------------------------------------------------------------------------------------------------------------
    def testSubtraction(self):
        """
        Test subtraction two points.
        """
        p1 = Point2(1.0, 2.0)
        p2 = Point2(3.0, 5.0)

        p3 = p1 - p2
        self.assertAlmostEqual(1.0, p1.x)
        self.assertAlmostEqual(2.0, p1.y)
        self.assertAlmostEqual(3.0, p2.x)
        self.assertAlmostEqual(5.0, p2.y)
        self.assertAlmostEqual(-2.0, p3.x)
        self.assertAlmostEqual(-3.0, p3.y)

        p3 = p2 - p1
        self.assertAlmostEqual(1.0, p1.x)
        self.assertAlmostEqual(2.0, p1.y)
        self.assertAlmostEqual(3.0, p2.x)
        self.assertAlmostEqual(5.0, p2.y)
        self.assertAlmostEqual(2.0, p3.x)
        self.assertAlmostEqual(3.0, p3.y)

    # ------------------------------------------------------------------------------------------------------------------
    def testDivision(self):
        """
        Test division of a point.
        """
        p1 = Point2(1.0, 2.0)
        p2 = p1 / 2.0
        self.assertAlmostEqual(1.0, p1.x)
        self.assertAlmostEqual(2.0, p1.y)
        self.assertAlmostEqual(0.5, p2.x)
        self.assertAlmostEqual(1.0, p2.y)

    # ------------------------------------------------------------------------------------------------------------------
    def testMultiplication(self):
        """
        Test multiplication of a point.
        """
        p1 = Point2(1.0, 2.0)
        p2 = p1 * 3.0
        self.assertAlmostEqual(1.0, p1.x)
        self.assertAlmostEqual(2.0, p1.y)
        self.assertAlmostEqual(3.0, p2.x)
        self.assertAlmostEqual(6.0, p2.y)

    # ------------------------------------------------------------------------------------------------------------------
    def testLength(self):
        """
        Test length of a point.
        """
        point = Point2(3.0, 4.0)
        length = point.length()
        self.assertAlmostEqual(3.0, point.x)
        self.assertAlmostEqual(4.0, point.y)
        self.assertAlmostEqual(5.0, length)

# ----------------------------------------------------------------------------------------------------------------------
