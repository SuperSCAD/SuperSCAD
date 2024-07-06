from super_scad.d3.Cylinder4n import Cylinder4n
from super_scad.scad.Context import Context
from super_scad.scad.ScadObject import ScadObject
from super_scad.scad.Unit import Unit


class ImperialCylinder4n(ScadObject):
    """
    Class for imperial cylinders.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 height: float | None = None,
                 radius: float | None = None,
                 diameter: float | None = None) -> None:
        """
        Object constructor.
        """
        ScadObject.__init__(self, args=locals())

        self.imperial_cylinder: Cylinder4n | None = None
        """
        The imperial cylinder.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        Context.set_unit_length_current(Unit.INCH)

        self.imperial_cylinder = Cylinder4n(height=self._args.get('height'),
                                            radius=self._args.get('radius'),
                                            diameter=self._args.get('diameter'))

        return self.imperial_cylinder

# ----------------------------------------------------------------------------------------------------------------------
