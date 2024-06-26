from typing import List

from Private.PrivateMultiChildScadCommand import PrivateMultiChildScadCommand
from ScadObject import ScadObject


class Minkowski(PrivateMultiChildScadCommand):
    """
    Displays the minkowski sum of child nodes. See
    https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Transformations#minkowski.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *, convexity: int, children: List[ScadObject]):
        """
        Object constructor.

        :param convexity:
        """
        PrivateMultiChildScadCommand.__init__(self, command='minkowski', args=locals(), children=children)

# ----------------------------------------------------------------------------------------------------------------------
