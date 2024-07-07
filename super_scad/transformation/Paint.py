from typing import Dict

from super_scad.private.PrivateSingleChildScadCommand import PrivateSingleChildScadCommand
from super_scad.scad.ArgumentAdmission import ArgumentAdmission
from super_scad.scad.ScadObject import ScadObject
from super_scad.type.Color import Color


class Paint(PrivateSingleChildScadCommand):
    """
    Displays a child object using a specified color and opacity. See
    https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Transformations#color.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 color: Color,
                 child: ScadObject) -> None:
        """
        Object constructor.

        :param color: The color and opacity of the child object.
        :param child: The child object to be painted.
        """
        PrivateSingleChildScadCommand.__init__(self, command='color', args=locals(), child=child)

    # ------------------------------------------------------------------------------------------------------------------
    def _validate_arguments(self) -> None:
        """
        Validates the arguments supplied to the constructor of this SuperSCAD object.
        """
        admission = ArgumentAdmission(self._args)
        admission.validate_exclusive({'color'})

    # ------------------------------------------------------------------------------------------------------------------
    def argument_map(self) -> Dict[str, str]:
        """
        Returns the map from SuperSCAD arguments to OpenSCAD arguments.
        """
        return {'color': 'c'}

# ----------------------------------------------------------------------------------------------------------------------
