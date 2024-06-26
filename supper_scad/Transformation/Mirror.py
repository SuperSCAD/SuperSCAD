from ScadObject import ScadObject
from Private.PrivateSingleChildScadCommand import PrivateSingleChildScadCommand
from Type.Point3 import Point3


class Mirror(PrivateSingleChildScadCommand):
    """
    Transforms the child element to a mirror of the original, as if it were the mirror image seen through a plane
    intersecting the origin. See https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Transformations#mirror.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *, v: Point3, child: ScadObject):
        """
        Object constructor.

        :param v:
        """
        PrivateSingleChildScadCommand.__init__(self, command='mirror', args=locals(), child=child)

# ----------------------------------------------------------------------------------------------------------------------
