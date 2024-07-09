from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.scad.Unit import Unit
from super_scad.transformation.Translate2D import Translate2D
from super_scad.type.Point2 import Point2


class ImperialTranslate2D(ScadWidget):
    """
    Class for imperial translation.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 vector: Point2 | None = None,
                 x: float | None = None,
                 y: float | None = None,
                 child: ScadWidget) -> None:
        """
        Object constructor.
        """
        ScadWidget.__init__(self, args=locals())

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

        self.imperial_translate = Translate2D(vector=self._args.get('vector'),
                                              x=self._args.get('x'),
                                              y=self._args.get('y'),
                                              child=self.child)

        return self.imperial_translate

# ----------------------------------------------------------------------------------------------------------------------
