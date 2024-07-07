import unittest

from super_scad.scad.ArgumentAdmission import ArgumentAdmission


class ArgumentAdmissionTest(unittest.TestCase):
    """
    Test case for ArgumentAdmission.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testExclusiveExclusive(self):
        """
        Test exclusive arguments that are exclusive.
        """
        args = {'radius': 1.0}
        admission = ArgumentAdmission(args)
        admission.validate_exclusive({'radius', 'diameter'})
        self.assertTrue(True)

    # ------------------------------------------------------------------------------------------------------------------
    def testExclusiveNotExclusive(self):
        """
        Test exclusive arguments that are not exclusive.
        """
        args = {'radius': 1.0, 'diameter': 0.5}
        admission = ArgumentAdmission(args)
        self.assertRaises(ValueError, lambda: admission.validate_exclusive({'radius'}, {'diameter'}))

    # ------------------------------------------------------------------------------------------------------------------
    def testRequiredRequired(self):
        """
        Test required arguments that are given.
        """
        args = {'height': 10.0, 'radius': 1.0}
        admission = ArgumentAdmission(args)
        admission.validate_required({'height'}, {'radius', 'diameter'})
        self.assertTrue(True)

    # ------------------------------------------------------------------------------------------------------------------
    def testRequiredNotGiven(self):
        """
        Test required arguments that are given.
        """
        args = {'height': 10.0}
        admission = ArgumentAdmission(args)
        self.assertRaises(ValueError, lambda: admission.validate_required({'height'}, {'radius', 'diameter'}))

# ----------------------------------------------------------------------------------------------------------------------
