from ScadTestCase import ScadTestCase
from super_scad.boolean.Difference import Difference
from super_scad.d3.Cylinder import Cylinder
from super_scad.scad.Scad import Scad
from super_scad.scad.Unit import Unit
from super_scad.transformation.Rotate3D import Rotate3D


class DifferenceTest(ScadTestCase):
    """
    Test cases for Difference.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testDifference(self):
        """
        The test case for Difference.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        difference = Difference(children=[Cylinder(height=4, radius=1, center=True, fn=100),
                                          Rotate3D(angle_x=90,
                                                   child=Cylinder(height=4, radius=0.9, center=True, fn=100))])

        scad.run_super_scad(difference, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
