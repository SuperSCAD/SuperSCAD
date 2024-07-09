from super_scad.d2.Circle import Circle
from super_scad.d3.RotateExtrude import RotateExtrude
from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.scad.Unit import Unit
from super_scad.transformation.Translate2D import Translate2D


class ImperialUnitDonut(ScadWidget):
    """
    Extrudes an imperial donut.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        """
        Object constructor.
        """
        ScadWidget.__init__(self, args=locals())

        self.imperial_unit_donut: RotateExtrude | None = None
        """
        The imperial sphere.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        Context.set_unit_length_current(Unit.INCH)

        self.imperial_unit_donut = RotateExtrude(convexity=10,
                                                 fs=0.01,
                                                 child=Translate2D(x=1.0, child=Circle(diameter=1.0, fn=100)))

        return self.imperial_unit_donut

# ----------------------------------------------------------------------------------------------------------------------
