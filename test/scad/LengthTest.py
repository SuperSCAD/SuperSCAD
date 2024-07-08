import math
import unittest

from super_scad.scad import Length
from super_scad.scad.Unit import Unit


class LengthTest(unittest.TestCase):
    """
    Test cases for Length class.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testMetric(self):
        """
        Test conversion between metric lengths.
        """
        self.assertEqual(1.0, Length.convert(1000.0, Unit.MM, Unit.M))
        self.assertEqual(1.0, Length.convert(100.0, Unit.CM, Unit.M))
        self.assertEqual(1.0, Length.convert(10.0, Unit.DM, Unit.M))
        self.assertEqual(1.0, Length.convert(1.0, Unit.M, Unit.M))
        self.assertEqual(1000.0, Length.convert(1.0, Unit.KM, Unit.M))

    # ------------------------------------------------------------------------------------------------------------------
    def testImperial(self):
        """
        Test conversion between imperial lengths.
        """
        self.assertAlmostEqual(1.0, Length.convert(1000.0, Unit.THOU, Unit.INCH))
        self.assertAlmostEqual(1.0, Length.convert(12.0, Unit.INCH, Unit.FOOT))
        self.assertAlmostEqual(1.0, Length.convert(3.0, Unit.FOOT, Unit.YARD))
        self.assertAlmostEqual(1.0, Length.convert(5280.0, Unit.FOOT, Unit.MILE))

    # ------------------------------------------------------------------------------------------------------------------
    def testPracticalConversions(self):
        """
        Test some practical conversions.
        """
        self.assertAlmostEqual(25.4, Length.convert(1.0, Unit.INCH, Unit.MM))
        self.assertAlmostEqual(1.0, Length.convert(25.4, Unit.MM, Unit.INCH))
        self.assertAlmostEqual(0.9144, Length.convert(1, Unit.YARD, Unit.M))

    # ------------------------------------------------------------------------------------------------------------------
    def testFreeOfScale(self):
        """
        Test a length free of any scale can be converted to a length free of any scale only.
        """
        self.assertRaises(ValueError, lambda: Length.convert(1.0, Unit.FREE, Unit.MM))
        self.assertRaises(ValueError, lambda: Length.convert(1.0, Unit.MM, Unit.FREE))
        self.assertEqual(math.pi, Length.convert(math.pi, Unit.FREE, Unit.FREE))

# ----------------------------------------------------------------------------------------------------------------------
