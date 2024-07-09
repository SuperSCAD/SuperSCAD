from super_scad.d2.Semicircle4n import Semicircle4n
from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.scad.Unit import Unit


class ImperialSemicircle4n(ScadWidget):
    """
    Widget for creating imperial semicircles.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 radius: float | None = None,
                 diameter: float | None = None) -> None:
        """
        Object constructor.
        """
        ScadWidget.__init__(self, args=locals())

        self.imperial_semicircle4n: Semicircle4n | None = None
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

        self.imperial_semicircle4n = Semicircle4n(radius=self._args.get('radius'),
                                                  diameter=self._args.get('diameter'))

        return self.imperial_semicircle4n

# ----------------------------------------------------------------------------------------------------------------------
