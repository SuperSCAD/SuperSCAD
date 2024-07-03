from super_scad.Context import Context
from super_scad.ScadObject import ScadObject
from super_scad.ScadSingleChildParent import ScadSingleChildParent
from super_scad.transformation.private.PrivateTranslate import PrivateTranslate
from super_scad.type.Point3 import Point3


class Translate3D(ScadSingleChildParent):
    """
    Translates (moves) its child object along the specified vector. See
    https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Transformations#translate.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 vector: Point3 | None = None,
                 x: float | None = None,
                 y: float | None = None,
                 z: float | None = None,
                 child: ScadObject):
        """
        Object constructor.

        :param vector: The vector over which the child object is translated.
        :param x: The distance the child object is translated along the x-axis.
        :param y: The distance the child object is translated along the y-axis.
        :param z: The distance the child object is translated along the z-axis.
        :param child: The child object to be translated.
        """
        ScadSingleChildParent.__init__(self, args=locals(), child=child)

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def vector(self) -> Point3:
        """
        Returns the scaling factor along all three the axes.
        """
        return Point3(self.x, self.y, self.z)

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def x(self) -> float:
        """
        Returns distance the child object is translated to along the x-axis.
        """
        if 'vector' in self._args:
            return self.uc(self._args['vector'].x)

        return self.uc(self._args.get('x', 0.0))

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def y(self) -> float:
        """
        Returns distance the child object is translated to along the y-axis.
        """
        if 'vector' in self._args:
            return self.uc(self._args['vector'].y)

        return self.uc(self._args.get('y', 0.0))

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def z(self) -> float:
        """
        Returns distance the child object is translated to along the z-axis.
        """
        if 'vector' in self._args:
            return self.uc(self._args['vector'].z)

        return self.uc(self._args.get('z', 0.0))

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        return PrivateTranslate(vector=Point3(x=self.x, y=self.y, z=self.z), child=self.child)

# ----------------------------------------------------------------------------------------------------------------------
