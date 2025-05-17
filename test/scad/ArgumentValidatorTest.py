import unittest

from super_scad.scad.ArgumentValidator import ArgumentValidator


class ArgumentValidatorTest(unittest.TestCase):
    """
    Test case for ArgumentValidator.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_exclusive_exclusive(self):
        """
        Test exclusive arguments that are exclusive.
        """
        args = {'radius': 1.0}
        validator = ArgumentValidator(args)
        validator.validate_exclusive({'radius', 'diameter'})
        self.assertTrue(True)

    # ------------------------------------------------------------------------------------------------------------------
    def test_exclusive_not_exclusive_set(self):
        """
        Test exclusive arguments that are not exclusive.
        """
        args = {'radius': 1.0, 'diameter': 0.5}
        validator = ArgumentValidator(args)
        self.assertRaises(ValueError, lambda: validator.validate_exclusive({'radius'}, {'diameter'}))

    # ------------------------------------------------------------------------------------------------------------------
    def test_exclusive_not_exclusive_str(self):
        """
        Test exclusive arguments that are not exclusive.
        """
        args = {'radius': 1.0, 'diameter': 0.5}
        validator = ArgumentValidator(args)
        self.assertRaises(ValueError, lambda: validator.validate_exclusive('radius', 'diameter'))

    # ------------------------------------------------------------------------------------------------------------------
    def test_exclusive_not_a_set_or_str(self):
        """
        Test invalid arguments.
        """
        args = {'radius': 1.0}
        validator = ArgumentValidator(args)
        self.assertRaises(TypeError, lambda: validator.validate_exclusive({'radius'}, {'diameter'}, ['height']))

    # ------------------------------------------------------------------------------------------------------------------
    def test_required_required_sets(self):
        """
        Test required arguments that are given.
        """
        args = {'height': 10.0, 'radius': 1.0}
        validator = ArgumentValidator(args)
        validator.validate_required({'height'}, {'radius', 'diameter'})
        self.assertTrue(True)

    # ------------------------------------------------------------------------------------------------------------------
    def test_required_required_sets_and_str(self):
        """
        Test required arguments that are given.
        """
        args = {'height': 10.0, 'radius': 1.0}
        validator = ArgumentValidator(args)
        validator.validate_required('height', {'radius', 'diameter'})
        self.assertTrue(True)

    # ------------------------------------------------------------------------------------------------------------------
    def test_required_not_given_sets(self):
        """
        Test required arguments that are given.
        """
        args = {'height': 10.0}
        validator = ArgumentValidator(args)
        self.assertRaises(ValueError, lambda: validator.validate_required({'height'}, {'radius', 'diameter'}))

    # ------------------------------------------------------------------------------------------------------------------
    def test_required_not_given_sets_and_str1(self):
        """
        Test required arguments that are given.
        """
        args = {'height': 10.0}
        validator = ArgumentValidator(args)
        self.assertRaises(ValueError, lambda: validator.validate_required('height', {'radius', 'diameter'}))

    # ------------------------------------------------------------------------------------------------------------------
    def test_required_not_given_sets_and_str2(self):
        """
        Test required arguments that are given.
        """
        args = {'radius': 10.0}
        validator = ArgumentValidator(args)
        self.assertRaises(ValueError, lambda: validator.validate_required('height', {'radius', 'diameter'}))

    # ------------------------------------------------------------------------------------------------------------------
    def test_required_not_a_set_or_str(self):
        """
        Test invalid arguments.
        """
        args = {'height': 10.0}
        validator = ArgumentValidator(args)
        self.assertRaises(TypeError, lambda: validator.validate_required('height', ['radius', 'diameter']))

    # ------------------------------------------------------------------------------------------------------------------
    def test_argument_count_ok(self):
        """
        Test argument count with correct nummber of arguments.
        """
        args = {'countersink_radius': 10.0, 'countersink_angle': 90, 'countersink_height': None}
        validator = ArgumentValidator(args)
        validator.validate_count(2,
                                 {'countersink_radius', 'countersink_diameter'},
                                 'countersink_angle',
                                 'countersink_height')
        self.assertTrue(True)

    # ------------------------------------------------------------------------------------------------------------------
    def test_argument_count_ok_with_double(self):
        """
        Test argument count with correct nummber of arguments.
        """
        args = {'countersink_radius':   10.0,
                'countersink_diameter': 21.0,
                'countersink_angle':    90,
                'countersink_height':   None}
        validator = ArgumentValidator(args)
        validator.validate_count(2,
                                 {'countersink_radius', 'countersink_diameter'},
                                 'countersink_angle',
                                 'countersink_height')
        self.assertTrue(True)

    # ------------------------------------------------------------------------------------------------------------------
    def test_argument_count_to_less1(self):
        """
        Test argument count with correct nummber of arguments.
        """
        args = {'countersink_radius': 10.0, 'countersink_angle': None, 'countersink_height': None}
        validator = ArgumentValidator(args)
        self.assertRaises(ValueError, lambda: validator.validate_count(2,
                                                                       {'countersink_radius', 'countersink_diameter'},
                                                                       'countersink_angle',
                                                                       'countersink_height'))

    # ------------------------------------------------------------------------------------------------------------------
    def test_argument_count_to_less2(self):
        """
        Test argument count with correct nummber of arguments.
        """
        args = {'countersink_radius': None, 'countersink_angle': None, 'countersink_height': None}
        validator = ArgumentValidator(args)
        self.assertRaises(ValueError, lambda: validator.validate_count(2,
                                                                       {'countersink_radius', 'countersink_diameter'},
                                                                       'countersink_angle',
                                                                       'countersink_height'))

    # ------------------------------------------------------------------------------------------------------------------
    def test_argument_count_to_much(self):
        """
        Test argument count with correct nummber of arguments.
        """
        args = {'countersink_radius': 10.0, 'countersink_angle': 90.0, 'countersink_height': 10.0}
        validator = ArgumentValidator(args)
        self.assertRaises(ValueError, lambda: validator.validate_count(2,
                                                                       {'countersink_radius', 'countersink_diameter'},
                                                                       'countersink_angle',
                                                                       'countersink_height'))

    # ------------------------------------------------------------------------------------------------------------------
    def test_argument_count_wrong_type1(self):
        """
        Test argument count with correct nummber of arguments.
        """
        args = {'countersink_radius': 10.0, 'countersink_angle': 90.0, 'countersink_height': None}
        validator = ArgumentValidator(args)
        self.assertRaises(TypeError, lambda: validator.validate_count(2,
                                                                      ['countersink_radius', 'countersink_diameter'],
                                                                      'countersink_angle',
                                                                      'countersink_height'))

# ----------------------------------------------------------------------------------------------------------------------
