from Context import Context
from ScadObject import ScadObject
from ScadSingleChildParent import ScadSingleChildParent
from Transformation.Private.PrivateTranslate import PrivateTranslate
from Type.Point3 import Point3


class Translate3D(ScadSingleChildParent):
    """
    Translates (moves) its child elements along the specified vector. See
    https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Transformations#translate.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *, x: float = 0.0, y: float = 0.0, z: float = 0.0, child: ScadObject):
        """
        Object constructor.

        :param x: The distance the child is translated to along the X-coordinate.
        :param y: The distance the child is translated to along the Y-coordinate.
        :param z: The distance the child is translated to along the Z-coordinate.
        """
        ScadSingleChildParent.__init__(self, args=locals(), child=child)

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def x(self) -> float:
        """
        Returns distance the child is translated to along the X-coordinate.
        """
        return self.uc(self._args['x'])

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def y(self) -> float:
        """
        Returns distance the child is translated to along the Y-coordinate.
        """
        return self.uc(self._args['y'])

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def z(self) -> float:
        """
        Returns distance the child is translated to along the Y-coordinate.
        """
        return self.uc(self._args['z'])

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        return PrivateTranslate(vector=Point3(x=self.x, y=self.y, z=self.z), child=self.child)

# ----------------------------------------------------------------------------------------------------------------------
