from super_scad.Context import Context
from super_scad.ScadObject import ScadObject
from super_scad.ScadSingleChildParent import ScadSingleChildParent
from super_scad.transformation.private.PrivateRotate import PrivateRotate
from super_scad.type.Point3 import Point3


class Rotate3D(ScadSingleChildParent):
    """
    Rotates its child degrees about the axis of the coordinate system or around an arbitrary axis. See
    https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Transformations#rotate.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 angle: float | Point3 | None = None,
                 angle_x: float | None = None,
                 angle_y: float | None = None,
                 angle_z: float | None = None,
                 vector: Point3 | None = None,
                 child: ScadObject) -> None:
        """
        Object constructor.

        :param angle: The angle of rotation around all axis or a vector.
        :param angle_x: The angle of rotation around the x-axis.
        :param angle_y: The angle of rotation around the y-axis.
        :param angle_z: The angle of rotation around the z-axis.
        :param vector: The vector of rotation.
        """
        ScadSingleChildParent.__init__(self, args=locals(), child=child)

    # ------------------------------------------------------------------------------------------------------------------
    def _validate_arguments(self) -> None:
        pass

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def angle(self) -> float | Point3 | None:
        """
        Returns the angle around of rotation around a vector.
        """
        if 'vector' in self._args:
            return self._args.get('angle')

        return Point3(self.angle_x, self.angle_y, self.angle_z)

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def angles(self) -> Point3 | None:
        """
        Returns the angle around all three axes.
        """
        if 'vector' in self._args:
            return None

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def angle_x(self) -> float | None:
        """
        Returns the angle of rotation around the x-axis.
        """
        if 'vector' in self._args:
            return None

        if 'angle' in self._args:
            return self._args['angle'].x

        return self._args.get('angle_x', 0.0)

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def angle_y(self) -> float | None:
        """
        Returns the angle of rotation around the y-axis.
        """
        if 'vector' in self._args:
            return None

        if 'angle' in self._args:
            return self._args['angle'].y

        return self._args.get('angle_y', 0.0)

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def angle_z(self) -> float | None:
        """
        Returns the angle of rotation around the z-axis.
        """
        if 'vector' in self._args:
            return None

        if 'angle' in self._args:
            return self._args['angle'].z

        return self._args.get('angle_z', 0.0)

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def vector(self) -> Point3 | None:
        """
        Returns the vector of rotation.
        """
        if 'vector' in self._args:
            return self.uc(self._args['vector'])

        return None

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        return PrivateRotate(angle=self.angle, vector=self.vector, child=self.child)

# ----------------------------------------------------------------------------------------------------------------------
