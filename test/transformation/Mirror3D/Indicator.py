from super_scad.d3.Polyhedron import Polyhedron
from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.scad.Unit import Unit
from super_scad.transformation.Translate3D import Translate3D
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

        point0 = Point3(20.0, 20.0, 0.0)
        point1 = Point3(20.0, 0.0, 0.0)
        point2 = Point3(0.0, 0.0, 0.0)
        point3 = Point3(0.0, 20.0, 0.0)
        point4 = Point3(20.0, 20.0, 20.0)

        faces = [[point0, point1, point4],
                 [point1, point2, point4],
                 [point2, point3, point4],
                 [point3, point0, point4],
                 [point1, point0, point3],
                 [point2, point1, point3]]

        return Translate3D(x=10.0,
                           y=10.0,
                           z=10.0,
                           child=Polyhedron(faces=faces))

# ----------------------------------------------------------------------------------------------------------------------
