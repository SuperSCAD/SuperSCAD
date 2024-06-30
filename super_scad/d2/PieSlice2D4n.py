from super_scad.d2.Circle4n import Circle4n
from super_scad.d2.private.PrivatePieSlice2D import PrivatePieSlice2D
from super_scad.ScadObject import ScadObject


class PieSlice2D4n(PrivatePieSlice2D):
    """
    Class for 2D pie slices.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 angle: float | None = None,
                 start_angle: float | None = None,
                 end_angle: float | None = None,
                 radius: float | None = None,
                 inner_radius: float | None = None,
                 outer_radius: float | None = None):
        """
        Object constructor.

        :param angle:
        :param start_angle:
        :param end_angle:
        :param radius:
        :param inner_radius:
        :param outer_radius:
        """
        PrivatePieSlice2D.__init__(self, args=locals())

    # ------------------------------------------------------------------------------------------------------------------
    def _validate_arguments(self) -> None:
        pass

    # ------------------------------------------------------------------------------------------------------------------
    def _create_circle(self, radius: float) -> ScadObject:
        """
        Creates a circle with given radius.

        :param radius: Radius of the circle.
        """
        return Circle4n(radius=radius)

# ----------------------------------------------------------------------------------------------------------------------
