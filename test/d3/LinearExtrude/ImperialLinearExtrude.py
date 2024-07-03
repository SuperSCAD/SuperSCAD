from super_scad.Context import Context
from super_scad.d2.Square import Square
from super_scad.d3.LinearExtrude import LinearExtrude
from super_scad.ScadObject import ScadObject
from super_scad.Unit import Unit


class ImperialLinearExtrude(ScadObject):
    """
    Extrudes an imperial cube.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        """
        Object constructor.
        """
        ScadObject.__init__(self, args=locals())

        self.imperial_linear_extrude: LinearExtrude | None = None
        """
        The imperial sphere.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        context.unit = Unit.INCH

        self.imperial_linear_extrude = LinearExtrude(height=1.0,
                                                     fs=0.01,
                                                     child=Square(size=1.0)
                                                     )

        return self.imperial_linear_extrude

# ----------------------------------------------------------------------------------------------------------------------
