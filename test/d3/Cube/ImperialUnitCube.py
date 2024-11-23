from super_scad.d3.Cube import Cube
from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.scad.Unit import Unit


class ImperialUnitCube(ScadWidget):
    """
    Widget for creating an imperial unit cube.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self) -> None:
        """
        Object constructor.
        """
        ScadWidget.__init__(self)

        self.imperial_cube: Cube | None = None
        """
        The imperial unit cube.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        Context.set_unit_length_current(Unit.INCH)

        self.imperial_cube = Cube(size=1.0)

        return self.imperial_cube

# ----------------------------------------------------------------------------------------------------------------------
