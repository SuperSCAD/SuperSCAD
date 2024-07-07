from super_scad.d2.Circle4n import Circle4n
from super_scad.scad.ArgumentAdmission import ArgumentAdmission
from super_scad.scad.Context import Context
from super_scad.scad.ScadObject import ScadObject
from super_scad.transformation.Resize2D import Resize2D
from super_scad.type.Size2 import Size2


class Ellipse4n(ScadObject):
    """
    Class for ellipsis.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 radius_x: float | None = None,
                 radius_y: float | None = None,
                 diameter_x: float | None = None,
                 diameter_y: float | None = None):
        """
        Object constructor.
        """
        ScadObject.__init__(self, args=locals())

    # ------------------------------------------------------------------------------------------------------------------
    def _validate_arguments(self) -> None:
        """
        Validates the arguments supplied to the constructor of this SuperSCAD object.
        """
        admission = ArgumentAdmission(self._args)
        admission.validate_exclusive({'radius_x'}, {'diameter_x'})
        admission.validate_exclusive({'radius_y'}, {'diameter_y'})
        admission.validate_required({'radius_x', 'diameter_x'}, {'radius_y', 'diameter_y'})

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def radius_x(self) -> float:
        """
        Returns the radius of the ellipsis in x-direction.
        """
        return self.uc(self._args.get('radius_x', 0.5 * self._args.get('diameter_x', 0.0)))

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def radius_y(self) -> float:
        """
        Returns the radius of the ellipsis in y-direction.
        """
        return self.uc(self._args.get('radius_y', 0.5 * self._args.get('diameter_y', 0.0)))

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def diameter_x(self) -> float:
        """
        Returns the length of the ellipsis in x-direction.
        """
        return self.uc(self._args.get('diameter_x', 2.0 * self._args.get('radius_x', 0.0)))

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def diameter_y(self) -> float:
        """
        Returns the length of the ellipsis in y-direction.
        """
        return self.uc(self._args.get('diameter_y', 2.0 * self._args.get('radius_y', 0.0)))

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        diameter: float = max(self.diameter_x, self.diameter_y)

        return Resize2D(new_size=Size2(self.diameter_x, self.diameter_y), child=Circle4n(diameter=diameter))

# ----------------------------------------------------------------------------------------------------------------------
