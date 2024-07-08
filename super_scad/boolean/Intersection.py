from typing import List

from super_scad.private.PrivateMultiChildOpenScadCommand import PrivateMultiChildOpenScadCommand
from super_scad.scad.ScadObject import ScadObject


class Intersection(PrivateMultiChildOpenScadCommand):
    """
    Creates the intersection of all child nodes. This keeps the overlapping portion (logical and). See
    https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/CSG_Modelling#intersection.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *, children: List[ScadObject]):
        """
        Object constructor.
        """
        PrivateMultiChildOpenScadCommand.__init__(self, command='intersection', args=locals(), children=children)

# ----------------------------------------------------------------------------------------------------------------------
