from Context import Context
from ScadObject import ScadObject
from ScadSingleChildParent import ScadSingleChildParent
from Transformation.Private.PrivateRotate import PrivateRotate


class Rotate2D(ScadSingleChildParent):
    """
    Rotates its child about the z-axis. See https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Transformations#rotate.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *, angle: float | None = None, child: ScadObject) -> None:
        """
        Object constructor.

        :param angle: The angle of rotation (around the z-axis).
        :param child: The child object to be rotated (around the z-axis).
        """
        ScadSingleChildParent.__init__(self, args=locals(), child=child)

    # ------------------------------------------------------------------------------------------------------------------
    def _validate_arguments(self) -> None:
        pass

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def angle(self) -> float:
        """
        Returns the angle of rotation (around the z-axis).
        """
        return self.uc(self._args.get('angle', 0.0))

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        return PrivateRotate(angle=self.angle, child=self.child)

# ----------------------------------------------------------------------------------------------------------------------
