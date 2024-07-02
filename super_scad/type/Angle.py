import math


class Angle:
    """
    Utility class for angles.
    """

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def normalize(angle: float, norm: float = 360.0) -> float:
        """
        Returns the normalized angle of an angle. A normalized and is between 0.0 and 360.0 degrees.

        :param angle: The angle to be normalized.
        :param norm: The normalized value,must be a positive value.
        """
        angle = math.fmod(angle, norm)
        if angle < 0.0:
            angle += norm

        return angle

# ----------------------------------------------------------------------------------------------------------------------
