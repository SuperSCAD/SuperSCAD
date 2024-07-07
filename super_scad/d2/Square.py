from super_scad.d2.private.PrivateSquare import PrivateSquare
from super_scad.scad.ArgumentAdmission import ArgumentAdmission
from super_scad.scad.Context import Context
from super_scad.scad.ScadObject import ScadObject


class Square(ScadObject):
    """
    Class for squares.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 size: float,
                 center: bool = False):
        """
        Object constructor.

        :param size: The size of the square.
        :param center: Whether the square is centered at the origin.
        """
        ScadObject.__init__(self, args=locals())

    # ------------------------------------------------------------------------------------------------------------------
    def _validate_arguments(self) -> None:
        """
        Validates the arguments supplied to the constructor of this SuperSCAD object.
        """
        admission = ArgumentAdmission(self._args)
        admission.validate_required({'size'}, {'center'})

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def size(self) -> float:
        """
        Returns the size of the square.
        """
        return self.uc(self._args['size'])

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def center(self) -> bool:
        """
        Returns whether the rectangle is centered at the origin.
        """
        return self._args['center']

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        return PrivateSquare(size=self.size, center=self.center)

# ----------------------------------------------------------------------------------------------------------------------
