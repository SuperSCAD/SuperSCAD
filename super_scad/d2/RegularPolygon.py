import math
from typing import List

from super_scad.Context import Context
from super_scad.d2.Polygon import Polygon
from super_scad.ScadObject import ScadObject
from super_scad.type.Point2 import Point2
from super_scad.Unit import Unit


class RegularPolygon(ScadObject):
    """
    Class for regular polygons.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 sides: int,
                 outer_radius: float | None = None,
                 inner_radius: float | None = None,
                 size: float | None = None):
        """
        Object constructor.

        :param sides: The number of sider of the regular polygon.
        :param outer_radius: The outer radius (a.k.a. circumradius) of the regular polygon.
        :param inner_radius: The inner radius (a.k.a. apothem) of the regular polygon.
        :param size: The length of a side of the regular polygon.
        """
        ScadObject.__init__(self, args=locals())

        self.__angles: List[float] = []
        """
        The angles of the nodes regular polygon.
        """

        self.__nodes: List[Point2] = []
        """
        The nodes of the regular polygon.
        """

        self.__unit: Unit | None = None
        """
        The unit in which self.__points are calculated.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def _validate_arguments(self) -> None:
        pass

    # ------------------------------------------------------------------------------------------------------------------
    def __nodes_and_angles(self) -> None:
        """
        Computes the nodes ond the angles of the nodes of the regular polygon.
        """
        if len(self.__angles) > 0 and self.__unit == Context.current_target_unit:
            return

        self.__unit = Context.current_target_unit
        self.__nodes.clear()
        self.__angles.clear()

        step = 2.0 * math.pi / self.sides
        radius = self.outer_radius
        if self.sides % 2 == 0:
            # Even number of sides.
            angle = step / 2.0
        else:
            # Odd number of sides.
            angle = math.pi / 2.0

        for i in range(self.sides):
            self.__nodes.append(Point2(x=radius * math.cos(angle), y=radius * math.sin(angle)))
            self.__angles.append(math.degrees(angle))
            angle += step

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def sides(self) -> int:
        """
        Returns the number of sides of the polygon.
        """
        return self._args['sides']

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def outer_radius(self) -> float:
        """
        Returns the outer radius of the regular polygon.
        """
        if 'outer_radius' in self._args:
            return self.uc(self._args['outer_radius'])

        if 'inner_radius' in self._args:
            return self.uc(self._args['inner_radius'] / math.cos(math.pi / self.sides))

        if 'size' in self._args:
            return self.uc(self._args['size'] / (2.0 * math.sin(math.pi / self.sides)))

        return 0.0

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def inner_radius(self) -> float:
        """
        Returns the inner radius of the regular polygon.
        """
        if 'inner_radius' in self._args:
            return self.uc(self._args['inner_radius'])

        if 'outer_radius' in self._args:
            return self.uc(self._args['outer_radius'] * math.cos(math.pi / self.sides))

        if 'size' in self._args:
            return self.uc(self._args['size'] / (2.0 * math.tan(math.pi / self.sides)))

        return 0.0

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def size(self) -> float:
        """
        Returns the inner radius of the regular polygon.
        """
        if 'inner_radius' in self._args:
            return self.uc(2.0 * self._args['inner_radius'] * math.tan(math.pi / self.sides))

        if 'outer_radius' in self._args:
            return self.uc(2.0 * self._args['outer_radius'] * math.sin(math.pi / self.sides))

        if 'size' in self._args:
            return self.uc(self._args['size'])

        return 0.0

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def inner_angle(self) -> float:
        """
        Returns the inner angle in degrees between the edges of the regular polygon.
        """
        return 180.0 - 360.0 / self.sides

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def exterior_angle(self) -> float:
        """
        Returns the exterior angle in degrees between the edges of the regular polygon.
        """
        return 360.0 / self.sides

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def angles(self) -> List[float]:
        """
        Returns the angles in degrees of the position of the nodes of the regular polygon in polar coordinates.
        """
        self.__nodes_and_angles()

        return self.__angles

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def nodes(self) -> List[Point2]:
        """
        Returns the coordinates of the nodes of the regular polygon.
        """
        self.__nodes_and_angles()

        return self.__nodes

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        return Polygon(points=self.nodes)

# ----------------------------------------------------------------------------------------------------------------------
