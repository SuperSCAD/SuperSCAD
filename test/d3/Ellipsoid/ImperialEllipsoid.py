from super_scad.d3.Ellipsoid import Ellipsoid
from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.scad.Unit import Unit


class ImperialEllipsoid(ScadWidget):
    """
    Widget for creating imperial ellipsoids.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 radius_x: float | None = None,
                 radius_y: float | None = None,
                 radius_z: float | None = None,
                 diameter_x: float | None = None,
                 diameter_y: float | None = None,
                 diameter_z: float | None = None,
                 fa: float | None = None,
                 fs: float | None = None,
                 fn: int | None = None) -> None:
        """
        Object constructor.
        """
        ScadWidget.__init__(self, args=locals())

        self.imperial_ellipsoid: Ellipsoid | None = None
        """
        The imperial ellipsoid.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        Context.set_unit_length_current(Unit.INCH)

        self.imperial_ellipsoid = Ellipsoid(radius_x=self._args.get('radius_x'),
                                            radius_y=self._args.get('radius_y'),
                                            radius_z=self._args.get('radius_z'),
                                            diameter_x=self._args.get('diameter_x'),
                                            diameter_y=self._args.get('diameter_y'),
                                            diameter_z=self._args.get('diameter_z'),
                                            fa=self._args.get('fa'),
                                            fs=self._args.get('fs'),
                                            fn=self._args.get('fn'))

        return self.imperial_ellipsoid

# ----------------------------------------------------------------------------------------------------------------------
