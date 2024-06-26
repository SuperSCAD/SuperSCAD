from typing import Dict, Set

from ScadObject import ScadObject
from Private.PrivateSingleChildScadCommand import PrivateSingleChildScadCommand
from Type.Point2 import Point2
from Type.Point3 import Point3


class PrivateTranslate(PrivateSingleChildScadCommand):
    """
    Translates (moves) its child objects along the specified vector. See
    https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Transformations#translate.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *, vector: Point2 | Point3, child: ScadObject):
        """
        Object constructor.

        :param vector:
        """
        PrivateSingleChildScadCommand.__init__(self, command='translate', args=locals(), child=child)

    # ------------------------------------------------------------------------------------------------------------------
    def argument_map(self) -> Dict[str, str]:
        """
        Returns the map from SuperSCAD arguments to OpenSCAD arguments.
        """
        return {'vector': 'v'}

    # ------------------------------------------------------------------------------------------------------------------
    def argument_lengths(self) -> Set[str]:
        """
        Returns the set with arguments that are lengths.
        """
        return {'v'}

# ----------------------------------------------------------------------------------------------------------------------
