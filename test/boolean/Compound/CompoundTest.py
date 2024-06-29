from ScadTestCase import ScadTestCase
from super_scad.boolean.Compound import Compound
from super_scad.d3.Cube import Cube
from super_scad.d3.Sphere import Sphere
from super_scad.Scad import Scad
from super_scad.transformation.Translate3D import Translate3D
from super_scad.Unit import Unit


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

        scad = Scad(unit=Unit.MM)
        compound = Compound(children=[Cube(size=2, center=True),
                                      Translate3D(x=5, child=Sphere(radius=1))])

        scad.run_super_scad(compound, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
