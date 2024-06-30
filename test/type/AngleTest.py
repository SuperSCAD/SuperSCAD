import unittest

from super_scad.type.Angle import Angle


class AngleTest(unittest.TestCase):
    """
    Test cases for Angle.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testNormalize(self):
        """
        Test cases for normalize.
        """
        for angle in [0.0, 90.0, 180.0, 270.0, 45.0]:
            self.assertAlmostEqual(angle, Angle.normalize(angle))
            self.assertAlmostEqual(angle, Angle.normalize(angle + 360.0))
            self.assertAlmostEqual(angle, Angle.normalize(angle + 720.0))
            self.assertAlmostEqual(angle, Angle.normalize(angle - 360.0))
            self.assertAlmostEqual(angle, Angle.normalize(angle - 720.0))

# ----------------------------------------------------------------------------------------------------------------------
