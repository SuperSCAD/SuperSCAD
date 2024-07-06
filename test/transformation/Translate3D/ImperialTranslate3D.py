from super_scad.scad.Context import Context
from super_scad.scad.ScadObject import ScadObject
from super_scad.scad.Unit import Unit
from super_scad.transformation.Translate3D import Translate3D
from super_scad.type.Point3 import Point3


class ImperialTranslate3D(ScadObject):
    """
    Class for imperial translation.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 vector: Point3 | None = None,
                 x: float | None = None,
                 y: float | None = None,
                 z: float | None = None,
                 child: ScadObject) -> None:
        """
        Object constructor.
        """
        ScadObject.__init__(self, args=locals())

        self.imperial_translate: Translate3D | None = None
        """
        The imperial translation.
        """

        self.child: ScadObject = child
        """
        The child object to be translated.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        context.unit = Unit.INCH

        self.imperial_translate = Translate3D(vector=self._args.get('vector'),
                                              x=self._args.get('x'),
                                              y=self._args.get('y'),
                                              z=self._args.get('z'),
                                              child=self.child)

        return self.imperial_translate

# ----------------------------------------------------------------------------------------------------------------------
