import math

from super_scad.boolean.Difference import Difference
from super_scad.boolean.Intersection import Intersection
from super_scad.boolean.Union import Union
from super_scad.Context import Context
from super_scad.d2.Circle import Circle
from super_scad.d2.Polygon import Polygon
from super_scad.ScadObject import ScadObject
from super_scad.type.Angle import Angle
from super_scad.type.Point2 import Point2


class PieSlice2D(ScadObject):
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
                 outer_radius: float | None = None,
                 fa: float | None = None,
                 fs: float | None = None,
                 fn: int | None = None):
        """
        Object constructor.

        :param angle:
        :param start_angle:
        :param end_angle:
        :param radius:
        :param inner_radius:
        :param outer_radius:
        :param fa: The minimum angle (in degrees) of each fragment.
        :param fs: The minimum circumferential length of each fragment.
        :param fn: The fixed number of fragments in 360 degrees. Values of 3 or more override fa and fs.
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
    @staticmethod
    def __angular_to_vector(length: float, angle: float, ):
        return Point2(length * math.cos(math.radians(angle)), length * math.sin(math.radians(angle)))

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        angle = self.angle
        start_angle = self.start_angle
        end_angle = self.end_angle

        if self.outer_radius <= 0.0 or angle == 0.0:  # xxx Use rounding in target units.
            return Union(children=[])

        if self.inner_radius == 0.0:  # xxx Use rounding in target units.
            circles = Circle(radius=self.outer_radius, fa=self.fa, fs=self.fs, fn=self.fn)
        else:
            circles = Difference(children=[Circle(radius=self.outer_radius, fa=self.fa, fs=self.fs, fn=self.fn),
                                           Circle(radius=self.inner_radius, fa=self.fa, fs=self.fs, fn=self.fn)])

        if round(angle - 360.0, 4) == 0.0:  # xxx Use rounding in target units.
            return circles

        if round(angle - 90.0, 4) < 0.0:  # xxx Use rounding in target units.
            size2 = self.outer_radius / math.cos(math.radians(Angle.normalize(angle, 90.0) / 2.0)) + context.eps
            points = [Point2(0.0, 0.0),
                      self.__angular_to_vector(size2, start_angle),
                      self.__angular_to_vector(size2, end_angle)]

        elif round(angle - 90.0, 4) == 0.0:  # xxx Use rounding in target units.
            size1 = math.sqrt(2.0) * self.outer_radius + context.eps
            size2 = self.outer_radius + context.eps
            points = [Point2(0.0, 0.0),
                      self.__angular_to_vector(size2, start_angle),
                      self.__angular_to_vector(size1, start_angle + 45.0),
                      self.__angular_to_vector(size2, end_angle)]

        elif round(angle - 180.0, 4) == 0.0:  # xxx Use rounding in target units.
            size1 = math.sqrt(2.0) * self.outer_radius + context.eps
            size2 = self.outer_radius + context.eps
            points = [self.__angular_to_vector(size2, start_angle),
                      self.__angular_to_vector(size1, start_angle + 45.0),
                      self.__angular_to_vector(size1, start_angle + 135.0),
                      self.__angular_to_vector(size2, end_angle)]

        elif round(angle - 270.0, 4) == 0.0:  # xxx Use rounding in target units.
            size1 = math.sqrt(2.0) * self.outer_radius + context.eps
            size2 = self.outer_radius + context.eps
            points = [Point2(0.0, 0.0),
                      self.__angular_to_vector(size2, start_angle),
                      self.__angular_to_vector(size1, start_angle + 45.0),
                      self.__angular_to_vector(size1, start_angle + 135.0),
                      self.__angular_to_vector(size1, start_angle + 225.0),
                      self.__angular_to_vector(size2, end_angle)]

        elif round(angle - 180.0, 4) < 0.0:  # xxx Use rounding in target units.
            phi = Angle.normalize((start_angle - end_angle) / 2.0, 90.0)
            size1 = math.sqrt(2.0) * self.outer_radius + context.eps
            size2 = math.sqrt(2.0) * self.outer_radius / (
                    math.cos(math.radians(phi)) + math.sin(math.radians(phi))) + context.eps
            points = [Point2(0.0, 0.0),
                      self.__angular_to_vector(size2, start_angle),
                      self.__angular_to_vector(size1, start_angle - phi + 90.0),
                      self.__angular_to_vector(size1, start_angle - phi + 180.0),
                      self.__angular_to_vector(size2, end_angle)]

        elif round(angle - 360.0, 4) < 0.0:  # xxx Use rounding in target units.
            phi = Angle.normalize((start_angle - end_angle) / 2.0, 90.0)
            size1 = math.sqrt(2.0) * self.outer_radius + context.eps
            size2 = math.sqrt(2.0) * self.outer_radius / (
                    math.cos(math.radians(phi)) + math.sin(math.radians(phi))) + context.eps
            points = [Point2(0.0, 0.0),
                      self.__angular_to_vector(size2, start_angle),
                      self.__angular_to_vector(size1, start_angle - phi + 90.0),
                      self.__angular_to_vector(size1, start_angle - phi + 180.0),
                      self.__angular_to_vector(size1, start_angle - phi + 270.0),
                      self.__angular_to_vector(size2, end_angle)]

        else:
            raise ValueError('Math is broken!')

        return Intersection(children=[circles, Polygon(points=points, convexity=2)])

# ----------------------------------------------------------------------------------------------------------------------
