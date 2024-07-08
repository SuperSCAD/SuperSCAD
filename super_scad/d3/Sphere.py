from typing import Dict, Set

from super_scad.private.PrivateOpenScadCommand import PrivateOpenScadCommand
from super_scad.scad.ArgumentAdmission import ArgumentAdmission


class Sphere(PrivateOpenScadCommand):
    """
    Class for spheres. See https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Primitive_Solids#sphere.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 radius: float | None = None,
                 diameter: float | None = None,
                 fa: float | None = None,
                 fs: float | None = None,
                 fn: int | None = None):
        """
        Object constructor.

        :param radius: The radius of the sphere.
        :param diameter: The diameter of the sphere.
        :param fa: The minimum angle (in degrees) of each fragment.
        :param fs: The minimum circumferential length of each fragment.
        :param fn: The fixed number of fragments in 360 degrees. Values of 3 or more override fa and fs.
        """
        PrivateOpenScadCommand.__init__(self, command='sphere', args=locals())

    # ------------------------------------------------------------------------------------------------------------------
    def _validate_arguments(self) -> None:
        """
        Validates the arguments supplied to the constructor of this SuperSCAD object.
        """
        admission = ArgumentAdmission(self._args)
        admission.validate_exclusive({'radius'}, {'diameter'})
        admission.validate_required({'radius', 'diameter'})

    # ------------------------------------------------------------------------------------------------------------------
    def argument_map(self) -> Dict[str, str]:
        """
        Returns the map from SuperSCAD arguments to OpenSCAD arguments.
        """
        return {'radius': 'r', 'diameter': 'd', 'fa': '$fa', 'fs': '$fs', 'fn': '$fn'}

    # ------------------------------------------------------------------------------------------------------------------
    def argument_lengths(self) -> Set[str]:
        """
        Returns the set with arguments that are lengths.
        """
        return {'r', 'd', '$fs'}

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def radius(self) -> float:
        """
        Returns the radius of the sphere.
        """
        return self.uc(self._args.get('radius', 0.5 * self._args.get('diameter', 0.0)))

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def diameter(self) -> float:
        """
        Returns the diameter of the sphere.
        """
        return self.uc(self._args.get('diameter', 2.0 * self._args.get('radius', 0.0)))

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
        Returns the fixed number of fragments in 360 degrees. Values of 3 or more override fa and fs.
        """
        return self._args.get('fn')

# ----------------------------------------------------------------------------------------------------------------------
