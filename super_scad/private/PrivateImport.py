import os.path
from abc import ABC
from pathlib import Path
from typing import Dict

from super_scad.private.PrivateScadCommand import PrivateScadCommand


class PrivateImport(PrivateScadCommand, ABC):
    """
    Abstract parent class for Import2D and Import3D. See
    https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Importing_Geometry#import.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 path: Path | str | None = None,
                 convexity: int | None = None,
                 layer: str | None = None):
        """
        Object constructor.

        :param path: The absolute path or the relative path from the target script to the file that will be imported.
        :param convexity: Number of "inward" curves, i.e. expected number of path crossings of an arbitrary line through
                          the child object.
        :param layer: For DXF import only, specify a specific layer to import.
        """
        if path is not None:
            path = str(path)

        if not os.path.isfile(path):
            ValueError('Path "{}" is not a file'.format(path))

        PrivateScadCommand.__init__(self, command='import', args=locals())

    # ------------------------------------------------------------------------------------------------------------------
    def _validate_arguments(self) -> None:
        pass

    # ------------------------------------------------------------------------------------------------------------------
    def argument_map(self) -> Dict[str, str]:
        """
        Returns the map from SuperSCAD arguments to OpenSCAD arguments.
        """
        return {'path': 'file'}

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def convexity(self) -> int | None:
        """
        Returns the number of "inward" curves, i.e. expected number of path crossings of an arbitrary line through the
        child object.
        """
        return self._args.get('convexity')

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def layer(self) -> str | None:
        """
        For DXF import only, return the specific layer to import.
        """
        return self._args.get('layer')

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def path(self) -> Path:
        """
        Returns The absolute path or the relative path from the target script to the file that will be imported.
        """
        return Path(self._args['path'])

# ----------------------------------------------------------------------------------------------------------------------
