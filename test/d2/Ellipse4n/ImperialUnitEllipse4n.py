from super_scad.d2.Ellipse4n import Ellipse4n
from super_scad.scad.Context import Context
from super_scad.scad.ScadObject import ScadObject
from super_scad.scad.Unit import Unit


class ImperialUnitEllipse4n(ScadObject):
    """
    Class for an imperial unit ellipse4n.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self) -> None:
        """
        Object constructor.
        """
        ScadObject.__init__(self, args={})

        self.imperial_ellipse: Ellipse4n | None = None
        """
        The imperial unit ellipse4n.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        context.unit = Unit.INCH

        self.imperial_ellipse = Ellipse4n(radius_x=2.0, radius_y=1.0)

        return self.imperial_ellipse

# ----------------------------------------------------------------------------------------------------------------------
