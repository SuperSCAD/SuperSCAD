from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.scad.Unit import Unit
from super_scad.transformation.Translate2D import Translate2D
from super_scad.type.Vector2 import Vector2


class ImperialTranslate2D(ScadWidget):
    """
    Class for imperial translation.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 vector: Vector2 | None = None,
                 x: float | None = None,
                 y: float | None = None,
                 child: ScadWidget) -> None:
        """
        Object constructor.
        """
        ScadWidget.__init__(self, )

        self._vector = vector
        self._x = x
        self._y = y

        self.imperial_translate: Translate2D | None = None
        """
        The imperial translation.
        """

        self.child: ScadWidget = child
        """
        the child widget to be translated.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        Context.set_unit_length_current(Unit.INCH)

        self.imperial_translate = Translate2D(vector=self._vector,
                                              x=self._x,
                                              y=self._y,
                                              child=self.child)

        return self.imperial_translate

# ----------------------------------------------------------------------------------------------------------------------
