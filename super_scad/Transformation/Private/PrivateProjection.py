from ScadObject import ScadObject
from Private.PrivateSingleChildScadCommand import PrivateSingleChildScadCommand


class PrivateProjection(PrivateSingleChildScadCommand):

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *, cut: bool, child: ScadObject) -> None:
        PrivateSingleChildScadCommand.__init__(self, command='projection', args=locals(), child=child)

# ----------------------------------------------------------------------------------------------------------------------
