from super_scad.d2.PieSlice2D import PieSlice2D
from super_scad.scad.Context import Context
from super_scad.scad.ScadObject import ScadObject
from super_scad.scad.Unit import Unit


class ImperialPieSlice2D(ScadObject):
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
                 fa: float | None = None,
                 fs: float | None = None,
                 fn: int | None = None):
        """
        Object constructor.
        """
        ScadObject.__init__(self, args=locals())

        self.imperial_pie_slice: PieSlice2D | None = None
        """
        The imperial sphere.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        Context.set_unit_length_current(Unit.INCH)

        self.imperial_pie_slice = PieSlice2D(angle=self._args.get('angle'),
                                             start_angle=self._args.get('start_angle'),
                                             end_angle=self._args.get('end_angle'),
                                             radius=self._args.get('radius'),
                                             inner_radius=self._args.get('inner_radius'),
                                             outer_radius=self._args.get('outer_radius'),
                                             fa=self._args.get('fa'),
                                             fs=self._args.get('fs'),
                                             fn=self._args.get('fn'))

        return self.imperial_pie_slice

# ----------------------------------------------------------------------------------------------------------------------
