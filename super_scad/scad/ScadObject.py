from abc import ABC, abstractmethod
from typing import Any, Dict, List

from super_scad.scad import Length
from super_scad.scad.Context import Context
from super_scad.scad.Unit import Unit
from super_scad.type.Point2 import Point2
from super_scad.type.Point3 import Point3
from super_scad.type.Size2 import Size2
from super_scad.type.Size3 import Size3


class ScadObject(ABC):
    """
    Abstract parent class for OpenSCAD objects.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *, args: Dict[str, Any] | None = None):
        """
        Object constructor.
        """
        self._args: Dict[str, Any] = {}
        """
        The arguments of this SuperSCAD object.
        """

        self.__unit: Unit = Context.get_unit_length_current()
        """
        The unit of length of the Context of this SuperSCAD object.
        """

        if args is not None:
            for key, value in args.items():
                if value is not None and value != self and key not in ('child', 'children'):
                    self._args[key] = value

        self._validate_arguments()

    # ------------------------------------------------------------------------------------------------------------------
    def _validate_arguments(self) -> None:
        """
        Validates the arguments supplied to the constructor of this SuperSCAD object.
        """
        pass

    # ------------------------------------------------------------------------------------------------------------------
    @abstractmethod
    def build(self, context: Context):
        """
        Builds a SuperSCAD object.

        :param context: The build context.

        :rtype: ScadObject
        """
        raise NotImplementedError()

    # ------------------------------------------------------------------------------------------------------------------
    def uc(self, length: int | float | Point2 | Point3 | Size2 | Size3 | List[Point2] | None) -> \
            float | Point2 | Point3 | Size2 | Size3 | List[Point2] | None:
        """
        Returns the length in the unit of the current context.

        :param length: The length.
        """
        if Context.get_unit_length_current() == self.__unit:
            if isinstance(length, int):
                return float(length)
            return length

        if length is None:
            return None

        if isinstance(length, float):
            return Length.convert(length, self.__unit, Context.get_unit_length_current())

        if isinstance(length, int):
            return Length.convert(float(length), self.__unit, Context.get_unit_length_current())

        if isinstance(length, Point2):
            return Point2(self.uc(length.x), self.uc(length.y))

        if isinstance(length, Point3):
            return Point3(self.uc(length.x), self.uc(length.y), self.uc(length.z))

        if isinstance(length, Size2):
            return Size2(self.uc(length.width), self.uc(length.depth))

        if isinstance(length, Size3):
            return Size3(self.uc(length.width), self.uc(length.depth), self.uc(length.height))

        if isinstance(length, List):
            points = []
            for point in length:
                points.append(self.uc(point))

            return points

        raise ValueError('Can not convert length of type {}.'.format(type(length)))

# ----------------------------------------------------------------------------------------------------------------------
