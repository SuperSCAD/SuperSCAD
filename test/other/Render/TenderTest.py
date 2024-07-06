from ScadTestCase import ScadTestCase
from super_scad.boolean.Difference import Difference
from super_scad.d3.Cuboid import Cuboid
from super_scad.d3.Cylinder import Cylinder
from super_scad.d3.Sphere import Sphere
from super_scad.other.Render import Render
from super_scad.scad.Scad import Scad
from super_scad.scad.Unit import Unit
from super_scad.transformation.Translate3D import Translate3D


class TenderTest(ScadTestCase):
    """
    Test cases for Render.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testRender(self):
        """
        The unit test for Render.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(unit=Unit.MM)
        radius = 10.0
        render = Render(convexity=2,
                        child=Difference(children=[Cuboid(width=20,
                                                          depth=20,
                                                          height=150,
                                                          center=True),
                                                   Translate3D(x=-radius,
                                                               y=-radius,
                                                               child=Cylinder(radius=radius,
                                                                              height=80,
                                                                              center=True)),
                                                   Translate3D(x=-radius,
                                                               y=-radius,
                                                               z=40,
                                                               child=Sphere(radius=radius)),
                                                   Translate3D(x=-radius,
                                                               y=-radius,
                                                               z=-40,
                                                               child=Sphere(radius=radius))]))

        self.assertEqual(2, render.convexity)

        scad.run_super_scad(render, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
