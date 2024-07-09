from super_scad.private.PrivateSingleChildOpenScadCommand import PrivateSingleChildOpenScadCommand
from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.scad.ScadSingleChildParent import ScadSingleChildParent


class Modify(ScadSingleChildParent):
    """
    Class for applying modifier characters. See
    https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Modifier_Characters#Disable_Modifier
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 disable: bool | None = None,
                 show_only: bool | None = None,
                 highlight: bool | None = None,
                 debug: bool | None = None,
                 transparent: bool | None = None,
                 background: bool | None = None,
                 child: ScadWidget):
        """
        Object constructor.

        :param disable: Whether this child object is ignored.
        :param show_only: Whether to ignore the rest of the design and use this child object as design root.
        :param highlight: Whether this child object is used as usual in the rendering process but also draw it
                          unmodified in transparent pink.
        :param debug: Alias for highlight.
        :param transparent: Whether this child object is used as usual in the rendering process but draw it in
                            transparent gray (all transformations are still applied to the nodes in this tree).
        :param background: Alias for transparent.
        :param child: The child object.
        """
        ScadSingleChildParent.__init__(self, args=locals(), child=child)

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def disable(self) -> bool:
        """
        Returns whether this SuperSCAD widget is ignored.
        """
        return self._args.get('disable', False)

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def show_only(self) -> bool:
        """
        Returns whether to ignore the rest of the design and use this SuperSCAD widget as design root.
        """
        return self._args.get('show_only', False)

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def highlight(self) -> bool:
        """
        Returns whether this SuperSCAD widget is used as usual in the rendering process but also draw it unmodified in
        transparent pink.
        """
        return self._args.get('highlight', False) or self._args.get('debug', False)

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def transparent(self) -> bool:
        """
        Returns whether this SuperSCAD widget is used as usual in the rendering process but draw it in transparent gray
        (all transformations are still applied to the nodes in this tree).
        """
        return self._args.get('transparent', False) or self._args.get('background', False)

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        modifiers = ('*' if self.disable else '') + \
                    ('!' if self.show_only else '') + \
                    ('#' if self.highlight else '') + \
                    ('%' if self.transparent else '')

        if modifiers == '':
            return self.child

        return PrivateSingleChildOpenScadCommand(command=modifiers + 'union', args={}, child=self.child)

# ----------------------------------------------------------------------------------------------------------------------
