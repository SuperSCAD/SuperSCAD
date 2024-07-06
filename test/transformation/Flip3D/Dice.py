from super_scad.boolean.Difference import Difference
from super_scad.boolean.Intersection import Intersection
from super_scad.boolean.Union import Union
from super_scad.scad.Context import Context
from super_scad.d3.Cube import Cube
from super_scad.d3.Sphere import Sphere
from super_scad.scad.ScadObject import ScadObject
from super_scad.transformation.Translate3D import Translate3D
from super_scad.type.Point3 import Point3


class Dice(ScadObject):
    """
    Class for a simple dice.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *, size: float):
        """
        Object constructor.

        :param size: The size of the dice.
        """
        ScadObject.__init__(self)

        self.__size: float = size
        """
        The size of the dice.
        """

        self.__dot_size: float = size / 10.0
        """
        The radius of a dot.
        """

        self.__dot_sep: float = 0.25 * size
        """
        The radius of a dot.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def __build_body(self) -> ScadObject:
        """
        Build the body of the dice.
        """
        return Intersection(children=[Cube(size=self.__size, center=True),
                                      Sphere(radius=0.75 * self.__size, fn=50)])

    # ------------------------------------------------------------------------------------------------------------------
    def __dot_grid_to_point3(self,
                             *,
                             i: int,
                             j: int,
                             x: float | None = None,
                             y: float | None = None,
                             z: float | None = None) -> Point3:
        """
        Converts coordinates for a dot to a vector.
        """
        if x is not None:
            return Point3(x=x, y=i * self.__dot_sep, z=j * self.__dot_sep)

        if y is not None:
            return Point3(x=i * self.__dot_sep, y=y, z=j * self.__dot_sep)

        if z is not None:
            return Point3(x=i * self.__dot_sep, y=j * self.__dot_sep, z=z)

        raise ValueError('Missing fixed plane')

    # ------------------------------------------------------------------------------------------------------------------
    def __build_dot(self,
                    *,
                    i: int,
                    j: int,
                    x: float | None = None,
                    y: float | None = None,
                    z: float | None = None) -> ScadObject:
        """
        Builds a single dot.
        """
        return Translate3D(vector=self.__dot_grid_to_point3(i=i, j=j, x=x, y=y, z=z),
                           child=Sphere(radius=self.__dot_size, fn=50))

    # ------------------------------------------------------------------------------------------------------------------
    def __dots1(self) -> ScadObject:
        """
        Returns the dots for side 1.
        """
        return self.__build_dot(i=0, j=0, x=self.__size / 2.0)

    # ------------------------------------------------------------------------------------------------------------------
    def __dots2(self) -> ScadObject:
        """
        Returns the dots for side 2.
        """
        return Union(children=[self.__build_dot(i=-1, j=1, y=self.__size / 2.0),
                               self.__build_dot(i=1, j=-1, y=self.__size / 2.0), ])

    # ------------------------------------------------------------------------------------------------------------------
    def __dots3(self) -> ScadObject:
        """
        Returns the dots for side 3.
        """
        return Union(children=[self.__build_dot(i=-1, j=1, z=self.__size / 2.0),
                               self.__build_dot(i=0, j=0, z=self.__size / 2.0),
                               self.__build_dot(i=1, j=-1, z=self.__size / 2.0), ])

    # ------------------------------------------------------------------------------------------------------------------
    def __dots4(self) -> ScadObject:
        """
        Returns the dots for side 4.
        """
        return Union(children=[self.__build_dot(i=-1, j=1, z=-self.__size / 2.0),
                               self.__build_dot(i=-1, j=-1, z=-self.__size / 2.0),
                               self.__build_dot(i=1, j=1, z=-self.__size / 2.0),
                               self.__build_dot(i=1, j=-1, z=-self.__size / 2.0)])

    # ------------------------------------------------------------------------------------------------------------------
    def __dots5(self) -> ScadObject:
        """
        Returns the dots for side 5.
        """
        return Union(children=[self.__build_dot(i=-1, j=1, y=-self.__size / 2.0),
                               self.__build_dot(i=-1, j=-1, y=-self.__size / 2.0),
                               self.__build_dot(i=0, j=0, y=-self.__size / 2.0),
                               self.__build_dot(i=1, j=1, y=-self.__size / 2.0),
                               self.__build_dot(i=1, j=-1, y=-self.__size / 2.0)])

    # ------------------------------------------------------------------------------------------------------------------
    def __dots6(self) -> ScadObject:
        """
        Returns the dots for side 6.
        """
        return Union(children=[self.__build_dot(i=-1, j=-1, x=-self.__size / 2.0),
                               self.__build_dot(i=-1, j=0, x=-self.__size / 2.0),
                               self.__build_dot(i=-1, j=1, x=-self.__size / 2.0),
                               self.__build_dot(i=1, j=-1, x=-self.__size / 2.0),
                               self.__build_dot(i=1, j=0, x=-self.__size / 2.0),
                               self.__build_dot(i=1, j=1, x=-self.__size / 2.0)])

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        return Difference(children=[self.__build_body(),
                                    self.__dots1(),
                                    self.__dots2(),
                                    self.__dots3(),
                                    self.__dots4(),
                                    self.__dots5(),
                                    self.__dots6()])

# ----------------------------------------------------------------------------------------------------------------------
