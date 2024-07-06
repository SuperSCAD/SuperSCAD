from super_scad.d2.Semicircle4n import Semicircle4n
from super_scad.scad.Context import Context
from super_scad.scad.ScadObject import ScadObject
from super_scad.scad.Unit import Unit


class ImperialSemicircle4n(ScadObject):
    """
    Class for imperial semicircles.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 radius: float | None = None,
                 diameter: float | None = None) -> None:
        """
        Object constructor.
        """
        ScadObject.__init__(self, args=locals())

        self.imperial_semicircle4n: Semicircle4n | None = None
        """
        The imperial semicircle.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        context.unit = Unit.INCH

        self.imperial_semicircle4n = Semicircle4n(radius=self._args.get('radius'),
                                                  diameter=self._args.get('diameter'))

        return self.imperial_semicircle4n

# ----------------------------------------------------------------------------------------------------------------------
