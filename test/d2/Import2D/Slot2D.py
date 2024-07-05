from super_scad.Context import Context
from super_scad.d2.Import2D import Import2D
from super_scad.d3.LinearExtrude import LinearExtrude
from super_scad.ScadObject import ScadObject


class Slot2D(ScadObject):
    """
    Extrudes Sample009.dxf.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        """
        Object constructor.
        """
        ScadObject.__init__(self)

        self.import2d: Import2D | None = None

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        self.import2d = Import2D(path=context.resolve_path('../../slot.dxf'),
                                 convexity=10,
                                 layer='Sketch')

        return LinearExtrude(height=5.0, center=True, convexity=10, child=self.import2d)

# ----------------------------------------------------------------------------------------------------------------------
