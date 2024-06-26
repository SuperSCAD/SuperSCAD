from typing import Dict

from ScadObject import ScadObject
from Private.PrivateSingleChildScadCommand import PrivateSingleChildScadCommand
from Type.Point3 import Point3


class PrivateScale(PrivateSingleChildScadCommand):
    """
    Scales its child elements using the specified vector. See
    https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Transformations#scale.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *, factor: Point3, child: ScadObject) -> None:
        """
        Object constructor.

        :param factor: The scaling factor to apply.
        """
        PrivateSingleChildScadCommand.__init__(self, command='scale', args=locals(), child=child)

    # ------------------------------------------------------------------------------------------------------------------
    def argument_map(self) -> Dict[str, str]:
        """
        Returns the map from SuperSCAD arguments to OpenSCAD arguments.
        """
        return {'factor': 'v'}

# ----------------------------------------------------------------------------------------------------------------------
