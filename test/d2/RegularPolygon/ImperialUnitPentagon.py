from super_scad.Context import Context
from super_scad.d2.RegularPolygon import RegularPolygon
from super_scad.ScadObject import ScadObject
from super_scad.Unit import Unit


class ImperialUnitPentagon(ScadObject):
    """
    Class for an imperial unit pentagon.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self) -> None:
        """
        Object constructor.
        """
        ScadObject.__init__(self, args={})

        self.imperial_pentagon: RegularPolygon | None = None
        """
        The imperial pentagon.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        context.unit = Unit.INCH

        self.imperial_pentagon = RegularPolygon(size=1.0, sides=5)
        self.imperial_pentagon.nodes  # Force calculation of the nodes in inches.

        return self.imperial_pentagon

# ----------------------------------------------------------------------------------------------------------------------
