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
        q1 = Quaternion(**unit_quaternion())

        with pytest.raises(NotImplementedError, match="unsupported operation for: "):
            q1._typecheck(dict())

        assert q1._typecheck(Quaternion()) is None
