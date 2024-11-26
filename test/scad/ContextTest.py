from pathlib import Path

from ScadTestCase import ScadTestCase
from super_scad.boolean.Empty import Empty
from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad.scad.Unit import Unit
from super_scad.type import Vector3


class ContextTest(ScadTestCase):
    """
    Text cases for Context.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_resolve_path(self):
        """
        Test method resolve_path.
        """
        context = Context(unit_length_final=Unit.MM, fn=360)

        context.target_path = 'test/test.scad'
        self.assertEqual(Path('/etc/password'), context.resolve_path('/etc/password'))
        self.assertEqual(Path('other/__init__.py'), context.resolve_path('../other/__init__.py'))
        context.target_path = 'test/test.scad'

        context.target_path = 'super_scad/test.scad'
        self.assertEqual(Path('/etc/password'), context.resolve_path('/etc/password'))
        self.assertEqual(Path('../test/other/__init__.py'), context.resolve_path('../other/__init__.py'))

    # ------------------------------------------------------------------------------------------------------------------
    def test_viewport_default(self):
        """
        Test default viewport.
        """
        context = Context(vpt=Context.DEFAULT_VIEWPORT_TRANSLATION,
                          vpr=Context.DEFAULT_VIEWPORT_ROTATION,
                          vpd=Context.DEFAULT_VIEWPORT_DISTANCE,
                          vpf=Context.DEFAULT_VIEWPORT_FIELD_OF_VIEW)
        scad = Scad(context=context)

        self.assertEqual(Context.DEFAULT_VIEWPORT_TRANSLATION, context.vpt)
        self.assertEqual(Context.DEFAULT_VIEWPORT_ROTATION, context.vpr)
        self.assertEqual(Context.DEFAULT_VIEWPORT_DISTANCE, context.vpd)
        self.assertEqual(Context.DEFAULT_VIEWPORT_FIELD_OF_VIEW, context.vpf)

        empty = Empty()

        path_actual, path_expected = self.paths()
        scad.run_super_scad(empty, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_vpt(self):
        """
        Test viewport translate.
        """
        translation = Vector3(15.0, 25.0, 35.0)
        context = Context(vpt=translation)
        scad = Scad(context=context)

        self.assertEqual(translation, context.vpt)
        self.assertEqual(Context.DEFAULT_VIEWPORT_ROTATION, context.vpr)
        self.assertEqual(Context.DEFAULT_VIEWPORT_DISTANCE, context.vpd)
        self.assertEqual(Context.DEFAULT_VIEWPORT_FIELD_OF_VIEW, context.vpf)

        empty = Empty()

        path_actual, path_expected = self.paths()
        scad.run_super_scad(empty, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_vpr(self):
        """
        Test viewport rotation.
        """
        rotation = Vector3(10.0, 20.0, 30.0)
        context = Context(vpr=rotation)
        scad = Scad(context=context)

        self.assertEqual(Context.DEFAULT_VIEWPORT_TRANSLATION, context.vpt)
        self.assertEqual(rotation, context.vpr)
        self.assertEqual(Context.DEFAULT_VIEWPORT_DISTANCE, context.vpd)
        self.assertEqual(Context.DEFAULT_VIEWPORT_FIELD_OF_VIEW, context.vpf)

        empty = Empty()

        path_actual, path_expected = self.paths()
        scad.run_super_scad(empty, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_vpd(self):
        """
        Test camera distance.
        """
        distance = 13.5
        context = Context(vpd=distance)
        scad = Scad(context=context)

        self.assertEqual(Context.DEFAULT_VIEWPORT_TRANSLATION, context.vpt)
        self.assertEqual(Context.DEFAULT_VIEWPORT_ROTATION, context.vpr)
        self.assertEqual(distance, context.vpd)
        self.assertEqual(Context.DEFAULT_VIEWPORT_FIELD_OF_VIEW, context.vpf)

        empty = Empty()

        path_actual, path_expected = self.paths()
        scad.run_super_scad(empty, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_vpf(self):
        """
        Test the FOV (Field of View) of the view.
        """
        fov = 30.3
        context = Context(vpf=fov)
        scad = Scad(context=context)

        self.assertEqual(Context.DEFAULT_VIEWPORT_TRANSLATION, context.vpt)
        self.assertEqual(Context.DEFAULT_VIEWPORT_ROTATION, context.vpr)
        self.assertEqual(Context.DEFAULT_VIEWPORT_DISTANCE, context.vpd)
        self.assertEqual(fov, context.vpf)

        empty = Empty()

        path_actual, path_expected = self.paths()
        scad.run_super_scad(empty, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
