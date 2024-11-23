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
    def test_exclusive_not_exclusive(self):
        """
        Test exclusive arguments that are not exclusive.
        """
        args = {'radius': 1.0, 'diameter': 0.5}
        validator = ArgumentValidator(args)
        self.assertRaises(ValueError, lambda: validator.validate_exclusive({'radius'}, {'diameter'}))

    # ------------------------------------------------------------------------------------------------------------------
    def test_required_required(self):
        """
        Test required arguments that are given.
        """
        args = {'height': 10.0, 'radius': 1.0}
        validator = ArgumentValidator(args)
        validator.validate_required({'height'}, {'radius', 'diameter'})
        self.assertTrue(True)

    # ------------------------------------------------------------------------------------------------------------------
    def test_required_not_given(self):
        """
        Test required arguments that are given.
        """
        args = {'height': 10.0}
        validator = ArgumentValidator(args)
        self.assertRaises(ValueError, lambda: validator.validate_required({'height'}, {'radius', 'diameter'}))

# ----------------------------------------------------------------------------------------------------------------------
