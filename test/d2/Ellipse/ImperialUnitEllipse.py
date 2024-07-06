from super_scad.d2.Ellipse import Ellipse
from super_scad.scad.Context import Context
from super_scad.scad.ScadObject import ScadObject
from super_scad.scad.Unit import Unit


class ImperialUnitEllipse(ScadObject):
    """
    Class for an imperial unit ellipse.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self) -> None:
        """
        Object constructor.
        """
        ScadObject.__init__(self, args={})

        self.imperial_ellipse: Ellipse | None = None
        """
        The imperial unit ellipse.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        Context.set_unit_length_current(Unit.INCH)

        self.imperial_ellipse = Ellipse(radius_x=2.0, radius_y=1.0)

        return self.imperial_ellipse

# ----------------------------------------------------------------------------------------------------------------------
