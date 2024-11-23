from super_scad.d2.Polygon import Polygon
from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.scad.Unit import Unit
from super_scad.transformation.Translate2D import Translate2D
from super_scad.type.Vector2 import Vector2


class Indicator(ScadWidget):
    """
    Widget for an object with clear left/right and up/down indication.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, unit=Unit.MM):
        """
        Object constructor.
        """
        ScadWidget.__init__(self)

        self._unit = unit

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        Context.set_unit_length_current(self._unit)

        return Translate2D(x=5.0, y=5.0, child=Polygon(points=[Vector2(0.0, 0.0),
                                                               Vector2(10.0, 0.0),
                                                               Vector2(0.0, 5.0)]))

    # ------------------------------------------------------------------------------------------------------------------
