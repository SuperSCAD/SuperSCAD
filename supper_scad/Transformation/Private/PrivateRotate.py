from typing import Dict

from ScadObject import ScadObject
from Private.PrivateSingleChildScadCommand import PrivateSingleChildScadCommand
from Type.Point3 import Point3


class PrivateRotate(PrivateSingleChildScadCommand):
    """
    Rotates its child 'a' degrees about the axis of the coordinate system or around an arbitrary axis. See
    https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Transformations#rotate.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *, angle: float | Point3, vector: Point3 | None = None, child: ScadObject) -> None:
        """
        Object constructor.

        :param angle:
        :param vector:
        """
        PrivateSingleChildScadCommand.__init__(self, command='rotate', args=locals(), child=child)

    # ------------------------------------------------------------------------------------------------------------------
    def argument_map(self) -> Dict[str, str]:
        """
        Returns the map from SuperSCAD arguments to OpenSCAD arguments.
        """
        return {'angle': 'a', 'vector': 'v'}

# ----------------------------------------------------------------------------------------------------------------------
