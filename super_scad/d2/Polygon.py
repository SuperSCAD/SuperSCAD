from typing import List

from super_scad.private.PrivateScadCommand import PrivateScadCommand
from super_scad.type.Path2 import Path2
from super_scad.type.Point2 import Point2


class Polygon(PrivateScadCommand):
    """
    Class for polygons. See https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Using_the_2D_Subsystem#polygon.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *, points: List[Point2], paths: List[Path2] | None = None, convexity: int | None = None):
        """
        Object constructor.

        :param points: See `OpenSCAD polygon documentation`_.
        :param paths: See `OpenSCAD polygon documentation`_
        :param convexity: See `OpenSCAD polygon documentation`_.

        .. _OpenSCAD polygon documentation: https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Using_the_2D_Subsystem#polygon
        """
        PrivateScadCommand.__init__(self, command='polygon', args=locals())

    # ------------------------------------------------------------------------------------------------------------------
    def _validate_arguments(self) -> None:
        pass

# ----------------------------------------------------------------------------------------------------------------------
