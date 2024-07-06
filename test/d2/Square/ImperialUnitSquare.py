from super_scad.d2.Square import Square
from super_scad.scad.Context import Context
from super_scad.scad.ScadObject import ScadObject
from super_scad.scad.Unit import Unit


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

        self.imperial_square: Square | None = None
        """
        The imperial unit square.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        context.unit = Unit.INCH

        self.imperial_square = Square(size=1.0)

        return self.imperial_square

# ----------------------------------------------------------------------------------------------------------------------
