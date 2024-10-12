import os
import unittest
from pathlib import Path

from super_scad.scad.Context import Context
from super_scad.scad.Unit import Unit


class ContextTest(unittest.TestCase):
    """
    Text cases for Context.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_resolve_path(self):
        """
        Test method resolve_path.
        """
        context = Context(project_home=Path(os.getcwd()).resolve(), unit_length_final=Unit.MM, fn=360)

        context.target_path = 'test/test.scad'
        self.assertEqual(Path('/etc/password'), context.resolve_path('/etc/password'))
        self.assertEqual(Path('other/__init__.py'), context.resolve_path('../other/__init__.py'))
        context.target_path = 'test/test.scad'

        context.target_path = 'super_scad/test.scad'
        self.assertEqual(Path('/etc/password'), context.resolve_path('/etc/password'))
        self.assertEqual(Path('../test/other/__init__.py'), context.resolve_path('../other/__init__.py'))

# ----------------------------------------------------------------------------------------------------------------------
