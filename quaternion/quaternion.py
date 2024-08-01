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
        # check input types
        for key, key_type in inspect.get_annotations(self.__init__).items():
            if not isinstance(locals()[key], eval(key_type)):
                raise TypeError(f"{key} must be {key_type}")

        self.x = round(x, 16)
        self.i = round(i, 16)
        self.j = round(j, 16)
        self.k = round(k, 16)

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

    def __eq__(self, value: Quaternion) -> bool:
        """checks if this quaternion is equal to another

        Parameters
        ----------
        value : Quaternion
            the other quaternion that this is compared against

        Returns
        -------
        bool
            Return True if the two quaternions are equal and False if not
        """
        # check that the other value is an appropriate type
        self._typecheck(value)

        # perform equality check
        is_equal = (
            self.x == value.x
            and self.i == value.i
            and self.j == value.j
            and self.k == value.k
        )
        return is_equal

    def __str__(self) -> str:
        """Create the string representation of this quaternion

        Returns
        -------
        str
            The string representation of the quaternion
        """
        # return the string representing this quaternion
        return (
            f"{self.x}"
            f"{'+' if self.i>=0 else ''}{self.i}i"
            f"{'+' if self.j>=0 else ''}{self.j}j"
            f"{'+' if self.k>=0 else ''}{self.k}k"
        )

    def __add__(self, other: Quaternion) -> Quaternion:
        """Add two quaternions together

        Parameters
        ----------
        other : Quaternion
            The other quaternion to be added

        Returns
        -------
        Quaternion
            The resulting quaternion from the addition
        """
        # check other is a Quaternion
        self._typecheck(other)
        # Perform addition
        return type(self)(
            self.x + other.x, self.i + other.i, self.j + other.j, self.k + other.k
        )

    def __sub__(self, other: Quaternion) -> Quaternion:
        """Subtract two quaternions

        Parameters
        ----------
        other : Quaternion
            The other quaternion to be subracted from this one

        Returns
        -------
        Quaternion
            The rsulting quaternion
        """

        # check other is a Quaternion
        self._typecheck(other)
        # perform subtration and return
        return type(self)(
            self.x - other.x, self.i - other.i, self.j - other.j, self.k - other.k
        )

    def __mul__(self, other: Quaternion) -> Quaternion:
        """Multiply two quaternions

        Parameters
        ----------
        other : Quaternion
            the other quaternion to be multiplied with

        Returns
        -------
        Quaternion
            The resulting quaterion
        """

        # check if being multiplied by a scalar, if so quick mult
        if isinstance(other, int | float):
            return Quaternion(
                other * self.x, other * self.i, other * self.j, other * self.k
            )
        # otherwise check other is a quaternion
        self._typecheck(other)

        # perform x component calculation
        quaternion_x_component = Quaternion(
            self.x * other.x,
            self.x * other.i,
            self.x * other.j,
            self.x * other.k,
        )
        # perform i component calculation
        quaternion_i_component = Quaternion(
            -self.i * other.i,
            self.i * other.x,
            -self.i * other.k,
            self.i * other.j,
        )
        # perform j component calculation
        quaternion_j_component = Quaternion(
            -self.j * other.j,
            self.j * other.k,
            self.j * other.x,
            -self.j * other.i,
        )
        # perform k component calculation
        quaternion_k_component = Quaternion(
            -self.k * other.k,
            -self.k * other.j,
            self.k * other.i,
            self.k * other.x,
        )
        # combine and return
        return (
            quaternion_x_component
            + quaternion_i_component
            + quaternion_j_component
            + quaternion_k_component
        )

    def __rmul__(self, other: int | float) -> Quaternion:
        """multiply from the right, only for scalars

        Parameters
        ----------
        other : int | float
            The scalar to be multiplied with this quaternion

        Returns
        -------
        Quaternion
            The resulting multiplication

        Raises
        ------
        NotImplementedError
            Is raised if the other object is not a int or a float
        """

        # check if scalar, if so do calculation
        if isinstance(other, int | float):
            return Quaternion(
                other * self.x, other * self.i, other * self.j, other * self.k
            )
        else:
            # otherwise raise error
            raise NotImplementedError
