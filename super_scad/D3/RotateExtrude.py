from typing import Dict, Set

from ScadObject import ScadObject
from Private.PrivateSingleChildScadCommand import PrivateSingleChildScadCommand


class RotateExtrude(PrivateSingleChildScadCommand):
    """
    Rotational extrusion spins a 2D shape around the Z-axis to form a solid which has rotational symmetry. See
    https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Using_the_2D_Subsystem#rotate_extrude.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 angle: float,
                 convexity: int | None = None,
                 child: ScadObject,
                 fa: float | None = None,
                 fs: float | None = None,
                 fn: int | None = None):
        """
        Object constructor.

        :param angle: See `OpenSCAD rotate_extrude documentation`_.
        :param convexity: See `OpenSCAD rotate_extrude documentation`_.
        :param fa: See `OpenSCAD rotate_extrude documentation`_.
        :param fs: See `OpenSCAD rotate_extrude documentation`_.
        :param fn: See `OpenSCAD rotate_extrude documentation`_.

        .. _OpenSCAD rotate_extrude documentation: https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Using_the_2D_Subsystem#rotate_extrude
        """
        PrivateSingleChildScadCommand.__init__(self, command='rotate_extrude', args=locals(), child=child)

    # ------------------------------------------------------------------------------------------------------------------
    def _validate_arguments(self) -> None:
        pass

    # ------------------------------------------------------------------------------------------------------------------
    def argument_map(self) -> Dict[str, str]:
        """
        Returns the map from SuperSCAD arguments to OpenSCAD arguments.
        """
        return {'fa': '$fa', 'fs': '$fs', 'fn': '$fn'}

    # ------------------------------------------------------------------------------------------------------------------
    def argument_lengths(self) -> Set[str]:
        """
        Returns the set with arguments that are lengths.
        """
        return {'fs'}

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def angle(self) -> float:
        """
        Returns the number of degrees to sweep, starting at the positive X axis. The direction of the sweep follows the
        Right Hand Rule, hence a negative angle sweeps clockwise.
        """
        return self._args['angle']

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def convexity(self) -> int:
        """
        Returns the convexity.
        """
        return self._args.get('convexity', 2)

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def fa(self) -> float | None:
        """
        Returns the minimum angle (in degrees) of each fragment.
        """
        return self._args.get('fa')

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def fs(self) -> float | None:
        """
        Returns the minimum circumferential length of each fragment.
        """
        return self.uc(self._args.get('fs'))

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def fn(self) -> int | None:
        """
        Returns the fixed number of fragments in 360 degrees. Values of 3 or more override $fa and $fs.
        """
        return self._args.get('fn')

# ----------------------------------------------------------------------------------------------------------------------
