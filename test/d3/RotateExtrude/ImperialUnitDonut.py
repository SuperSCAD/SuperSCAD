from super_scad.Context import Context
from super_scad.d2.Circle import Circle
from super_scad.d3.RotateExtrude import RotateExtrude
from super_scad.ScadObject import ScadObject
from super_scad.transformation.Translate2D import Translate2D
from super_scad.Unit import Unit


class ImperialUnitDonut(ScadObject):
    """
    Extrudes an imperial donut.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        """
        Object constructor.
        """
        ScadObject.__init__(self, args=locals())

        self.imperial_unit_donut: RotateExtrude | None = None
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

        self.imperial_unit_donut = RotateExtrude(convexity=10,
                                                 fs=0.01,
                                                 child=Translate2D(x=1.0, child=Circle(diameter=1.0, fn=100)))

        return self.imperial_unit_donut

# ----------------------------------------------------------------------------------------------------------------------
