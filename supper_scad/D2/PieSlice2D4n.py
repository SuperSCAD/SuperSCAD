from Boolean.Difference import Difference
from Boolean.Intersection import Intersection
from Boolean.Union import Union
from Context import Context
from D2.Circle4n import Circle4n
from D2.Square import Square
from ScadObject import ScadObject
from Transformation.Rotate2D import Rotate2D
from Transformation.Translate2D import Translate2D


class PieSlice2D4n(ScadObject):
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
        ScadObject.__init__(self, args=locals())

    # ------------------------------------------------------------------------------------------------------------------
    def _validate_arguments(self) -> None:
        pass

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def angle(self) -> float:
        """
        Returns the angle of the pie slice.
        """
        return self.end_angle - self.start_angle

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def start_angle(self) -> float:
        """
        Returns the start angle of the pie slice.
        """
        return self._args.get('start_angle', 0.0)

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def end_angle(self) -> float:
        """
        Returns the end angle of the pie slice.
        """
        return self._args.get('end_angle', self._args.get('angle', 0.0))

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def radius(self) -> float:
        """
        Returns the outer radius of the pie slice.
        """
        return self.uc(self.outer_radius)

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def inner_radius(self) -> float:
        """
        Returns the inner radius of the pie slice.
        """
        return self.uc(self._args.get('inner_radius', 0.0))

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def outer_radius(self) -> float:
        """
        Returns the outer radius of the pie slice.
        """
        return self.uc(self._args.get('outer_radius', self._args.get('radius', 0.0)))

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        size = self.outer_radius + 2 * context.eps
        trans = self.outer_radius + context.eps
        angle = self.angle

        if angle <= 90.0:
            return Intersection(children=[
                Difference(children=[Circle4n(radius=self.outer_radius), Circle4n(radius=self.inner_radius)]),
                Rotate2D(angle=self.end_angle - 90, child=Square(size=size)),
                Rotate2D(angle=self.start_angle, child=Square(size=size))])

        children = []
        if self.start_angle < 0.0 and self.end_angle > 90.0:
            children.append(Square(size=size))
        if self.start_angle < 90.0 and self.end_angle > 180.0:
            children.append(Translate2D(x=-trans, child=Square(size=size)))
        if self.start_angle < 180.0 and self.end_angle > 270.0:
            children.append(Translate2D(x=-trans, y=-trans, child=Square(size=size)))
        children.append(Rotate2D(angle=self.end_angle - 90, child=Square(size=size)))
        children.append(Rotate2D(angle=self.start_angle, child=Square(size=size)))

        return Intersection(children=[
            Difference(children=[Circle4n(radius=self.outer_radius), Circle4n(radius=self.inner_radius)]),
            Union(children=children)])

# ----------------------------------------------------------------------------------------------------------------------
