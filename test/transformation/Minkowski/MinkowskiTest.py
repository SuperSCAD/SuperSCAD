from ScadTestCase import ScadTestCase
from super_scad.d3.Cuboid import Cuboid
from super_scad.d3.Cylinder import Cylinder
from super_scad.scad.Scad import Scad
from super_scad.scad.Unit import Unit
from super_scad.transformation.Minkowski import Minkowski
from super_scad.type.Size3 import Size3


class MinkowskiTest(ScadTestCase):
    """
    test case for minkowski.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testMinkowski(self):
        """
        Test case for minkowski without convexity.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit_length_final=Unit.MM)
        minkowski = Minkowski(children=[Cuboid(size=Size3(10, 10, 1)),
                                        Cylinder(radius=2.0, height=1.0)])

        scad.run_super_scad(minkowski, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testMinkowskiWithConvexity(self):
        """
        Test case for minkowski with convexity.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit_length_final=Unit.MM)
        minkowski = Minkowski(convexity=10,
                              children=[Cuboid(size=Size3(10, 10, 1)),
                                        Cylinder(radius=2.0, height=1.0)])

        scad.run_super_scad(minkowski, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
