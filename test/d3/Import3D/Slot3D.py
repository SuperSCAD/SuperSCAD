from super_scad.Context import Context
from super_scad.d2.Import2D import Import2D
from super_scad.d3.Import3D import Import3D
from super_scad.ScadObject import ScadObject
from super_scad.transformation.Paint import Paint
from super_scad.type.Color import Color


class Slot3D(ScadObject):
    """
    Paints slot.stl
    """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        return Paint(color=Color(color='Fuchsia'),
                     child=Import3D(path=context.resolve_path('../../slot.stl')))

# ----------------------------------------------------------------------------------------------------------------------
