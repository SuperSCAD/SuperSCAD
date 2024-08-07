from super_scad.d0.Import import Import
from super_scad.d3.LinearExtrude import LinearExtrude
from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget


class Slot2D(ScadWidget):
    """
    Extrudes Sample009.dxf.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        """
        Object constructor.
        """
        ScadWidget.__init__(self)

        self.import2d: Import | None = None

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        self.import2d = Import(path=context.resolve_path('../../slot.dxf'),
                               convexity=10,
                               layer='Sketch')

        return LinearExtrude(height=5.0, center=True, convexity=10, child=self.import2d)

# ----------------------------------------------------------------------------------------------------------------------
