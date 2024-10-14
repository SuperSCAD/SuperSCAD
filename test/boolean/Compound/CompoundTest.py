from ScadTestCase import ScadTestCase
from super_scad.boolean.Compound import Compound
from super_scad.d3.Cube import Cube
from super_scad.d3.Sphere import Sphere
from super_scad.scad.Scad import Scad
from super_scad.scad.Unit import Unit
from super_scad.transformation.Translate3D import Translate3D


class CompoundTest(ScadTestCase):
    """
    Test cases for Compound.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testCompound(self):
        """
        The test case for Compound.
        """
        path_actual, path_expected = self.paths()

        scad = self.create_scad()
        compound = Compound(children=[Cube(size=2, center=True),
                                      Translate3D(x=5, child=Sphere(radius=1))])

        scad.run_super_scad(compound, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
