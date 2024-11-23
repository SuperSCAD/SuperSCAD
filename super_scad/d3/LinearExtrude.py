from super_scad.d3.private.PrivateLinearExtrude import PrivateLinearExtrude
from super_scad.scad.Context import Context
from super_scad.scad.ScadSingleChildParent import ScadSingleChildParent
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.transformation.Translate3D import Translate3D
from super_scad.type.Vector2 import Vector2


class LinearExtrude(ScadSingleChildParent):
    """
    Linear Extrusion is an operation that takes a 2D object as input and generates a 3D object as a result. See
    https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Using_the_2D_Subsystem#linear_extrude.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 height: float,
                 center: bool = False,
                 convexity: int | None = None,
                 twist: float = 0.0,
                 scale: float | Vector2 = 1.0,
                 slices: int | None = None,
                 segments: int | None = None,
                 fa: float | None = None,
                 fs: float | None = None,
                 fn: int | None = None,
                 extend_top_by_eps: bool = False,
                 extend_bottom_by_eps: bool = False,
                 child: ScadWidget):
        """
        Object constructor.

        :param height: The height of the extruded object.
        :param center: Whether the extruded object is centered along the z-as.
        :param convexity: Number of "inward" curves, i.e., expected number of path crossings of an arbitrary line 
                          through the child widget.
        :param twist: The number of degrees through which the shape is extruded. Setting the parameter twist = 360
                      extrudes through one revolution. The twist direction follows the left-hand rule.
        :param scale: Scales the 2D shape by this value over the height of the extrusion.
        :param slices: Defines the number of intermediate points along the Z axis of the extrusion. Its default
                       increases with the value of twist. Explicitly setting slices may improve the output refinement.
        :param segments: Adds vertices (points) to the extruded polygon resulting in smoother twisted geometries.
                         Segments need to be a multiple of the polygon's fragments to have an effect (6 or 9... for a
                         circle($fn=3), 8,12... for a square()).
        :param fa: The minimum angle (in degrees) of each fragment.
        :param fs: The minimum circumferential length of each fragment.
        :param fn: The fixed number of fragments in 360 degrees. Values of 3 or more override fa and fs.
        :param extend_top_by_eps: Whether to extend the top by eps for a clear overlap.
        :param extend_bottom_by_eps: Whether to extend the bottom by eps for a clear overlap.
        """
        ScadSingleChildParent.__init__(self, child=child)

        self._height: float = height
        """
        The height of the extruded object.
        """

        self._center: bool = center
        """
        Whether the extruded object is centered along the z-as.
        """

        self._convexity: int | None = convexity
        """
        Number of "inward" curves, i.e., expected number of path crossings of an arbitrary line through the child
        widget.
        """

        self._twist: float = twist
        """
        The number of degrees through which the shape is extruded. 
        """

        self._scale: float | Vector2 = scale
        """
        Scales the 2D shape by this value over the height of the extrusion.
        """

        self._slices: int | None = slices
        """
        DDefines the number of intermediate points along the Z axis of the extrusion. 
        """

        self._segments: int | None = segments
        """
        Adds vertices (points) to the extruded polygon resulting in smoother twisted geometries.
        """

        self._fa: float | None = fa
        """
        The minimum angle (in degrees) of each fragment.
        """

        self._fs: float | None = fs
        """
        The minimum circumferential length of each fragment.
        """

        self._fn: int | None = fn
        """
        The fixed number of fragments in 360 degrees. Values of 3 or more override fa and fs.
        """

        self._extend_top_by_eps: bool = extend_top_by_eps
        """
        Whether to extend the top by eps for a clear overlap.  
        """

        self._extend_bottom_by_eps: bool = extend_bottom_by_eps
        """
        Whether to extend the bottom by eps for a clear overlap.  
        """

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def height(self) -> float:
        """
        Returns the height of the extruded object.
        """
        return self._height

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def center(self) -> bool:
        """
        Returns whether the extruded object is centered along the z-as.
        """
        return self._center

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def convexity(self) -> int | None:
        """
        Returns the number of "inward" curves, i.e., expected number of path crossings of an arbitrary line through the
        child widget.
        """
        return self._convexity

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def twist(self) -> float:
        """
        Returns the number of degrees of through which the shape is extruded. Setting the parameter twist = 360
        extrudes through one revolution. The twist direction follows the left-hand rule.
        """
        return self._twist

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def scale(self) -> float | Vector2:
        """
        Returns the number of degrees of through which the shape is extruded. Setting the parameter twist = 360
        extrudes through one revolution. The twist direction follows the left-hand rule.
        """
        return self._scale

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def slices(self) -> int | None:
        """
        Returns the number of intermediate points along the Z axis of the extrusion. Its default
        increases with the value of twist. Explicitly setting slices may improve the output refinement.
        """
        return self._slices

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def segments(self) -> int | None:
        """
        Returns the Adds vertices (points) to the extruded polygon resulting in smoother twisted geometries.
        """
        return self._segments

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def fa(self) -> float | None:
        """
        Returns the minimum angle (in degrees) of each fragment.
        """
        return self._fa

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def fs(self) -> float | None:
        """
        Returns the minimum circumferential length of each fragment.
        """
        return self._fs

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def fn(self) -> int | None:
        """
        Returns the fixed number of fragments in 360 degrees. Values of 3 or more override $fa and $fs.
        """
        return self._fn

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def extend_top_by_eps(self) -> bool:
        """
        Returns whether to extend the top by eps for a clear overlap.
        """
        return self._extend_top_by_eps

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def extend_bottom_by_eps(self) -> bool:
        """
        Returns whether to extend the bottom by eps for a clear overlap.
        """
        return self._extend_bottom_by_eps

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        height = self._height
        if self._extend_top_by_eps:
            height += context.eps
        if self._extend_bottom_by_eps:
            height += context.eps

        if (not self._extend_bottom_by_eps and not self._extend_top_by_eps) or \
                (self._extend_bottom_by_eps and self._extend_top_by_eps and self._center):
            return PrivateLinearExtrude(height=height,
                                        center=self._center,
                                        convexity=self._convexity,
                                        twist=self._twist,
                                        scale=self._scale,
                                        slices=self._slices,
                                        segments=self._segments,
                                        fa=self._fa,
                                        fs=self._fs,
                                        fn=self._fn,
                                        child=self.child)

        offset = 0.0
        if self._center:
            offset -= 0.5 * self._height
        if self._extend_bottom_by_eps:
            offset -= context.eps

        return Translate3D(z=offset,
                           child=PrivateLinearExtrude(height=height,
                                                      center=False,
                                                      convexity=self._convexity,
                                                      twist=self._twist,
                                                      scale=self._scale,
                                                      slices=self._slices,
                                                      segments=self._segments,
                                                      fa=self._fa,
                                                      fs=self._fs,
                                                      fn=self._fn,
                                                      child=self.child))

# ----------------------------------------------------------------------------------------------------------------------
