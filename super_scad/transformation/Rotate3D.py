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
                 angle: float | None = None,
                 angles: Point3 | None = None,
                 angle_x: float | None = None,
                 angle_y: float | None = None,
                 angle_z: float | None = None,
                 vector: Point3 | None = None,
                 child: ScadObject) -> None:
        """
        Object constructor.

        :param angle: The angle of rotation around a vector.
        :param angles: The angle of rotation around all three axes.
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
    def angle(self) -> float | None:
        """
        Returns the angle around of rotation around a vector.
        """
        return self._args.get('angle')

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def angles(self) -> Point3 | None:
        """
        Returns the angle around all three axes.
        """
        if 'vector' in self._args:
            return None

        return Point3(self.angle_x, self.angle_y, self.angle_z)

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def angle_x(self) -> float | None:
        """
        Returns the angle of rotation around the x-axis.
        """
        if 'angles' in self._args:
            return self._args['angles'].x

        if 'vector' in self._args:
            return None

        return self._args.get('angle_x', 0.0)

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def angle_y(self) -> float | None:
        """
        Returns the angle of rotation around the y-axis.
        """
        if 'angles' in self._args:
            return self._args['angles'].y

        if 'vector' in self._args:
            return None

        return self._args.get('angle_y', 0.0)

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def angle_z(self) -> float | None:
        """
        Returns the angle of rotation around the z-axis.
        """
        if 'angles' in self._args:
            return self._args['angles'].z

        if 'vector' in self._args:
            return None

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
        if 'vector' in self._args:
            return PrivateRotate(angle=self.angle, vector=self.vector, child=self.child)

        return PrivateRotate(angle=self.angles, child=self.child)

# ----------------------------------------------------------------------------------------------------------------------
