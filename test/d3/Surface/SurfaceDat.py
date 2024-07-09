from super_scad.d3.Surface import Surface
from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget


class SurfaceDat(ScadWidget):
    """
    Paints slot.stl
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        """
        Object constructor.
        """
        ScadWidget.__init__(self)

        self.surface: Surface | None = None

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        self.surface = Surface(path=context.resolve_path('../../surface.dat'),
                               center=True,
                               convexity=5)

        return self.surface

# ----------------------------------------------------------------------------------------------------------------------
