from abc import ABC
from typing import Any, Dict, List

from super_scad.Context import Context
from super_scad.ScadObject import ScadObject


class ScadMultiChildParent(ScadObject, ABC):
    """
    Class for SuperSCAD objects that have multiple children.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *, args: Dict[str, Any], children: List[ScadObject]):
        """
        Object constructor.

        :param children: The child SuperSCAD objects of this multi-child parent.
        """
        ScadObject.__init__(self, args=args)

        self.__children: List[ScadObject] = children
        """
        The child SuperSCAD objects of this multi-child parent.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def children(self) -> List[ScadObject]:
        """
        Returns the children of this multi-child parent.
        """
        return self.__children

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadObject:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        return self

# ----------------------------------------------------------------------------------------------------------------------
