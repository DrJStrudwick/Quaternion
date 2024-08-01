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

    def test_add(self):
        """Test that the add method works"""

        # init quaternions
        quaternion_1 = Quaternion(0, 1, -1, 0.2)
        quaternion_unit = Quaternion(**unit_quaternion())
        quaternion_2 = Quaternion(1, 2, 0, 1.2)

        # assert addition is correct
        assert (quaternion_1 + quaternion_unit) == quaternion_2
