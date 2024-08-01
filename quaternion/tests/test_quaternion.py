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
