from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.scad.Unit import Unit
from super_scad.transformation.Translate3D import Translate3D
from super_scad.type.Vector3 import Vector3


class ImperialTranslate3D(ScadWidget):
    """
    Widget for creating imperial translation.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 vector: Vector3 | None = None,
                 x: float | None = None,
                 y: float | None = None,
                 z: float | None = None,
                 child: ScadWidget) -> None:
        """
        Object constructor.
        """
        ScadWidget.__init__(self, args=locals())

        self.imperial_translate: Translate3D | None = None
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

        self.imperial_translate = Translate3D(vector=self._args.get('vector'),
                                              x=self._args.get('x'),
                                              y=self._args.get('y'),
                                              z=self._args.get('z'),
                                              child=self.child)

        return self.imperial_translate

# ----------------------------------------------------------------------------------------------------------------------
