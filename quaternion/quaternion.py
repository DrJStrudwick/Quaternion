# Copyright (c) 2024 jamesstrudwick
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT
# from typing import Self
from __future__ import annotations
import inspect


class Quaternion:
    def __init__(
        self,
        x: int | float = 0,
        i: int | float = 0,
        j: int | float = 0,
        k: int | float = 0,
    ):
        """
        Constructs the attributes for the Quaternion object

        Parameters
        ----------
        x : int | float, optional
            The value for the x component, by default 0
        i : int | float, optional
            The value for the i component, by default 0
        j : int | float, optional
            The value for the j component, by default 0
        k : int | float, optional
            The value for the k component, by default 0

        Raises
        ------
        TypeError
            Is raised if any of the arguments are not an int or float
        """
        self.x = x
        self.i = i
        self.j = j
        self.k = k

        # check input types
        for key, key_type in inspect.get_annotations(self.__init__).items():
            if not isinstance(locals()[key], eval(key_type)):
                raise TypeError(f"{key} must be {key_type}")

    def _typecheck(self, other: any):
        """Checks if another provided object is an instance of this class

        Parameters
        ----------
        other : any
            The other object to be checked

        Raises
        ------
        NotImplementedError
            Is raised if the other object is not an instance of this class
        """
        if not isinstance(other, type(self)):
            raise NotImplementedError(
                "unsupported operation for: "
                f"'{type(self).__name__}' and '{type(other).__name__}'"
            )
