from super_scad.Context import Context
from super_scad.d2.RightTriangle import RightTriangle
from super_scad.ScadObject import ScadObject
from super_scad.Unit import Unit


class ImperialUnitRightTriangle(ScadObject):
    """
    Class for an imperial unit rightTriangle.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self) -> None:
        """
        Object constructor.
        """
        ScadObject.__init__(self, args={})

        self.imperial_right_triangle: RightTriangle | None = None
        """
        The imperial unit rightTriangle.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        context.unit = Unit.INCH

        self.imperial_right_triangle = RightTriangle(width=2.0, depth=1.0)

        return self.imperial_right_triangle

# ----------------------------------------------------------------------------------------------------------------------
