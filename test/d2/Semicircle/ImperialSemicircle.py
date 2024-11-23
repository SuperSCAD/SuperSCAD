from super_scad.d2.Semicircle import Semicircle
from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.scad.Unit import Unit


class ImperialSemicircle(ScadWidget):
    """
    Class for imperial semicircles.
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

        self.imperial_semicircle: Semicircle | None = None
        """
        The imperial semicircle.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        Context.set_unit_length_current(Unit.INCH)

        self.imperial_semicircle = Semicircle(radius=self._radius,
                                              diameter=self._diameter,
                                              fa=self._fa,
                                              fs=self._fs,
                                              fn=self._fn)

        return self.imperial_semicircle

# ----------------------------------------------------------------------------------------------------------------------
