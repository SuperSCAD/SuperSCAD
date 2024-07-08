import math
import unittest

from super_scad.scad.unit.AngstromUnit import AngstromUnit
from super_scad.scad.unit.AstronomicalUnit import AstronomicalUnit
from super_scad.scad.unit.AttoparsecUnit import AttoparsecUnit
from super_scad.scad.unit.CentimeterUnit import CentimeterUnit
from super_scad.scad.unit.DecimeterUnit import DecimeterUnit
from super_scad.scad.unit.FootUnit import FootUnit
from super_scad.scad.unit.InchUnit import InchUnit
from super_scad.scad.unit.KilometerUnit import KilometerUnit
from super_scad.scad.unit.LightYearUnit import LightYearUnit
from super_scad.scad.unit.LiUnit import LiUnit
from super_scad.scad.unit.MeterUnit import MeterUnit
from super_scad.scad.unit.MicrometerUnit import MicrometerUnit
from super_scad.scad.unit.MileUnit import MileUnit
from super_scad.scad.unit.MillimeterUnit import MillimeterUnit
from super_scad.scad.unit.ParsecUnit import ParsecUnit
from super_scad.scad.unit.ThouUnit import ThouUnit
from super_scad.scad.unit.YardUnit import YardUnit


class UnitTest(unittest.TestCase):
    """
    Test case for unit tests.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testMetricUnits(self):
        """
        The metric system is brilliant in its simplicity.
        """
        micrometer = MicrometerUnit()
        millimeter = MillimeterUnit()
        centimeter = CentimeterUnit()
        decimeter = DecimeterUnit()
        meter = MeterUnit()
        kilometer = KilometerUnit()

        self.assertAlmostEqual(millimeter.meters(), 1000.0 * micrometer.meters())
        self.assertAlmostEqual(centimeter.meters(), 10.0 * millimeter.meters())
        self.assertAlmostEqual(decimeter.meters(), 10.0 * centimeter.meters())
        self.assertAlmostEqual(meter.meters(), 10.0 * decimeter.meters())
        self.assertAlmostEqual(kilometer.meters(), 1000.0 * meter.meters())

        # The meter defines its self.
        self.assertEqual(1.0, meter.meters())

    # ------------------------------------------------------------------------------------------------------------------
    def testScienceUnits(self):
        """
        The unit of length used in science.
        """
        angstrom = AngstromUnit()
        light_year = LightYearUnit()
        meter = MeterUnit()
        astronomical_unit = AstronomicalUnit()
        parsec = ParsecUnit()
        attoparsec = AttoparsecUnit()

        c = 299792458.0  # Speed of light in vacuum.

        self.assertAlmostEqual(meter.meters(), 1E10 * angstrom.meters())
        self.assertAlmostEqual(light_year.meters(), 365.25 * 24 * 60 * 60 * c * meter.meters())
        self.assertAlmostEqual(499.0, astronomical_unit.meters() / c, places=2)
        self.assertAlmostEqual((648000 / math.pi) * astronomical_unit.meters(), parsec.meters())
        self.assertAlmostEqual(1E-18, attoparsec.meters() / parsec.meters())
        self.assertAlmostEqual(3.086, 100 * attoparsec.meters(), 3)

    # ------------------------------------------------------------------------------------------------------------------
    def testInsanity(self):
        """
        The imperial system makes satellites crash on Mars.
        """
        thou = ThouUnit()
        inch = InchUnit()
        foot = FootUnit()
        yard = YardUnit()
        mile = MileUnit()

        self.assertAlmostEqual(inch.meters(), 1000.0 * thou.meters())
        self.assertAlmostEqual(foot.meters(), 12.0 * inch.meters())
        self.assertAlmostEqual(yard.meters(), 3.0 * foot.meters())
        self.assertAlmostEqual(mile.meters(), 5280.0 * foot.meters())

        # Note: the imperial system is defined in terms of the metric system.
        millimeter = MillimeterUnit()
        self.assertAlmostEqual(inch.meters(), 25.4 * millimeter.meters())

    # ------------------------------------------------------------------------------------------------------------------
    def testChineseLengthUnits(self):
        """
        The imperial system lets you crash satellites on Mars.
        """
        li = LiUnit()
        meter = MeterUnit()

        self.assertAlmostEqual(li.meters(), 500.0 * meter.meters())

# ----------------------------------------------------------------------------------------------------------------------
