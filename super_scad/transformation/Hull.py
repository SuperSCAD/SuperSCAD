from typing import List

from super_scad.private.PrivateMultiChildOpenScadCommand import PrivateMultiChildOpenScadCommand
from super_scad.scad.ScadObject import ScadObject


class Hull(PrivateMultiChildOpenScadCommand):
    """
    Displays the convex hull of child nodes. See
    https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Transformations#hull.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, children: List[ScadObject]):
        """
        Object constructor.
        """
        PrivateMultiChildOpenScadCommand.__init__(self, command='hull', args=locals(), children=children)

# ----------------------------------------------------------------------------------------------------------------------
