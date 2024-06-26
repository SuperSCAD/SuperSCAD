from Private.PrivateScadCommand import PrivateScadCommand


class Text(PrivateScadCommand):
    """
    Class for texts. See https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Text.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 text: str,
                 size: int = 10,
                 font: str | None = None,
                 halign: str = 'left',
                 valign: str = 'baseline',
                 spacing: float = 1.0,
                 direction: str = 'ltr',
                 language: str = 'en',
                 script: str = 'latin',
                 fn: int | None = None):
        """
        Object constructor.

        :param text: See `OpenSCAD text documentation`_.
        :param size: See `OpenSCAD text documentation`_.
        :param font: See `OpenSCAD text documentation`_.
        :param halign: See `OpenSCAD text documentation`_.
        :param valign: See `OpenSCAD text documentation`_.
        :param spacing: See `OpenSCAD text documentation`_.
        :param direction: See `OpenSCAD text documentation`_.
        :param language: See `OpenSCAD text documentation`_.
        :param script: See `OpenSCAD text documentation`_.
        :param fn: See `OpenSCAD text documentation`_.

        .. _OpenSCAD text documentation: https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Text
        """
        PrivateScadCommand.__init__(self, command='text', args=locals())

    # ------------------------------------------------------------------------------------------------------------------
    def _validate_arguments(self) -> None:
        pass

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def fn(self) -> int | None:
        """
        Returns used for subdividing the curved path segments provided by freetype.
        """
        return self._args.get('fn')

# ----------------------------------------------------------------------------------------------------------------------
