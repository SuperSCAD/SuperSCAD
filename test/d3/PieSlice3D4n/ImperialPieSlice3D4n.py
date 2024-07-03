from super_scad.Context import Context
from super_scad.d3.PieSlice3D4n import PieSlice3D4n
from super_scad.ScadObject import ScadObject
from super_scad.Unit import Unit


class ImperialPieSlice3D4n(ScadObject):
    """
    Class for imperial pie slices.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 angle: float | None = None,
                 start_angle: float | None = None,
                 end_angle: float | None = None,
                 radius: float | None = None,
                 inner_radius: float | None = None,
                 outer_radius: float | None = None,
                 height: float):
        """
        Object constructor.
        """
        ScadObject.__init__(self, args=locals())

        self.imperial_pie_slice: PieSlice3D4n | None = None
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

        self.imperial_pie_slice = PieSlice3D4n(angle=self._args.get('angle'),
                                               start_angle=self._args.get('start_angle'),
                                               end_angle=self._args.get('end_angle'),
                                               radius=self._args.get('radius'),
                                               inner_radius=self._args.get('inner_radius'),
                                               outer_radius=self._args.get('outer_radius'),
                                               height=self._args.get('height'))

        return self.imperial_pie_slice

# ----------------------------------------------------------------------------------------------------------------------
