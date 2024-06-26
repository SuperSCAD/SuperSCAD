from Context import Context
from D2.Circle4n import Circle4n
from D3.Cylinder import Cylinder
from ScadObject import ScadObject


class Cylinder4n(ScadObject):
    """
    Class for cylinder. See https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Primitive_Solids#cylinder.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 height: float,
                 radius: float | None = None,
                 diameter: float | None = None,
                 center: bool = False):
        """
        Object constructor.

        :param height: See `OpenSCAD cylinder documentation`_.
        :param radius: See `OpenSCAD cylinder documentation`_.
        :param diameter: See `OpenSCAD cylinder documentation`_.
        :param center: See `OpenSCAD cylinder documentation`_.

        .. _OpenSCAD cylinder documentation: https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Primitive_Solids#cylinder
        """
        ScadObject.__init__(self, args=locals())

    # ------------------------------------------------------------------------------------------------------------------
    def _validate_arguments(self) -> None:
        pass

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def center(self) -> bool:
        """
        Returns whether the cylinder is centered along the z-as.
        """
        return self._args['center']

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def diameter(self) -> float:
        """
        Returns the diameter of the cylinder.
        """
        return self.uc(self._args.get('diameter', 2.0 * self._args.get('radius', 0.0)))

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def radius(self) -> float:
        """
        Returns the radius of the cylinder.
        """
        return self.uc(self._args.get('radius', 0.5 * self._args.get('diameter', 0.0)))

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def height(self) -> float:
        """
        Returns the height of the cylinder.
        """
        return self.uc(self._args.get('height', 0.0))

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        return Cylinder(diameter=self.diameter,
                        height=self.height,
                        center=self.center,
                        fn=Circle4n.r2sides4n(self.radius, context))

# ----------------------------------------------------------------------------------------------------------------------
