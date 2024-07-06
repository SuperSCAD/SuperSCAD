from super_scad.d3.Ellipsoid4n import Ellipsoid4n
from super_scad.scad.Context import Context
from super_scad.scad.ScadObject import ScadObject
from super_scad.scad.Unit import Unit


class ImperialEllipsoid4n(ScadObject):
    """
    Class for imperial ellipsoids.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 radius_x: float | None = None,
                 radius_y: float | None = None,
                 radius_z: float | None = None,
                 diameter_x: float | None = None,
                 diameter_y: float | None = None,
                 diameter_z: float | None = None) -> None:
        """
        Object constructor.
        """
        ScadObject.__init__(self, args=locals())

        self.imperial_ellipsoid: Ellipsoid4n | None = None
        """
        The imperial ellipsoid.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        context.unit = Unit.INCH

        self.imperial_ellipsoid = Ellipsoid4n(radius_x=self._args.get('radius_x'),
                                              radius_y=self._args.get('radius_y'),
                                              radius_z=self._args.get('radius_z'),
                                              diameter_x=self._args.get('diameter_x'),
                                              diameter_y=self._args.get('diameter_y'),
                                              diameter_z=self._args.get('diameter_z'))

        return self.imperial_ellipsoid

# ----------------------------------------------------------------------------------------------------------------------
