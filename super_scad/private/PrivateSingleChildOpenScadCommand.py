from typing import Any, Dict

from super_scad.private.PrivateOpenScadCommand import PrivateOpenScadCommand
from super_scad.scad.ScadObject import ScadObject
from super_scad.scad.ScadSingleChildParent import ScadSingleChildParent


class PrivateSingleChildOpenScadCommand(PrivateOpenScadCommand, ScadSingleChildParent):
    """
    Parent class for OpenSCAD commands with a single child.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, command: str, args: Dict[str, Any], child: ScadObject):
        """
        Object constructor.

        :param command: The OpenSCAD command.
        :param args: The arguments of the command.
        :param child: The child SuperSCAD object of this single-child parent.
        """
        PrivateOpenScadCommand.__init__(self, command=command, args=args)
        ScadSingleChildParent.__init__(self, args=args, child=child)

# ----------------------------------------------------------------------------------------------------------------------
