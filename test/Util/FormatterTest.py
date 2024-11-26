import math
import unittest

from super_scad.scad.Context import Context
from super_scad.type import Vector2, Vector3
from super_scad.util.Formatter import Formatter


class FormatterTest(unittest.TestCase):
    """
    Test the formatter
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_format_lengths(self):
        """
        Lengths must be formatted as floats.
        """
        context = Context()

        self.assertEqual(Formatter.format(context, 10, is_length=True), '10.0')
        self.assertEqual(Formatter.format(context, math.pi, is_length=True), '3.1416')
        self.assertEqual(Formatter.format(context, Vector2(1, 2), is_length=True), '[1.0, 2.0]')
        self.assertEqual(Formatter.format(context, Vector3(1, 2, 3), is_length=True), '[1.0, 2.0, 3.0]')

# ----------------------------------------------------------------------------------------------------------------------
