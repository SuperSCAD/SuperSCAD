from typing import List, Set

from super_scad.private.PrivateScadCommand import PrivateScadCommand
from super_scad.type.Point2 import Point2


class PrivatePolygon(PrivateScadCommand):
    """
    Class for polygons. See https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Using_the_2D_Subsystem#polygon.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 points: List[Point2],
                 paths: List[List[int]] | None = None,
                 convexity: int | None = None):
        """
        Object constructor.

        :param points: The list of 2D points of the polygon.
        :param paths: The order to traverse the points.
        :param convexity: Integer number of "inward" curves, i.e. expected path crossings of an arbitrary line through
                          the polygon.
        """
        PrivateScadCommand.__init__(self, command='polygon', args=locals())

    # ------------------------------------------------------------------------------------------------------------------
    def argument_lengths(self) -> Set[str]:
        """
        Returns the set with arguments that are lengths.
        """
        return {'points'}

# ----------------------------------------------------------------------------------------------------------------------
