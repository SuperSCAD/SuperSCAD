from super_scad.Context import Context
from super_scad.d3.Import3D import Import3D
from super_scad.ScadObject import ScadObject
from super_scad.transformation.Paint import Paint
from super_scad.type.Color import Color


class Slot3D(ScadObject):
    """
    Paints slot.stl
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        """
        Object constructor.
        """
        ScadObject.__init__(self)

        self.import3d: Import3D | None = None

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        self.import3d = Import3D(path=context.resolve_path('../../slot.stl'), convexity=10)

        return Paint(color=Color(color='Fuchsia'), child=self.import3d)

# ----------------------------------------------------------------------------------------------------------------------
