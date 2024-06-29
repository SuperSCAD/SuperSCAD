from super_scad.Context import Context
from super_scad.d2.Semicircle import Semicircle
from super_scad.ScadObject import ScadObject
from super_scad.Unit import Unit


class ImperialSemicircle(ScadObject):
    """
    Class for imperial semicircles.
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

        self.imperial_semicircle: Semicircle | None = None
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

        self.imperial_semicircle = Semicircle(radius=self._args.get('radius'),
                                              diameter=self._args.get('diameter'),
                                              fa=self._args.get('fa'),
                                              fs=self._args.get('fs'),
                                              fn=self._args.get('fn'))

        return self.imperial_semicircle

# ----------------------------------------------------------------------------------------------------------------------
