from super_scad.d2.Circle4n import Circle4n
from super_scad.d2.Semicircle4n import Semicircle4n
from super_scad.d3.RotateExtrude import RotateExtrude
from super_scad.scad.ArgumentAdmission import ArgumentAdmission
from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.transformation.Rotate2D import Rotate2D


class Sphere4n(ScadWidget):
    """
    Widget for creating spheres. See https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Primitive_Solids#sphere.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 radius: float | None = None,
                 diameter: float | None = None):
        """
        Object constructor.

        :param radius: The radius of the sphere.
        :param diameter: The diameter of the sphere.
        """
        ScadWidget.__init__(self, args=locals())

    # ------------------------------------------------------------------------------------------------------------------
    def _validate_arguments(self) -> None:
        """
        Validates the arguments supplied to the constructor of this SuperSCAD widget.
        """
        admission = ArgumentAdmission(self._args)
        admission.validate_exclusive({'radius'}, {'diameter'})
        admission.validate_required({'radius', 'diameter'})

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
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        return RotateExtrude(angle=360.0,
                             fn=Circle4n.r2sides4n(self.radius, context),
                             child=Rotate2D(angle=-90.0, child=Semicircle4n(diameter=self.diameter)))

# ----------------------------------------------------------------------------------------------------------------------
