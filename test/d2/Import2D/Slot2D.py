from super_scad.Context import Context
from super_scad.d2.Import2D import Import2D
from super_scad.d3.LinearExtrude import LinearExtrude
from super_scad.ScadObject import ScadObject


class Slot2D(ScadObject):
    """
    Extrudes Sample009.dxf.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        return LinearExtrude(height=5.0,
                             center=True,
                             convexity=10,
                             child=Import2D(path=context.resolve_path('../../slot.dxf'),
                                            layer='Sketch'))

# ----------------------------------------------------------------------------------------------------------------------
