from ScadTestCase import ScadTestCase
from super_scad.boolean.Compound import Compound
from super_scad.boolean.Difference import Difference
from super_scad.d3.Cube import Cube
from super_scad.d3.Cylinder import Cylinder
from super_scad.other.Modify import Modify
from super_scad.scad.Scad import Scad
from super_scad.scad.Unit import Unit
from super_scad.transformation.Rotate3D import Rotate3D
from super_scad.transformation.Translate3D import Translate3D


class ModifyTest(ScadTestCase):
    """
    Test case for Modify.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testTransparentModifier(self):
        """
        Test the transparent modifier.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit_length_final=Unit.MM)
        difference = Difference(children=[Cylinder(height=12,
                                                   radius=5,
                                                   center=True,
                                                   fn=100),
                                          Rotate3D(angle_x=90,
                                                   child=Cylinder(height=15,
                                                                  radius=1,
                                                                  center=True,
                                                                  fn=100)),
                                          Modify(transparent=True,
                                                 child=Rotate3D(angle_y=90,
                                                                child=Cylinder(height=15,
                                                                               radius=3,
                                                                               center=True,
                                                                               fn=100)))])

        scad.run_super_scad(difference, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testHighlightModifier(self):
        """
        Test the highlight modifier.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit_length_final=Unit.MM)
        difference = Difference(children=[Cylinder(height=12,
                                                   radius=5,
                                                   center=True,
                                                   fn=100),
                                          Rotate3D(angle_x=90,
                                                   child=Cylinder(height=15,
                                                                  radius=1,
                                                                  center=True,
                                                                  fn=100)),
                                          Modify(highlight=True,
                                                 child=Rotate3D(angle_y=90,
                                                                child=Cylinder(height=15,
                                                                               radius=3,
                                                                               center=True,
                                                                               fn=100)))])

        scad.run_super_scad(difference, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testShowOnlyModifier(self):
        """
        Test the show only modifier.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit_length_final=Unit.MM)
        difference = \
            Difference(children=[Cube(size=10,
                                      center=True),
                                 Translate3D(z=5,
                                             child=Modify(show_only=True,
                                                          child=Rotate3D(angle_x=90,
                                                                         child=Modify(debug=True,
                                                                                      child=Cylinder(height=20,
                                                                                                     radius=2,
                                                                                                     center=True,
                                                                                                     fn=40)))))])

        scad.run_super_scad(difference, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testDisableModifier(self):
        """
        Test the disable modifier.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit_length_final=Unit.MM)
        cube = Cube(size=10, center=True)
        cylinders = Compound(children=[Rotate3D(angle_y=90,
                                                child=Cylinder(height=20,
                                                               radius=2,
                                                               center=True,
                                                               fn=40)),
                                       Modify(disable=True,
                                              child=Rotate3D(angle_x=90,
                                                             child=Modify(highlight=True,
                                                                          child=Cylinder(height=20,
                                                                                         radius=2,
                                                                                         center=True,
                                                                                         fn=40))))])
        difference = Difference(children=[cube, Translate3D(z=5, child=cylinders)])

        scad.run_super_scad(difference, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testNoModifying(self):
        """
        Test the modifier without modifications.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit_length_final=Unit.MM)
        cylinder = Modify(child=Cylinder(height=20, radius=2, center=True, fn=40))

        scad.run_super_scad(cylinder, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
