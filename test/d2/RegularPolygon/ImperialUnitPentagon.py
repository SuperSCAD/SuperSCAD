from typing import List

from super_scad.Context import Context
from super_scad.d2.RegularPolygon import RegularPolygon
from super_scad.ScadObject import ScadObject
from super_scad.type.Point2 import Point2
from super_scad.Unit import Unit


class ImperialUnitPentagon(ScadObject):
    """
    Class for an imperial unit pentagon.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self) -> None:
        """
        Object constructor.
        """
        ScadObject.__init__(self, args={})

        self.scad_object = None

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def outer_radius(self) -> float:
        """
        Returns the outer radius of the regular polygon.
        """
        return self.scad_object.outer_radius

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def inner_radius(self) -> float:
        """
        Returns the inner radius of the regular polygon.
        """
        return self.scad_object.inner_radius

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def size(self) -> float:
        """
        Returns the size of the regular polygon.
        """
        return self.scad_object.size

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def nodes(self) -> List[Point2]:
        """
        Returns the coordinates of the nodes of the regular polygon.
        """
        return self.scad_object.nodes

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        context.unit = Unit.INCH

        self.scad_object = RegularPolygon(size=1.0, sides=5)
        self.scad_object.nodes  # Force calculation of the nodes in inches.

        return self.scad_object

# ----------------------------------------------------------------------------------------------------------------------
