from super_scad.d3.Polyhedron import Polyhedron
from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.scad.Unit import Unit
from super_scad.type.Point3 import Point3


class ImperialUnitCube(ScadWidget):
    """
    An imperial unit cube.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        """
        Object constructor.
        """
        ScadWidget.__init__(self, args=locals())

        self.imperial_unit_cube: Polyhedron | None = None
        """
        The imperial unit cube.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        Context.set_unit_length_current(Unit.INCH)

        p0 = Point3(0.0, 0.0, 0.0)
        p1 = Point3(1.0, 0.0, 0.0)
        p2 = Point3(1.0, 1.0, 0.0)
        p3 = Point3(0.0, 1.0, 0.0)
        p4 = Point3(0.0, 0.0, 1.0)
        p5 = Point3(1.0, 0.0, 1.0)
        p6 = Point3(1.0, 1.0, 1.0)
        p7 = Point3(0.0, 1.0, 1.0)
        faces = [[p0, p1, p2, p3],  # bottom
                 [p4, p5, p1, p0],  # front
                 [p7, p6, p5, p4],  # top
                 [p5, p6, p2, p1],  # right
                 [p6, p7, p3, p2],  # back
                 [p7, p4, p0, p3]]  # left

        self.imperial_unit_cube = Polyhedron(faces=faces)

        return self.imperial_unit_cube

# ----------------------------------------------------------------------------------------------------------------------
