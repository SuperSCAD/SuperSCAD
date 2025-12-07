import math
import unittest

from super_scad.scad import Length
from super_scad.scad.Unit import Unit
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
    def test_metric_units(self):
        """
        The metric system is brilliant in its simplicity.
        """
        micrometer = Length.length_unit(Unit.UM)
        millimeter = Length.length_unit(Unit.MM)
        centimeter = Length.length_unit(Unit.CM)
        decimeter = Length.length_unit(Unit.DM)
        meter = Length.length_unit(Unit.M)
        kilometer = Length.length_unit(Unit.KM)

        self.assertAlmostEqual(millimeter.meters(), 1000.0 * micrometer.meters())
        self.assertAlmostEqual(centimeter.meters(), 10.0 * millimeter.meters())
        self.assertAlmostEqual(decimeter.meters(), 10.0 * centimeter.meters())
        self.assertAlmostEqual(meter.meters(), 10.0 * decimeter.meters())
        self.assertAlmostEqual(kilometer.meters(), 1000.0 * meter.meters())

        # The meter defines its self.
        self.assertEqual(1.0, meter.meters())

        self.assertEqual(micrometer.symbol(), 'µm')
        self.assertEqual(millimeter.symbol(), 'mm')
        self.assertEqual(centimeter.symbol(), 'cm')
        self.assertEqual(decimeter.symbol(), 'dm')
        self.assertEqual(meter.symbol(), 'm')
        self.assertEqual(kilometer.symbol(), 'km')

    # ------------------------------------------------------------------------------------------------------------------
    def test_science_units(self):
        """
        The unit of length used in science.
        """
        angstrom = Length.length_unit(Unit.ANGSTROM)
        light_year = Length.length_unit(Unit.LIGHT_YEAR)
        meter = Length.length_unit(Unit.M)
        astronomical_unit = Length.length_unit(Unit.ASTRONOMICAL_UNIT)
        parsec = Length.length_unit(Unit.PARSEC)
        attoparsec = Length.length_unit(Unit.ATTOPARSEC)

        c = 299792458.0  # Speed of light in vacuum.

        self.assertAlmostEqual(meter.meters(), 1E10 * angstrom.meters())
        self.assertAlmostEqual(light_year.meters(), 365.25 * 24 * 60 * 60 * c * meter.meters())
        self.assertAlmostEqual(499.0, astronomical_unit.meters() / c, places=2)
        self.assertAlmostEqual((648000 / math.pi) * astronomical_unit.meters(), parsec.meters())
        self.assertAlmostEqual(1E-18, attoparsec.meters() / parsec.meters())
        self.assertAlmostEqual(3.086, 100 * attoparsec.meters(), 3)

        self.assertEqual(angstrom.symbol(), 'Å')
        self.assertEqual(light_year.symbol(), 'ly')
        self.assertEqual(meter.symbol(), 'm')
        self.assertEqual(astronomical_unit.symbol(), 'AU')
        self.assertEqual(meter.symbol(), 'm')
        self.assertEqual(parsec.symbol(), 'pc')
        self.assertEqual(attoparsec.symbol(), 'apc')

    # ------------------------------------------------------------------------------------------------------------------
    def test_insanity(self):
        """
        The imperial system makes satellites crash on Mars.
        """
        thou = Length.length_unit(Unit.THOU)
        inch = Length.length_unit(Unit.INCH)
        foot = Length.length_unit(Unit.FOOT)
        yard = Length.length_unit(Unit.YARD)
        mile = Length.length_unit(Unit.MILE)

        self.assertAlmostEqual(inch.meters(), 1000.0 * thou.meters())
        self.assertAlmostEqual(foot.meters(), 12.0 * inch.meters())
        self.assertAlmostEqual(yard.meters(), 3.0 * foot.meters())
        self.assertAlmostEqual(mile.meters(), 5280.0 * foot.meters())

        # Note: the imperial system is defined in terms of the metric system.
        millimeter = MillimeterUnit()
        self.assertAlmostEqual(inch.meters(), 25.4 * millimeter.meters())

        self.assertEqual(thou.symbol(), 'thou')
        self.assertEqual(inch.symbol(), 'in')
        self.assertEqual(foot.symbol(), 'ft')
        self.assertEqual(yard.symbol(), 'yd')
        self.assertEqual(mile.symbol(), 'mi')

    # ------------------------------------------------------------------------------------------------------------------
    def test_chinese_length_units(self):
        """
        The imperial system lets you crash satellites on Mars.
        """
        li = Length.length_unit(Unit.LI)
        meter = Length.length_unit(Unit.M)

        self.assertAlmostEqual(li.meters(), 500.0 * meter.meters())

        self.assertEqual(li.symbol(), '里')

# ----------------------------------------------------------------------------------------------------------------------
