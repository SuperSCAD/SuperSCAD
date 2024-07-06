from d3.RotateExtrude.ImperialUnitDonut import ImperialUnitDonut
from ScadTestCase import ScadTestCase
from super_scad.boolean.Union import Union
from super_scad.d2.Circle import Circle
from super_scad.d3.Cylinder import Cylinder
from super_scad.d3.RotateExtrude import RotateExtrude
from super_scad.scad.Scad import Scad
from super_scad.scad.Unit import Unit
from super_scad.transformation.Rotate3D import Rotate3D
from super_scad.transformation.Translate2D import Translate2D
from super_scad.transformation.Translate3D import Translate3D


class RotateExtrudeTest(ScadTestCase):
    """
    Test cases for RotateExtrude.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testSample1(self):
        """
        Test sample 1 from the OpenSCAD cheatsheet.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit_length_final=Unit.MM)
        extrude = RotateExtrude(convexity=10,
                                child=Translate2D(x=2.0, child=Circle(radius=1.0)))

        self.assertAlmostEqual(360.0, extrude.angle)
        self.assertEqual(10, extrude.convexity)
        self.assertIsNone(extrude.fa)
        self.assertIsNone(extrude.fs)
        self.assertIsNone(extrude.fn)

        scad.run_super_scad(extrude, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testSample2(self):
        """
        Test sample 2 from the OpenSCAD cheatsheet.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit_length_final=Unit.MM)
        extrude = RotateExtrude(convexity=10,
                                fn=100,
                                child=Translate2D(x=2.0, child=Circle(radius=1.0, fn=100)))

        self.assertAlmostEqual(360.0, extrude.angle)
        self.assertEqual(10, extrude.convexity)
        self.assertIsNone(extrude.fa)
        self.assertIsNone(extrude.fs)
        self.assertEqual(100, extrude.fn)

        scad.run_super_scad(extrude, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testSample3(self):
        """
        Test sample 3 from the OpenSCAD cheatsheet.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit_length_final=Unit.MM)
        eps = 0.01
        union = Union(children=[Translate3D(x=eps,
                                            y=60.0,
                                            child=RotateExtrude(angle=270.0,
                                                                convexity=10,
                                                                child=Translate2D(x=40.0,
                                                                                  child=Circle(radius=10.0)))),
                                RotateExtrude(angle=90.0,
                                              convexity=10,
                                              child=Translate2D(x=20.0,
                                                                child=Circle(radius=10.0))),
                                Translate2D(x=20.0,
                                            y=eps,
                                            child=Rotate3D(angle_x=90.0,
                                                           child=Cylinder(height=80 + eps,
                                                                          radius=10.0)))])

        scad.run_super_scad(union, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialMetricLinearExtrude(self):
        """
        Test for an extrude imperial unit cube in metric units.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit_length_final=Unit.MM)
        extrude = ImperialUnitDonut()

        scad.run_super_scad(extrude, path_actual)
        self.assertAlmostEqual(0.254, extrude.imperial_unit_donut.fs)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialImperialLinearExtrude(self):
        """
        Test for an extruded imperial unit donut in imperial units.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit_length_final=Unit.INCH)
        extrude = ImperialUnitDonut()

        scad.run_super_scad(extrude, path_actual)
        self.assertAlmostEqual(0.01, extrude.imperial_unit_donut.fs)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
