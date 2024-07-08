from super_scad.private.PrivateSingleChildOpenScadCommand import PrivateSingleChildOpenScadCommand
from super_scad.scad.ScadObject import ScadObject


class PrivateProjection(PrivateSingleChildOpenScadCommand):

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *, cut: bool, child: ScadObject) -> None:
        """
        Object constructor.

        :param cut: Whether to cut the 3D model at height 0.0.
        :param child: The child object.
        """
        PrivateSingleChildOpenScadCommand.__init__(self, command='projection', args=locals(), child=child)

# ----------------------------------------------------------------------------------------------------------------------
