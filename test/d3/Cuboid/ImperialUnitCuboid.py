from super_scad.d3.Cuboid import Cuboid
from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.scad.Unit import Unit


class ImperialUnitCuboid(ScadWidget):
    """
    Class for an imperial unit cuboid.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self) -> None:
        """
        Object constructor.
        """
        ScadWidget.__init__(self, args={})

        self.imperial_cuboid: Cuboid | None = None
        """
        The imperial unit cuboid.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        Context.set_unit_length_current(Unit.INCH)

        self.imperial_cuboid = Cuboid(width=3.0, depth=2.0, height=1.0)

        return self.imperial_cuboid

# ----------------------------------------------------------------------------------------------------------------------
