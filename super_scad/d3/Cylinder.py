from super_scad.d3.private.PrivateCylinder import PrivateCylinder
from super_scad.scad.ArgumentAdmission import ArgumentAdmission
from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.util.Radius2Sides4n import Radius2Sides4n


class Cylinder(ScadWidget):
    """
    Widget for creating cylinders.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 height: float,
                 radius: float | None = None,
                 diameter: float | None = None,
                 center: bool = False,
                 fa: float | None = None,
                 fs: float | None = None,
                 fn: int | None = None,
                 fn4n: bool | None = None):
        """
        Object constructor.

        :param height: The height of the cylinder.
        :param radius: The radius of the cylinder.
        :param diameter: The diameter of the cylinder.
        :param center: Whether the cylinder is centered along the z-as.
        :param fa: The minimum angle (in degrees) of each fragment.
        :param fs: The minimum circumferential length of each fragment.
        :param fn: The fixed number of fragments in 360 degrees. Values of 3 or more override fa and fs.
        :param fn4n: Whether to create a cylinder with a multiple of 4 vertices.
        """
        ScadWidget.__init__(self, args=locals())

    # ------------------------------------------------------------------------------------------------------------------
    def _validate_arguments(self) -> None:
        """
        Validates the arguments supplied to the constructor of this SuperSCAD widget.
        """
        admission = ArgumentAdmission(self._args)
        admission.validate_exclusive({'radius'}, {'diameter'})
        admission.validate_exclusive({'fn4n'}, {'fa', 'fs', 'fn'})
        admission.validate_required({'height'},
                                    {'radius', 'diameter'},
                                    {'center'})

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def center(self) -> bool:
        """
        Returns whether the cylinder is centered along the z-as.
        """
        return self._args['center']

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def radius(self) -> float:
        """
        Returns the radius of the cylinder.
        """
        return self.uc(self._args.get('radius', 0.5 * self._args.get('diameter', 0.0)))

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def diameter(self) -> float:
        """
        Returns the diameter of the cylinder.
        """
        return self.uc(self._args.get('diameter', 2.0 * self._args.get('radius', 0.0)))

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def height(self) -> float:
        """
        Returns the height of the cylinder.
        """
        return self.uc(self._args['height'])

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

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def fn4n(self) -> bool | None:
        """
        Returns whether to create a circle with multiple of 4 vertices.
        """
        return self._args.get('fn4n')

    # ------------------------------------------------------------------------------------------------------------------
    def real_fn(self, context: Context) -> int | None:
        """
        Returns the real fixed number of fragments in 360 degrees.
        """
        if self.fn4n:
            return Radius2Sides4n.r2sides4n(self.radius, context)

        return self.fn

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """

        return PrivateCylinder(height=self.height,
                               diameter=self.diameter,
                               center=self.center,
                               fa=self.fa,
                               fs=self.fs,
                               fn=self.real_fn(context))

# ----------------------------------------------------------------------------------------------------------------------
