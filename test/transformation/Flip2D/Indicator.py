from super_scad.scad.Context import Context
from super_scad.d2.RightTriangle import RightTriangle
from super_scad.scad.ScadObject import ScadObject
from super_scad.transformation.Translate2D import Translate2D
from super_scad.scad.Unit import Unit


class Indicator(ScadObject):
    """
    Class for an object with clear left/right and up/down indication.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, unit=Unit.MM):
        """
        Object constructor.
        """
        ScadObject.__init__(self, args=locals())

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        context.unit = self._args['unit']

        return Translate2D(x=5.0, y=5.0, child=RightTriangle(width=10.0, depth=5.0))

    # ------------------------------------------------------------------------------------------------------------------
