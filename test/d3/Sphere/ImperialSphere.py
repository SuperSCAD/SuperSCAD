from super_scad.Context import Context
from super_scad.d3.Sphere import Sphere
from super_scad.ScadObject import ScadObject
from super_scad.Unit import Unit


class ImperialSphere(ScadObject):
    """
    Class for imperial spheres.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 radius: float | None = None,
                 diameter: float | None = None,
                 fa: float | None = None,
                 fs: float | None = None,
                 fn: int | None = None) -> None:
        """
        Object constructor.
        """
        ScadObject.__init__(self, args=locals())

        self.imperial_sphere: Sphere | None = None
        """
        The imperial sphere.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        context.unit = Unit.INCH

        self.imperial_sphere = Sphere(radius=self._args.get('radius'),
                                      diameter=self._args.get('diameter'),
                                      fa=self._args.get('fa'),
                                      fs=self._args.get('fs'),
                                      fn=self._args.get('fn'))

        return self.imperial_sphere

# ----------------------------------------------------------------------------------------------------------------------
