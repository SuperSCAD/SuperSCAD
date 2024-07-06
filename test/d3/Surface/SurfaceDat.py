from super_scad.d3.Surface import Surface
from super_scad.scad.Context import Context
from super_scad.scad.ScadObject import ScadObject


class SurfaceDat(ScadObject):
    """
    Paints slot.stl
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        """
        Object constructor.
        """
        ScadObject.__init__(self)

        self.surface: Surface | None = None

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        self.surface = Surface(path=context.resolve_path('../../surface.dat'),
                               center=True,
                               convexity=5)

        return self.surface

# ----------------------------------------------------------------------------------------------------------------------
