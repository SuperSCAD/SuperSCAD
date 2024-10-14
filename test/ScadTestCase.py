import inspect
import unittest
from pathlib import Path

from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad.scad.Unit import Unit


class ScadTestCase(unittest.TestCase):
    """
    Parent test case for SuperSCAD test cases.
    """

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def create_scad(*, unit_length_final: Unit = Unit.MM) -> Scad:
        """
        Creates the SuperSCAD super object.

        @param unit_length_final: The unit of length used in the generated OpenSCAD code.
        """
        context = Context(unit_length_final=unit_length_final)

        return Scad(context=context)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def paths():
        """
        Returns a path to the actual generated OpenSCAD code and the expected OpenSCAD code.
        """
        directory = Path(inspect.stack()[1][1]).parent
        method = inspect.stack()[1][3]
        path_actual = Path.joinpath(directory, method + '.actual.scad')
        path_expected = Path.joinpath(directory, method + '.expected.scad')

        return path_actual, path_expected

# ----------------------------------------------------------------------------------------------------------------------
