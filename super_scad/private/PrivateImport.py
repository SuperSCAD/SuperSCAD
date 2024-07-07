from abc import ABC
from pathlib import Path
from typing import Dict

from super_scad.private.PrivateScadCommand import PrivateScadCommand
from super_scad.scad.ArgumentAdmission import ArgumentAdmission
from super_scad.scad.Context import Context
from super_scad.scad.ScadObject import ScadObject


class PrivateImport(PrivateScadCommand, ABC):
    """
    Abstract parent class for Import2D and Import3D. See
    https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Importing_Geometry#import.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 path: Path | str,
                 convexity: int | None = None,
                 layer: str | None = None):
        """
        Object constructor.

        :param path: The absolute path or the relative path from the target script to the file that will be imported.
        :param convexity: Number of "inward" curves, i.e. expected number of path crossings of an arbitrary line through
                          the child object.
        :param layer: For DXF import only, specify a specific layer to import.
        """
        if isinstance(path, Path):
            path = str(path)

        PrivateScadCommand.__init__(self, command='import', args=locals())

    # ------------------------------------------------------------------------------------------------------------------
    def _validate_arguments(self) -> None:
        """
        Validates the arguments supplied to the constructor of this SuperSCAD object.
        """
        admission = ArgumentAdmission(self._args)
        admission.validate_required({'path'})

        # We like to validate here whether the path goes to an exiting readable file, but we need the build context for
        # that. So, we test the existence of the file in the build method.

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

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        path = self.path
        if not path.is_absolute():
            path = context.target_path.parent.joinpath(path)

        if not path.is_file():
            raise FileNotFoundError(f'File {path} does not exist.')

        return self

# ----------------------------------------------------------------------------------------------------------------------
