from super_scad.d2.Square import Square
from super_scad.d3.LinearExtrude import LinearExtrude
from super_scad.scad.Context import Context
from super_scad.scad.ScadObject import ScadObject
from super_scad.scad.Unit import Unit


class ImperialUnitCube(ScadObject):
    """
    Extrudes an imperial unit cube.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        """
        Object constructor.
        """
        ScadObject.__init__(self, args=locals())

        self.imperial_unit_cube: LinearExtrude | None = None
        """
        The imperial unit cube.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        Context.set_unit_length_current(Unit.INCH)

        self.imperial_unit_cube = LinearExtrude(height=1.0, fs=0.01, child=Square(size=1.0))

        return self.imperial_unit_cube

# ----------------------------------------------------------------------------------------------------------------------
