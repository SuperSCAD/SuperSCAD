from super_scad.d2.Polygon import Polygon
from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.scad.Unit import Unit
from super_scad.type.Point2 import Point2


class ImperialUnitPolygon(ScadWidget):
    """
    Class for an imperial unit polygon.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self) -> None:
        """
        Object constructor.
        """
        ScadWidget.__init__(self, args={})

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        Context.set_unit_length_current(Unit.INCH)

        return Polygon(primary=[Point2(0.0, 0.0),
                                Point2(2.0, 0.0),
                                Point2(2.0, 2.0),
                                Point2(0.0, 2.0)],
                       secondary=[Point2(0.5, 0.5),
                                  Point2(1.5, 0.5),
                                  Point2(1.5, 1.5),
                                  Point2(0.5, 1.5)],
                       convexity=4)

# ----------------------------------------------------------------------------------------------------------------------
