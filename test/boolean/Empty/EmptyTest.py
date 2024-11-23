from ScadTestCase import ScadTestCase
from super_scad.boolean.Empty import Empty


class EmptyTest(ScadTestCase):
    """
    Test cases for Empty.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_empty(self):
        """
        The test case for Empty.
        """
        scad = self.create_scad()

        empty = Empty()

        path_actual, path_expected = self.paths()
        scad.run_super_scad(empty, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
