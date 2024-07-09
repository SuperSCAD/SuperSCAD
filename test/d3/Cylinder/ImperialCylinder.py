from super_scad.d3.Cylinder import Cylinder
from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.scad.Unit import Unit


class ImperialCylinder(ScadWidget):
    """
    Widget for creating imperial cylinders.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 height: float | None = None,
                 radius: float | None = None,
                 diameter: float | None = None,
                 fa: float | None = None,
                 fs: float | None = None,
                 fn: int | None = None) -> None:
        """
        Object constructor.
        """
        ScadWidget.__init__(self, args=locals())

        self.imperial_cylinder: Cylinder | None = None
        """
        The imperial cylinder.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        Context.set_unit_length_current(Unit.INCH)

        self.imperial_cylinder = Cylinder(height=self._args.get('height'),
                                          radius=self._args.get('radius'),
                                          diameter=self._args.get('diameter'),
                                          fa=self._args.get('fa'),
                                          fs=self._args.get('fs'),
                                          fn=self._args.get('fn'))

        return self.imperial_cylinder

# ----------------------------------------------------------------------------------------------------------------------
