from typing import Set

from Private.PrivateScadCommand import PrivateScadCommand
from Type.Size3 import Size3


class PrivateCube(PrivateScadCommand):
    """
    Class for cubes. See https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Primitive_Solids#cube.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *, size: float | Size3, center: bool = False):
        """
        Object constructor.

        :param size: The size of the cube.
        :param center: Whether the cube is centered at the origin.
        """
        PrivateScadCommand.__init__(self, command='cube', args=locals())

    # ------------------------------------------------------------------------------------------------------------------
    def argument_lengths(self) -> Set[str]:
        """
        Returns the set with arguments that are lengths.
        """
        return {'size'}

# ----------------------------------------------------------------------------------------------------------------------
