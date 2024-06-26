from Context import Context
from D3.Private.PrivateCube import PrivateCube
from ScadObject import ScadObject
from Type.Size3 import Size3


class Cuboid(ScadObject):
    """
    Class for cubes. See https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Primitive_Solids#cube.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 size: Size3 | None,
                 width: float | None,
                 depth: float | None,
                 height: float | None,
                 center: bool = False):
        """
        Object constructor.

        :param size: The size of the cuboid.
        :param width: The width (the size along the x-axis) of the cuboid.
        :param depth: The depth (the size along the y-axis) of the cuboid.
        :param height: The height (the size along the y-axis) of the cuboid.
        :param center: Whether the cuboid is centered at the origin.
        """
        ScadObject.__init__(self, args=locals())

    # ------------------------------------------------------------------------------------------------------------------
    def _validate_arguments(self) -> None:
        pass

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def center(self) -> bool:
        """
        Returns whether the cuboid is centered at the origin.
        """
        return self._args['center']

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def size(self) -> Size3:
        """
        Returns the size of the cuboid.
        """
        return Size3(width=self.width, depth=self.depth, height=self.height)

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def width(self) -> float:
        """
        Returns the width of the cuboid.
        """
        if isinstance(self._args.get('size'), Size3):
            return self.uc(self._args['size'].width)

        return self.uc(self._args['width'])

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def depth(self) -> float:
        """
        Returns the depth of the cuboid.
        """
        if isinstance(self._args.get('size'), Size3):
            return self.uc(self._args['size'].depth)

        return self.uc(self._args['depth'])

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def height(self) -> float:
        """
        Returns the height of the cuboid.
        """
        if isinstance(self._args.get('size'), Size3):
            return self.uc(self._args['size'].height)

        return self.uc(self._args['height'])

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        return PrivateCube(size=self.size, center=self.center)

# ----------------------------------------------------------------------------------------------------------------------
