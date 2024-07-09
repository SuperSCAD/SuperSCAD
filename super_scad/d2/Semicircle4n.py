from super_scad.boolean.Intersection import Intersection
from super_scad.d2.Circle4n import Circle4n
from super_scad.d2.Rectangle import Rectangle
from super_scad.scad.ArgumentAdmission import ArgumentAdmission
from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.transformation.Translate2D import Translate2D


class Semicircle4n(ScadWidget):
    """
    Widget for creating semicircles.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 radius: float | None = None,
                 diameter: float | None = None):
        """
        Object constructor.

        :param radius: The radius of the semicircle.
        :param diameter: The diameter of the semicircle.
        """
        ScadWidget.__init__(self, args=locals())

    # ------------------------------------------------------------------------------------------------------------------
    def _validate_arguments(self) -> None:
        """
        Validates the arguments supplied to the constructor of this SuperSCAD widget.
        """
        admission = ArgumentAdmission(self._args)
        admission.validate_exclusive({'radius'}, {'diameter'})
        admission.validate_required({'radius', 'diameter'})

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def radius(self) -> float:
        """
        Returns the radius of the circle.
        """
        return self.uc(self._args.get('radius', 0.5 * self._args.get('diameter', 0.0)))

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def diameter(self) -> float:
        """
        Returns the diameter of the circle.
        """
        return self.uc(self._args.get('diameter', 2.0 * self._args.get('radius', 0.0)))

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        return Intersection(children=[Circle4n(diameter=self.diameter),
                                      Translate2D(x=-(self.radius + context.eps),
                                                  child=Rectangle(width=self.diameter + 2 * context.eps,
                                                                  depth=self.radius + context.eps))])

# ----------------------------------------------------------------------------------------------------------------------
