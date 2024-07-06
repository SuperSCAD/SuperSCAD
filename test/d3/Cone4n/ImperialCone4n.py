from super_scad.d3.Cone import Cone
from super_scad.d3.Cone4n import Cone4n
from super_scad.scad.Context import Context
from super_scad.scad.ScadObject import ScadObject
from super_scad.scad.Unit import Unit


class ImperialCone4n(ScadObject):
    """
    Class for imperial cones.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 height: float | None = None,
                 top_radius: float | None = None,
                 top_diameter: float | None = None,
                 bottom_radius: float | None = None,
                 bottom_diameter: float | None = None) -> None:
        """
        Object constructor.
        """
        ScadObject.__init__(self, args=locals())

        self.imperial_cone: Cone | None = None
        """
        The imperial cone.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        context.unit = Unit.INCH

        self.imperial_cone = Cone4n(height=self._args.get('height'),
                                    top_radius=self._args.get('top_radius'),
                                    top_diameter=self._args.get('top_diameter'),
                                    bottom_radius=self._args.get('bottom_radius'),
                                    bottom_diameter=self._args.get('bottom_diameter'))

        return self.imperial_cone

# ----------------------------------------------------------------------------------------------------------------------
