from dataclasses import dataclass


@dataclass
class Size2:
    """
    Size in a 2D space.
    """
    width: float
    """
    The width.
    """

    depth: float
    """
    The depth.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __repr__(self):
        return f"[{self.width}, {self.depth}]"

# ----------------------------------------------------------------------------------------------------------------------
