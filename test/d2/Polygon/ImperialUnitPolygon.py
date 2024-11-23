from super_scad.d2.Polygon import Polygon
from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.scad.Unit import Unit
from super_scad.type.Vector2 import Vector2


class ImperialUnitPolygon(ScadWidget):
    """
    Class for an imperial unit polygon.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self) -> None:
        """
        Object constructor.
        """
        ScadWidget.__init__(self)

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        Context.set_unit_length_current(Unit.INCH)

        return Polygon(primary=[Vector2(0.0, 0.0),
                                Vector2(2.0, 0.0),
                                Vector2(2.0, 2.0),
                                Vector2(0.0, 2.0)],
                       secondary=[Vector2(0.5, 0.5),
                                  Vector2(1.5, 0.5),
                                  Vector2(1.5, 1.5),
                                  Vector2(0.5, 1.5)],
                       convexity=4)

# ----------------------------------------------------------------------------------------------------------------------
