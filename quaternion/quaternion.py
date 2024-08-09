# Copyright (c) 2024 jamesstrudwick
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT
# from typing import Self
from __future__ import annotations
import inspect


class Quaternion:
    ROUND_PRECISION = 16

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

        self.x = round(x, self.ROUND_PRECISION)
        self.i = round(i, self.ROUND_PRECISION)
        self.j = round(j, self.ROUND_PRECISION)
        self.k = round(k, self.ROUND_PRECISION)
        self.norm = self.x**2 + self.i**2 + self.j**2 + self.k**2

    def _type_check(self, other: any):
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
        self._type_check(value)

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
            f"{'+' if self.i >= 0 else ''}{self.i}i"
            f"{'+' if self.j >= 0 else ''}{self.j}j"
            f"{'+' if self.k >= 0 else ''}{self.k}k"
        )

    def __repr__(self) -> str:
        """Create the repr for this quaternion

        Returns
        -------
        str
            The repr for this quaternion
        """

        # Produce the repr
        return f"{type(self).__name__}(x={self.x}, i={self.i}, j={self.j}, k={self.k})"

    def __add__(self, other: Quaternion | int | float) -> Quaternion:
        """Add two quaternions together or a quaternion and a scalar

        Parameters
        ----------
        other : Quaternion | int | float
            The other quaternion/scalar to be added

        Returns
        -------
        Quaternion
            The resulting quaternion from the addition
        """
        # if the other object is a scalar
        if isinstance(other, int | float):
            return type(self)(self.x + other, self.i, self.j, self.k)
        # check other is a Quaternion
        self._type_check(other)
        # Perform addition
        return type(self)(
            self.x + other.x, self.i + other.i, self.j + other.j, self.k + other.k
        )

    def __radd__(self, other: int | float) -> Quaternion:
        """Add from the right, for scalars only

        Parameters
        ----------
        other : int | float
            The scalar this quaternion is being added to

        Returns
        -------
        Quaternion
            The resulting quaternion

        Raises
        ------
        NotImplementedError
            Is raised if the other is not a scalar
        """

        # if other object is a scalar
        if isinstance(other, int | float):
            # invoke normal addition, as operation is commutative
            return self.__add__(other=other)
        else:
            raise NotImplementedError

    def __sub__(self, other: Quaternion | int | float) -> Quaternion:
        """Subtract two quaternions or a quaternion and a scalar

        Parameters
        ----------
        other : Quaternion | int | float
            The other quaternion/scalar to be subtracted from this quaternion

        Returns
        -------
        Quaternion
            The resulting quaternion
        """
        # if the other object is a scalar
        if isinstance(other, int | float):
            return type(self)(self.x - other, self.i, self.j, self.k)

        # check other is a Quaternion
        self._type_check(other)
        # perform subtraction and return
        return type(self)(
            self.x - other.x, self.i - other.i, self.j - other.j, self.k - other.k
        )

    def __rsub__(self, other: int | float) -> Quaternion:
        """Sub from the right, for scalars only

        Parameters
        ----------
        other : int | float
            The scalar this quaternion is being subtracted from

        Returns
        -------
        Quaternion
            The resulting quaternion

        Raises
        ------
        NotImplementedError
            Is raised if the other is not a scalar
        """

        # if other object is a scalar
        if isinstance(other, int | float):
            # invoke subtraction, via negation and addition
            return (-1 * self) + other
        else:
            raise NotImplementedError

    def __mul__(self, other: Quaternion | int | float) -> Quaternion:
        """Multiply either two quaternions or quaternions & a scalar

        Parameters
        ----------
        other : Quaternion | int | float
            the other quaternion to be multiplied with

        Returns
        -------
        Quaternion
            The resulting quaternion
        """

        # check if being multiplied by a scalar, if so quick multiply
        if isinstance(other, int | float):
            return Quaternion(
                other * self.x, other * self.i, other * self.j, other * self.k
            )
        # otherwise check other is a quaternion
        self._type_check(other)

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

    def conjugate(self) -> Quaternion:
        """Produce the conjugate of the this quaternion

        Returns
        -------
        Quaternion
            the corresponding conjugate quaternion
        """

        # conjugate is ever non real part negated
        return Quaternion(self.x, -self.i, -self.j, -self.k)

    def inverse(self) -> Quaternion:
        """Produce the inverse of this quaternion

        Returns
        -------
        Quaternion
            The inverse of this quaternion
        """

        # return the inverse of this Quaternion
        return round(1 / self.norm, self.ROUND_PRECISION) * (self.conjugate())
