from super_scad.d3.Cone import Cone
from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.scad.Unit import Unit


class ImperialCone(ScadWidget):
    """
    Widget for creating imperial cones.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 height: float | None = None,
                 top_radius: float | None = None,
                 top_diameter: float | None = None,
                 bottom_radius: float | None = None,
                 bottom_diameter: float | None = None,
                 fa: float | None = None,
                 fs: float | None = None,
                 fn: int | None = None) -> None:
        """
        Object constructor.
        """
        ScadWidget.__init__(self)

        self._height = height
        self._top_radius = top_radius
        self._top_diameter = top_diameter
        self._bottom_radius = bottom_radius
        self._bottom_diameter = bottom_diameter
        self._fa = fa
        self._fs = fs
        self._fn = fn

        self.imperial_cone: Cone | None = None
        """
        The imperial cone.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        Context.set_unit_length_current(Unit.INCH)

        self.imperial_cone = Cone(height=self._height,
                                  top_radius=self._top_radius,
                                  top_diameter=self._top_diameter,
                                  bottom_radius=self._bottom_radius,
                                  bottom_diameter=self._bottom_diameter,
                                  fa=self._fa,
                                  fs=self._fs,
                                  fn=self._fn)

        return self.imperial_cone

# ----------------------------------------------------------------------------------------------------------------------
