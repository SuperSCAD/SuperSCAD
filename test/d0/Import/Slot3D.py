from super_scad.d0.Import import Import
from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.transformation.Paint import Paint
from super_scad.type.Color import Color


class Slot3D(ScadWidget):
    """
    Paints slot.stl
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        """
        Object constructor.
        """
        ScadWidget.__init__(self)

        self.import3d: Import | None = None

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        self.import3d = Import(path=context.resolve_path('../../slot.stl'), convexity=10)

        return Paint(color=Color(color='Fuchsia'), child=self.import3d)

# ----------------------------------------------------------------------------------------------------------------------
