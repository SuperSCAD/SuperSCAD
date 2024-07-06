from super_scad.d2.Circle import Circle
from super_scad.scad.Context import Context
from super_scad.scad.ScadObject import ScadObject
from super_scad.scad.Unit import Unit


class ImperialCircle(ScadObject):
    """
    Class for imperial circles.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 radius: float | None = None,
                 diameter: float | None = None,
                 fa: float | None = None,
                 fs: float | None = None,
                 fn: int | None = None) -> None:
        """
        Object constructor.
        """
        ScadObject.__init__(self, args=locals())

        self.imperial_circle: Circle | None = None
        """
        The imperial circle.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        Context.set_unit_length_current(Unit.INCH)

        self.imperial_circle = Circle(radius=self._args.get('radius'),
                                      diameter=self._args.get('diameter'),
                                      fa=self._args.get('fa'),
                                      fs=self._args.get('fs'),
                                      fn=self._args.get('fn'))

        return self.imperial_circle

# ----------------------------------------------------------------------------------------------------------------------
