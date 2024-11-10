import math

from ScadTestCase import ScadTestCase
from super_scad.other.Echo import Echo


class EchoTest(ScadTestCase):
    """
    Test cases for Echo.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_echo(self):
        """
        The test case for Echo.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        echo = Echo(message='Hello, world!', pi=math.pi, quot="'", double_qoute='"')

        scad.run_super_scad(echo, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
