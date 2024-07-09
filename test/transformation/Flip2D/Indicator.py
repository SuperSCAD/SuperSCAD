from super_scad.d2.RightTriangle import RightTriangle
from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.scad.Unit import Unit
from super_scad.transformation.Translate2D import Translate2D


class Indicator(ScadWidget):
    """
    Widget for an object with clear left/right and up/down indication.
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

        return Translate2D(x=5.0, y=5.0, child=RightTriangle(width=10.0, depth=5.0))

    # ------------------------------------------------------------------------------------------------------------------
