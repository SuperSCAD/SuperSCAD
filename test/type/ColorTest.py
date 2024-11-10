import unittest

from super_scad.type.Color import Color


class ColorTestCase(unittest.TestCase):
    """
    Test cases for Color.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_all_formats(self):
        """
        Test all format of lightslategray.
        """
        self.assertEqual('[0.467, 0.533, 0.6, 1.0]', str(Color((119, 136, 153))))
        self.assertEqual('[0.467, 0.533, 0.6, 1.0]', str(Color((119, 136, 153))))
        self.assertEqual('[0.467, 0.533, 0.6, 1.0]', str(Color([119, 136, 153])))
        self.assertEqual('[0.467, 0.533, 0.6, 1.0]', str(Color((119, 136, 153, 1.0))))
        self.assertEqual('[0.467, 0.533, 0.6, 1.0]', str(Color([119, 136, 153, 1.0])))
        self.assertEqual('[0.467, 0.533, 0.6, 1.0]', str(Color((0.467, 0.533, 0.6))))
        self.assertEqual('[0.467, 0.533, 0.6, 1.0]', str(Color([0.467, 0.533, 0.6])))
        self.assertEqual('[0.467, 0.533, 0.6, 1.0]', str(Color((0.467, 0.533, 0.6, 1.0))))
        self.assertEqual('[0.467, 0.533, 0.6, 1.0]', str(Color([0.467, 0.533, 0.6, 1.0])))
        self.assertEqual('[0.467, 0.533, 0.6, 1.0]', str(Color('#789')))
        self.assertEqual('[0.467, 0.533, 0.6, 1.0]', str(Color('#789F')))
        self.assertEqual('[0.467, 0.533, 0.6, 1.0]', str(Color('#789f')))
        self.assertEqual('[0.467, 0.533, 0.6, 1.0]', str(Color('#778899')))
        self.assertEqual('[0.467, 0.533, 0.6, 1.0]', str(Color('#778899FF')))
        self.assertEqual('[0.467, 0.533, 0.6, 1.0]', str(Color('#778899ff')))
        self.assertEqual('[0.467, 0.533, 0.6, 1.0]', str(Color('lightslategray')))
        self.assertEqual('[0.467, 0.533, 0.6, 1.0]', str(Color('lightslategrey')))
        self.assertEqual('[0.467, 0.533, 0.6, 1.0]', str(Color('LightSlateGray')))
        self.assertEqual('[0.467, 0.533, 0.6, 1.0]', str(Color('LightSlateGrey')))
        self.assertEqual('[0.467, 0.533, 0.6, 1.0]', str(Color('LIGHTSLATEGRAY')))
        self.assertEqual('[0.467, 0.533, 0.6, 1.0]', str(Color('LIGHTSLATEGREY')))
        self.assertEqual('[0.467, 0.533, 0.6, 1.0]', str(Color(Color('#789'))))

    # ------------------------------------------------------------------------------------------------------------------
    def testAlphaPrecedence(self):
        """
        Test alpha parameter precedence over alpha in color.
        """
        color = Color((119, 136, 153, 1.0), alpha=0.5)
        self.assertAlmostEqual(0.5, color.alpha)

        color = Color([119, 136, 153, 1.0], alpha=0.5)
        self.assertAlmostEqual(0.5, color.alpha)

        color = Color((0.467, 0.533, 0.6, 1.0), alpha=0.5)
        self.assertAlmostEqual(0.5, color.alpha)

        color = Color([0.467, 0.533, 0.6, 1.0], alpha=0.5)
        self.assertAlmostEqual(0.5, color.alpha)

        color = Color('#778899FF', alpha=0.5)
        self.assertAlmostEqual(0.5, color.alpha)

    # ------------------------------------------------------------------------------------------------------------------
    def testComponents(self):
        """
        Test components of a color.
        """
        color = Color('#778899', alpha=0.5)
        self.assertAlmostEqual(119.0 / 255.0, color.red)
        self.assertAlmostEqual(136.0 / 255.0, color.green)
        self.assertAlmostEqual(0.6, color.blue)
        self.assertAlmostEqual(0.5, color.alpha)

    # ------------------------------------------------------------------------------------------------------------------
    def testNormalization(self):
        """
        Test normalization of a color components.
        """
        self.assertEqual('[1.0, 1.0, 1.0, 1.0]', str(Color((1000, 1000, 1000))))
        self.assertEqual('[1.0, 1.0, 1.0, 1.0]', str(Color([1000, 1000, 1000])))
        self.assertEqual('[0.0, 0.0, 0.0, 1.0]', str(Color((-1000, -1000, -1000))))
        self.assertEqual('[0.0, 0.0, 0.0, 1.0]', str(Color([-1000, -1000, -1000])))
        self.assertEqual('[1.0, 1.0, 1.0, 1.0]', str(Color((1000, 1000, 1000, 1000))))
        self.assertEqual('[1.0, 1.0, 1.0, 1.0]', str(Color([1000, 1000, 1000, 1000])))
        self.assertEqual('[0.0, 0.0, 0.0, 0.0]', str(Color((-1000, -1000, -1000, -1000))))
        self.assertEqual('[0.0, 0.0, 0.0, 0.0]', str(Color([-1000, -1000, -1000, -1000])))

    # ------------------------------------------------------------------------------------------------------------------
    def testMultiplication(self):
        """
        Test multiplication of a color.
        """
        color = Color((119, 136, 153, 0.5))
        self.assertEqual('[0.467, 0.533, 0.6, 0.5]', str(color))
        self.assertEqual('[0.373, 0.427, 0.48, 0.5]', str(color * 0.8))

    # ------------------------------------------------------------------------------------------------------------------
    def testDivision(self):
        """
        Test division of a color.
        """
        color = Color((119, 136, 153, 0.5))
        self.assertEqual('[0.467, 0.533, 0.6, 0.5]', str(color))
        self.assertEqual('[0.373, 0.427, 0.48, 0.5]', str(color / 1.25))

    # ------------------------------------------------------------------------------------------------------------------
    def testInvalidColor1(self):
        """
        Test color with invalid color.
        """
        self.assertRaises(ValueError, lambda: Color(['red', 'green', 'blue']))
        self.assertRaises(ValueError, lambda: Color(['red', 'green', 'blue', 1.0]))
        self.assertRaises(ValueError, lambda: Color(('red', 'green', 'blue')))
        self.assertRaises(ValueError, lambda: Color(('red', 'green', 'blue', 1.0)))
        self.assertRaises(ValueError, lambda: Color('#'))
        self.assertRaises(ValueError, lambda: Color('#1234567890'))
        self.assertRaises(ValueError, lambda: Color(self))

# ----------------------------------------------------------------------------------------------------------------------
