from ScadTestCase import ScadTestCase
from super_scad.d2.Rectangle import Rectangle
from super_scad.d2.Square import Square
from super_scad.util.YinYang import YinYang


class YinYangTest(ScadTestCase):
    """
    Test cases for YinYang.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_apply_negatives_positives(self):
        """
        Test apply_negatives_positives.
        """
        scad = self.create_scad()

        big_square = Square(size=100.0, center=True)
        little_square = Square(size=25.0, center=True)
        bar = Rectangle(width=120.0, depth=10.0, center=True)

        yin_yang = YinYang()
        yin_yang += (little_square, bar)
        body = yin_yang.apply_negatives_positives(big_square)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(body, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_apply_positives_negatives(self):
        """
        Test apply_positives_negatives and adding None values.
        """
        scad = self.create_scad()

        big_square = Square(size=100.0, center=True)
        little_square = Square(size=25.0, center=True)
        bar = Rectangle(width=120.0, depth=10.0, center=True)

        yin_yang = YinYang()
        yin_yang += (little_square, None)
        yin_yang += (None, bar)
        body = yin_yang.apply_positives_negatives(big_square)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(body, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_apply_negatives_positives_positives_only(self):
        """
        Test apply_negatives_positives with positives only.
        """
        scad = self.create_scad()

        big_square = Square(size=100.0, center=True)
        bar = Rectangle(width=120.0, depth=10.0, center=True)

        yin_yang = YinYang()
        yin_yang += (None, bar)
        body = yin_yang.apply_negatives_positives(big_square)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(body, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_apply_negatives_positives_negatives_only(self):
        """
        Test apply_negatives_positives with negatives only.
        """
        scad = self.create_scad()

        big_square = Square(size=100.0, center=True)
        little_square = Square(size=25.0, center=True)

        yin_yang = YinYang()
        yin_yang += (little_square, None)
        body = yin_yang.apply_negatives_positives(big_square)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(body, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_apply_positives_negatives_positives_only(self):
        """
        Test apply_positives_negatives with positives only.
        """
        scad = self.create_scad()

        big_square = Square(size=100.0, center=True)
        bar = Rectangle(width=120.0, depth=10.0, center=True)

        yin_yang = YinYang()
        yin_yang += (None, bar)
        body = yin_yang.apply_positives_negatives(big_square)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(body, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_apply_positives_negatives_negatives_only(self):
        """
        Test apply_positives_negatives with negatives only.
        """
        scad = self.create_scad()

        big_square = Square(size=100.0, center=True)
        little_square = Square(size=25.0, center=True)

        yin_yang = YinYang()
        yin_yang += (little_square, None)
        body = yin_yang.apply_positives_negatives(big_square)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(body, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
