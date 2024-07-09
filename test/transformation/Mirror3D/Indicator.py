from super_scad.d3.Polyhedron import Polyhedron
from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.scad.Unit import Unit
from super_scad.transformation.Translate3D import Translate3D
from super_scad.type.Face3 import Face3
from super_scad.type.Point3 import Point3


class Indicator(ScadWidget):
    """
    Widget for creating an object with clear left/right and up/down indication.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, unit=Unit.MM):
        """
        Object constructor.
        """
        ScadWidget.__init__(self, args=locals())

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        Context.set_unit_length_current(self._args['unit'])

        return Translate3D(x=10.0,
                           y=10.0,
                           z=10.0,
                           child=Polyhedron(points=[Point3(20.0, 20.0, 0.0),
                                                    Point3(20.0, 0.0, 0.0),
                                                    Point3(0.0, 0.0, 0.0),
                                                    Point3(0.0, 20.0, 0.0),
                                                    Point3(20.0, 20.0, 20.0)],
                                            faces=[Face3([0, 1, 4]),
                                                   Face3([1, 2, 4]),
                                                   Face3([2, 3, 4]),
                                                   Face3([3, 0, 4]),
                                                   Face3([1, 0, 3]),
                                                   Face3([2, 1, 3])]))

# ----------------------------------------------------------------------------------------------------------------------
