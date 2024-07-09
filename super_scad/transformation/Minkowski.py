from typing import List

from super_scad.private.PrivateMultiChildOpenScadCommand import PrivateMultiChildOpenScadCommand
from super_scad.scad.ScadWidget import ScadWidget


class Minkowski(PrivateMultiChildOpenScadCommand):
    """
    Displays the minkowski sum of child nodes. See
    https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Transformations#minkowski.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *, convexity: int | None = None, children: List[ScadWidget]):
        """
        Object constructor.

        :param convexity: Number of "inward" curves, i.e. expected number of path crossings of an arbitrary line through
                          the child objects.
        :param children: The child objects.
        """
        PrivateMultiChildOpenScadCommand.__init__(self, command='minkowski', args=locals(), children=children)

# ----------------------------------------------------------------------------------------------------------------------
