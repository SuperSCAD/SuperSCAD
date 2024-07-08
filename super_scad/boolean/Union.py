from typing import List

from super_scad.private.PrivateMultiChildOpenScadCommand import PrivateMultiChildOpenScadCommand
from super_scad.scad.ScadObject import ScadObject


class Union(PrivateMultiChildOpenScadCommand):
    """
    Creates a union of all its child nodes. This is the sum of all children (logical or). See
    https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/CSG_Modelling#union.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *, children: List[ScadObject]):
        """
        Object constructor.
        """
        PrivateMultiChildOpenScadCommand.__init__(self, command='union', args=locals(), children=children)

# ----------------------------------------------------------------------------------------------------------------------
