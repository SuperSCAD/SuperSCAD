from typing import Tuple

from Context import Context
from ScadObject import ScadObject
from ScadSingleChildParent import ScadSingleChildParent
from Transformation.Private.PrivateResize import PrivateResize
from Type.Size2 import Size2


class Resize2D(ScadSingleChildParent):
    """
    Modifies the size of the child object to match the given x and y. See
    https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Transformations#resize.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 new_size: Size2 | None = None,
                 new_size_x: float | None = None,
                 new_size_y: float | None = None,
                 auto: bool | Tuple[bool, bool] = False,
                 convexity: int | None = None,
                 child: ScadObject):
        """
        Object constructor.

        :param new_size: The new_size along all two axes.
        :param new_size_x: The along the x-axis (a.k.a. width).
        :param new_size_y: The new size along the y-axis (a.k.a. depth).
        :param auto: Whether to auto-scale any 0-dimensions to match.
        :param convexity:
        :param child: The child object to be resized.
        """
        ScadSingleChildParent.__init__(self, args=locals(), child=child)

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def new_size(self) -> Size2:
        """
        Returns the new_size along all two axes.
        """
        return Size2(self.new_size_x, self.new_size_y)

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def new_size_x(self) -> float:
        """
        Returns the new size along the x-axis (a.k.a. width).
        """
        if 'new_size' in self._args:
            return self.uc(self._args['new_size'].width)

        return self.uc(self._args['new_width'])

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def new_size_y(self) -> float:
        """
        Returns the new size along the y-axis (a.k.a. depth).
        """
        if 'new_size' in self._args:
            return self.uc(self._args['new_size'].depth)

        return self.uc(self._args['new_depth'])

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        return PrivateResize(new_size=self.new_size, child=self.child)

# ----------------------------------------------------------------------------------------------------------------------
