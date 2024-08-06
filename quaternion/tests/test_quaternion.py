# Copyright (c) 2024 jamesstrudwick
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from quaternion.quaternion import Quaternion
import pytest


def unit_quaternion() -> dict[str, int]:
    """returns a dict respresenting the unit quaternion, used for testing

    Returns
    -------
    dict[str,int]
        The dict with the corresponding x,i,j,k values (all equal to 1)
    """
    return {"x": 1, "i": 1, "j": 1, "k": 1}


class TestQuaternion:

    @pytest.mark.parametrize("entry", ["x", "i", "j", "k"])
    def test_init_vartype(self, entry):
        with pytest.raises(TypeError, match="must be"):
            vals = unit_quaternion()
            vals[entry] = dict()
            Quaternion(**vals)

    def test_init_norm(self):
        """Test the norm is initialised correctly"""
        # assert that the norm is as expected
        assert Quaternion(**unit_quaternion()).norm == 4

    def test__typecheck(self):
        quaternion = Quaternion(**unit_quaternion())

        with pytest.raises(NotImplementedError, match="unsupported operation for: "):
            quaternion._typecheck(dict())

        assert quaternion._typecheck(Quaternion()) is None

    def test_eq(self):
        """Test that the equal method works"""
        # get two instances of the same quaternion
        quaternion_unit_1 = Quaternion(**unit_quaternion())
        quaternion_unit_2 = Quaternion(**unit_quaternion())

        # get a different quaternion
        quaternion_zero = Quaternion()

        # assert the two that the two that are the same work
        assert quaternion_unit_1 == quaternion_unit_2
        # assert that two different ones work
        assert quaternion_unit_1 != quaternion_zero

    def test_str(self):
        """Test that the str method works"""
        # assert that the str rep is as expected
        assert str(Quaternion(0, 0.2, -1, 1)) == "0+0.2i-1j+1k"

    def test_repr(self):
        """Test that the repr method works"""
        # assert that the repr rep is as expected
        assert repr(Quaternion(-12, 6, 24, 12)) == "Quaternion(x=-12, i=6, j=24, k=12)"

    def test_add(self):
        """Test that the add method works"""

        # init quaternions
        quaternion_1 = Quaternion(0, 1, -1, 0.2)
        quaternion_unit = Quaternion(**unit_quaternion())
        quaternion_2 = Quaternion(1, 2, 0, 1.2)

        # assert addition is correct
        assert (quaternion_1 + quaternion_unit) == quaternion_2

    def test_sub(self):
        """Test that the sub method works"""
        # init quaternions
        quaternion_1 = Quaternion(0, 1, -1, 0.2)
        quaternion_unit = Quaternion(**unit_quaternion())
        quaternion_2 = Quaternion(1, 2, 0, 1.2)

        # assert addition is correct
        assert (quaternion_2 - quaternion_unit) == quaternion_1

    def test_rmul(self):
        """Tests that the rmul works"""

        # init test quaternions
        quaternion_unit = Quaternion(**unit_quaternion())
        quaternion_2 = Quaternion(2, 2, 2, 2)
        quaternion_3 = Quaternion(0.2, 0.2, 0.2, 0.2)

        # check correct multiplication
        assert (2 * quaternion_unit) == quaternion_2
        assert (0.2 * quaternion_unit) == quaternion_3

        # test mult with wrong type
        with pytest.raises(NotImplementedError):
            dict() * quaternion_unit

    def test_mul(self):
        "Test that __mul__ works"

        # init quaternions
        quaternion_1 = Quaternion(1, 2, 3, 4)
        quaternion_2 = Quaternion(4, 3, 2, 1)
        quaternion_3 = Quaternion(-12, 6, 24, 12)
        # assert correct output
        assert (quaternion_1 * quaternion_2) == quaternion_3
        # assert non commute
        assert (quaternion_1 * quaternion_2) != (quaternion_2 * quaternion_1)
        # assert correct scalar
        assert (quaternion_1 * 2) == Quaternion(2, 4, 6, 8)

    def test_conjugate(self):
        """Test that conjugation works correctly"""
        # assert correct conjugation
        assert Quaternion(**unit_quaternion()).conjugate() == Quaternion(1, -1, -1, -1)

    def test_inverse(self):
        """Test that the inverse works correctly"""
        # assert correct inverse
        assert Quaternion(**unit_quaternion()).inverse() == Quaternion(
            1 / 4, -1 / 4, -1 / 4, -1 / 4
        )
