from super_scad.d2.Circle import Circle
from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.scad.Unit import Unit


class ImperialCircle(ScadWidget):
    """
    Widget for creating imperial circles.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 radius: float | None = None,
                 diameter: float | None = None,
                 fa: float | None = None,
                 fs: float | None = None,
                 fn: int | None = None) -> None:
        """
        Object constructor.
        """
        ScadWidget.__init__(self)

        self._radius = radius
        self._diameter = diameter
        self._fa = fa
        self._fs = fs
        self._fn = fn

        self.imperial_circle: Circle | None = None
        """
        The imperial circle.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        Context.set_unit_length_current(Unit.INCH)

        self.imperial_circle = Circle(radius=self._radius,
                                      diameter=self._diameter,
                                      fa=self._fa,
                                      fs=self._fs,
                                      fn=self._fn)

        return self.imperial_circle

# ----------------------------------------------------------------------------------------------------------------------
