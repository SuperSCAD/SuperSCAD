from typing import Dict

from super_scad.private.PrivateScadCommand import PrivateScadCommand


class Echo(PrivateScadCommand):
    """
    The echo() module prints the contents to the compilation window (aka Console). See
    https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Other_Language_Features#Echo_module.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, message: str | None = None, **kwargs):
        """
        Object constructor.
        """
        args = {'message': message}
        args.update(kwargs)
        PrivateScadCommand.__init__(self, command='echo', args=args)

    # ------------------------------------------------------------------------------------------------------------------
    def argument_map(self) -> Dict[str, str | None]:
        """
        Returns the map from SuperSCAD arguments to OpenSCAD arguments.
        """
        return {'message': None}

# ----------------------------------------------------------------------------------------------------------------------
