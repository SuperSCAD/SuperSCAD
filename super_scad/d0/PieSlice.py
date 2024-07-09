import math

from super_scad.boolean.Difference import Difference
from super_scad.boolean.Empty import Empty
from super_scad.boolean.Intersection import Intersection
from super_scad.d2.Circle import Circle
from super_scad.d2.Polygon import Polygon
from super_scad.d3.LinearExtrude import LinearExtrude
from super_scad.scad.ArgumentAdmission import ArgumentAdmission
from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.type.Angle import Angle
from super_scad.type.Point2 import Point2


class PieSlice(ScadWidget):
    """
    Widget for creating 2D and 3D pie slices.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 height: float | None = None,
                 angle: float | None = None,
                 start_angle: float | None = None,
                 end_angle: float | None = None,
                 radius: float | None = None,
                 inner_radius: float | None = None,
                 outer_radius: float | None = None,
                 fa: float | None = None,
                 fs: float | None = None,
                 fn: int | None = None,
                 fn4n: bool | None = None):
        """
        Object constructor.

        :param height: The height of the pie slice. If height is None, a 2D widget will be created.
        :param angle: The angle of the pie slice (implies starting angle is 0.0).
        :param start_angle: The start angle of the pie slice.
        :param end_angle: The end angle of the pie slice.
        :param radius: The radius of the pie slice (implies inner radius is 0.0).
        :param inner_radius: The inner radius of the pie slice.
        :param outer_radius: The outer radius of the pie slice.
        :param fa: The minimum angle (in degrees) of each fragment.
        :param fs: The minimum circumferential length of each fragment.
        :param fn: The fixed number of fragments in 360 degrees. Values of 3 or more override fa and fs.
        :param fn4n: Whether to create a circle with a multiple of 4 vertices.
        """
        ScadWidget.__init__(self, args=locals())

    # ------------------------------------------------------------------------------------------------------------------
    def _validate_arguments(self) -> None:
        """
        Validates the arguments supplied to the constructor of this SuperSCAD widget.
        """
        admission = ArgumentAdmission(self._args)
        admission.validate_exclusive({'angle'}, {'start_angle', 'end_angle'})
        admission.validate_exclusive({'radius'}, {'inner_radius', 'outer_radius'})
        admission.validate_required({'radius', 'outer_radius'}, {'angle', 'end_angle'})

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def height(self) -> float | None:
        """
        Returns teh height of the pie slice. If height is None, a 2D widget will be created.
        """
        return self.uc(self._args.get('height'))

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def angle(self) -> float:
        """
        Returns the angle of the pie slice.
        """
        return Angle.normalize(self.end_angle - self.start_angle)

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def start_angle(self) -> float:
        """
        Returns the start angle of the pie slice.
        """
        if 'angle' in self._args:
            return Angle.normalize(self._args['angle']) if self._args['angle'] < 0.0 else 0.0

        return Angle.normalize(self._args['start_angle'])

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def end_angle(self) -> float:
        """
        Returns the end angle of the pie slice.
        """
        if 'angle' in self._args:
            return Angle.normalize(self._args['angle']) if self._args['angle'] > 0.0 else 0.0

        return Angle.normalize(self._args['end_angle'])

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def radius(self) -> float:
        """
        Returns the outer radius of the pie slice.
        """
        return self.outer_radius

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
    @property
    def convexity(self) -> int:
        """
        Returns the convexity of the pie slice.
        """
        return 1 if self.angle < 180.0 else 2

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
    def fn4n(self) -> bool | None:
        """
        Returns whether to create a circle with multiple of 4 vertices.
        """
        return self._args.get('fn4n')

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def fn(self) -> int | None:
        """
        Returns the fixed number of fragments in 360 degrees. Values of 3 or more override $fa and $fs.
        """
        return self._args.get('fn')

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        angle = self.angle
        start_angle = self.start_angle
        end_angle = self.end_angle

        if self.outer_radius <= 0.0 or angle == 0.0:  # xxx Use rounding in target units.
            return Empty()

        if self.inner_radius == 0.0:  # xxx Use rounding in target units.
            circles = Circle(radius=self.outer_radius, fa=self.fa, fs=self.fs, fn=self.fn, fn4n=self.fn4n)
        else:
            circles = Difference(children=[Circle(radius=self.outer_radius,
                                                  fa=self.fa,
                                                  fs=self.fs,
                                                  fn=self.fn,
                                                  fn4n=self.fn4n),
                                           Circle(radius=self.inner_radius,
                                                  fa=self.fa,
                                                  fs=self.fs,
                                                  fn=self.fn,
                                                  fn4n=self.fn4n)])

        if round(angle - 360.0, 4) == 0.0:  # xxx Use rounding in target units.
            return circles

        if round(angle - 90.0, 4) < 0.0:  # xxx Use rounding in target units.
            size2 = (self.outer_radius + context.eps) / math.cos(math.radians(Angle.normalize(angle, 90.0) / 2.0))
            points = [Point2(0.0, 0.0),
                      Point2.from_polar_coordinates(size2, start_angle),
                      Point2.from_polar_coordinates(size2, end_angle)]

        elif round(angle - 90.0, 4) == 0.0:  # xxx Use rounding in target units.
            size1 = math.sqrt(2.0) * (self.outer_radius + context.eps)
            size2 = self.outer_radius + context.eps
            points = [Point2(0.0, 0.0),
                      Point2.from_polar_coordinates(size2, start_angle),
                      Point2.from_polar_coordinates(size1, start_angle + 45.0),
                      Point2.from_polar_coordinates(size2, end_angle)]

        elif round(angle - 180.0, 4) == 0.0:  # xxx Use rounding in target units.
            size1 = math.sqrt(2.0) * (self.outer_radius + context.eps)
            size2 = self.outer_radius + context.eps
            points = [Point2.from_polar_coordinates(size2, start_angle),
                      Point2.from_polar_coordinates(size1, start_angle + 45.0),
                      Point2.from_polar_coordinates(size1, start_angle + 135.0),
                      Point2.from_polar_coordinates(size2, end_angle)]

        elif round(angle - 270.0, 4) == 0.0:  # xxx Use rounding in target units.
            size1 = math.sqrt(2.0) * (self.outer_radius + context.eps)
            size2 = self.outer_radius + context.eps
            points = [Point2(0.0, 0.0),
                      Point2.from_polar_coordinates(size2, start_angle),
                      Point2.from_polar_coordinates(size1, start_angle + 45.0),
                      Point2.from_polar_coordinates(size1, start_angle + 135.0),
                      Point2.from_polar_coordinates(size1, start_angle + 225.0),
                      Point2.from_polar_coordinates(size2, end_angle)]

        elif round(angle - 180.0, 4) < 0.0:  # xxx Use rounding in target units.
            phi = Angle.normalize((start_angle - end_angle) / 2.0, 90.0)
            size1 = math.sqrt(2.0) * (self.outer_radius + context.eps)
            size2 = size1 / (math.cos(math.radians(phi)) + math.sin(math.radians(phi)))
            points = [Point2(0.0, 0.0),
                      Point2.from_polar_coordinates(size2, start_angle),
                      Point2.from_polar_coordinates(size1, start_angle - phi + 90.0),
                      Point2.from_polar_coordinates(size1, start_angle - phi + 180.0),
                      Point2.from_polar_coordinates(size2, end_angle)]

        elif round(angle - 360.0, 4) < 0.0:  # xxx Use rounding in target units.
            phi = Angle.normalize((start_angle - end_angle) / 2.0, 90.0)
            size1 = math.sqrt(2.0) * (self.outer_radius + context.eps)
            size2 = size1 / (math.cos(math.radians(phi)) + math.sin(math.radians(phi)))
            points = [Point2(0.0, 0.0),
                      Point2.from_polar_coordinates(size2, start_angle),
                      Point2.from_polar_coordinates(size1, start_angle - phi + 90.0),
                      Point2.from_polar_coordinates(size1, start_angle - phi + 180.0),
                      Point2.from_polar_coordinates(size1, start_angle - phi + 270.0),
                      Point2.from_polar_coordinates(size2, end_angle)]

        else:
            raise ValueError('Math is broken!')

        pie_slice = Intersection(children=[circles, Polygon(points=points, convexity=self.convexity)])

        if self.height is None:
            return pie_slice

        return LinearExtrude(height=self.height, child=pie_slice)

# ----------------------------------------------------------------------------------------------------------------------
