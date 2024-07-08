from typing import List

from super_scad.private.PrivateMultiChildOpenScadCommand import PrivateMultiChildOpenScadCommand
from super_scad.scad.ScadObject import ScadObject


class Difference(PrivateMultiChildOpenScadCommand):
    """
    Subtracts the second (and all further) child nodes from the first one (logical and not).
    See https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/CSG_Modelling#difference.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *, children: List[ScadObject]):
        """
        Object constructor.
        """
        PrivateMultiChildOpenScadCommand.__init__(self, command='difference', args=locals(), children=children)

# ----------------------------------------------------------------------------------------------------------------------
