from super_scad.Context import Context
from super_scad.d2.Rectangle import Rectangle
from super_scad.ScadObject import ScadObject
from super_scad.Unit import Unit


class ImperialUnitRectangle(ScadObject):
    """
    Class for an imperial unit rectangle.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self) -> None:
        """
        Object constructor.
        """
        ScadObject.__init__(self, args={})

        self.imperial_rectangle: Rectangle | None = None
        """
        The imperial unit rectangle.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        context.unit = Unit.INCH

        self.imperial_rectangle = Rectangle(width=2.0, depth=1.0)

        return self.imperial_rectangle

# ----------------------------------------------------------------------------------------------------------------------
