from super_scad.d2.RightTriangle import RightTriangle
from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.scad.Unit import Unit


class ImperialUnitRightTriangle(ScadWidget):
    """
    Widget for creating an imperial unit rightTriangle.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self) -> None:
        """
        Object constructor.
        """
        ScadWidget.__init__(self, args={})

        self.imperial_right_triangle: RightTriangle | None = None
        """
        The imperial unit rightTriangle.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        Context.set_unit_length_current(Unit.INCH)

        self.imperial_right_triangle = RightTriangle(width=2.0, depth=1.0)

        return self.imperial_right_triangle

# ----------------------------------------------------------------------------------------------------------------------
