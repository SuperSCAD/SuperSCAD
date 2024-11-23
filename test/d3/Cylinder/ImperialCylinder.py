from super_scad.d3.Cylinder import Cylinder
from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.scad.Unit import Unit


class ImperialCylinder(ScadWidget):
    """
    Widget for creating imperial cylinders.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 height: float | None = None,
                 radius: float | None = None,
                 diameter: float | None = None,
                 fa: float | None = None,
                 fs: float | None = None,
                 fn: int | None = None) -> None:
        """
        Object constructor.
        """
        ScadWidget.__init__(self)

        self._height = height
        self._radius = radius
        self._diameter = diameter
        self._fa = fa
        self._fs = fs
        self._fn = fn

        self.imperial_cylinder: Cylinder | None = None
        """
        The imperial cylinder.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        Context.set_unit_length_current(Unit.INCH)

        self.imperial_cylinder = Cylinder(height=self._height,
                                          radius=self._radius,
                                          diameter=self._diameter,
                                          fa=self._fa,
                                          fs=self._fs,
                                          fn=self._fn)

        return self.imperial_cylinder

# ----------------------------------------------------------------------------------------------------------------------
