import random
from typing import List

from super_scad.d2.private.PrivatePolygon import PrivatePolygon
from super_scad.scad.ArgumentAdmission import ArgumentAdmission
from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.type.Point2 import Point2


class Polygon(ScadWidget):
    """
    Widget for creating polygons. See https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Using_the_2D_Subsystem#polygon.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 primary: List[Point2] | None = None,
                 points: List[Point2] | None = None,
                 secondary: List[Point2] | None = None,
                 secondaries: List[List[Point2]] | None = None,
                 convexity: int | None = None):
        """
        Object constructor.

        :param primary: The list of 2D points of the polygon.
        :param points: Alias for primary.
        :param secondary: The secondary path that will be subtracted from the polygon.
        :param secondaries: The secondary paths that will be subtracted form the polygon.
        :param convexity: Number of "inward" curves, i.e., expected number of path crossings of an arbitrary line
                          through the child widget.
        """
        ScadWidget.__init__(self, args=locals())

    # ------------------------------------------------------------------------------------------------------------------
    def _validate_arguments(self) -> None:
        """
        Validates the arguments supplied to the constructor of this SuperSCAD widget.
        """
        admission = ArgumentAdmission(self._args)
        admission.validate_exclusive({'primary'}, {'points'})
        admission.validate_exclusive({'secondary'}, {'secondaries'})
        admission.validate_required({'primary', 'points'})

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def inner_angels(self) -> List[float]:
        """
        Returns the inner angels of the polygon (in the same order as the primary points).
        """
        angles = []

        radius: float = 0.0
        nodes = self.primary
        for point in nodes:
            radius = max(radius, point.x, point.y)

        n = len(nodes)
        for i in range(n):
            p1 = nodes[(i - 1) % n]
            p2 = nodes[i]
            p3 = nodes[(i + 1) % n]

            q1 = Point2((p1.x + p2.x + p3.x) / 3, (p1.y + p2.y + p3.y) / 3)
            q2 = Point2.from_polar_coordinates(2.0 * radius, random.uniform(0.0, 360.0))

            number_of_intersections = Polygon._count_intersections(nodes, q1, q2)
            angle = Point2.angle_3p(p1, p2,p3)
            if number_of_intersections % 2 == 0:
                angle = 360.0 - angle

            angles.append(angle)

        return angles

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def primary(self) -> List[Point2]:
        """
        Returns the points of the polygon.
        """
        return self.uc(self._args.get('primary', self._args.get('points')))

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def secondaries(self) -> List[List[Point2]] | None:
        """
        Returns the points of the polygon.
        """
        if 'secondaries' in self._args:
            tmp = []
            for points in self._args['secondaries']:
                tmp.append(self.uc(points))

            return tmp

        if 'secondary' in self._args:
            return [self.uc(self._args['secondary'])]

        return None

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def convexity(self) -> int | None:
        """
        Returns the convexity of the polygon.
        """
        return self._args.get('convexity')

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        secondaries = self.secondaries
        if secondaries is None:
            return PrivatePolygon(points=self.primary, convexity=self.convexity)

        points = self.primary
        n = 0
        m = n + len(points)
        paths = [list(range(n, m))]
        n = m

        for secondary in secondaries:
            m = n + len(secondary)
            points += secondary
            paths.append(list(range(n, m)))
            n = m

        return PrivatePolygon(points=points, paths=paths, convexity=self.convexity)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def _count_intersections(nodes: List[Point2], p1: Point2, q1: Point2) -> int:
        """
        Returns the number of intersections between a line segment (p1, q1) and the vertices of the polygon.

        @param nodes: The nodes of the polygon.
        @param p1: Start point of the line segment.
        @param q1: End point of the line segment.
        """
        intersections = 0

        n = len(nodes)
        for i in range(n):
            p2 = nodes[i]
            q2 = nodes[(i + 1) % n]

            if Point2.do_intersect(p1, q1, p2, q2):
                intersections += 1

        return intersections

# ----------------------------------------------------------------------------------------------------------------------
