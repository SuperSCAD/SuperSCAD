from super_scad.d2.Square import Square
from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.scad.Unit import Unit


class ImperialUnitSquare(ScadWidget):
    """
    Class for an imperial unit square.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self) -> None:
        """
        Object constructor.
        """
        ScadWidget.__init__(self, args={})

        self.imperial_square: Square | None = None
        """
        The imperial unit square.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        Context.set_unit_length_current(Unit.INCH)

        self.imperial_square = Square(size=1.0)

        return self.imperial_square

# ----------------------------------------------------------------------------------------------------------------------
