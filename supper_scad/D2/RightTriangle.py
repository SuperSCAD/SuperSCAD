from Context import Context
from D2.Polygon import Polygon
from ScadObject import ScadObject
from Type.Point2 import Point2


class RightTriangle(ScadObject):
    """
    A class to represent a right triangle (a.k.a. right-angled triangle, orthogonal triangle, or rectangular triangle).
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *, width: float, depth: float):
        """
        Object constructor.

        :param width: The width of a triangle.
        :param depth: The depth of a triangle.
        """
        ScadObject.__init__(self, args=locals())

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def width(self) -> float:
        """
        Returns the width of the right triangle.
        """
        return self.uc(self._args['width'])

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def depth(self) -> float:
        """
        Returns the depth of the right triangle.
        """
        return self.uc(self._args['depth'])

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        return Polygon(points=[Point2(0.0, 0.0), Point2(self.width, 0.0), Point2(0.0, self.depth)])

# ----------------------------------------------------------------------------------------------------------------------
