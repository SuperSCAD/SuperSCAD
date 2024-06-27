from super_scad.Context import Context
from super_scad.d2.Square import Square
from super_scad.ScadObject import ScadObject
from super_scad.Unit import Unit


class ImperialUnitSquare(ScadObject):
    """
    Class for an imperial unit square.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self) -> None:
        """
        Object constructor.
        """
        ScadObject.__init__(self, args={})

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        context.unit = Unit.INCH

        return Square(size=1.0)

# ----------------------------------------------------------------------------------------------------------------------
