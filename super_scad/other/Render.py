from super_scad.private.PrivateSingleChildOpenScadCommand import PrivateSingleChildOpenScadCommand
from super_scad.scad.ScadObject import ScadObject


class Render(PrivateSingleChildOpenScadCommand):
    """
    Forces the generation of a mesh even in preview mode. This is useful in certain situations, e.g. when the boolean
    operations become too slow to track. Render can also be used (typically in conjunction with convexity) to
    avoid/workaround preview artifacts. See
    https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Other_Language_Features#render.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 convexity: int | None = None,
                 child: ScadObject):
        """
        Object constructor.

        :param convexity: Number of "inward" curves, i.e. expected number of path crossings of an arbitrary line through
                          the child object.
        """
        PrivateSingleChildOpenScadCommand.__init__(self, command='render', args=locals(), child=child)

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def convexity(self) -> int | None:
        """
        Returns the number of "inward" curves, i.e. expected number of path crossings of an arbitrary line through the
        child object.
        """
        return self._args.get('convexity')

# ----------------------------------------------------------------------------------------------------------------------
