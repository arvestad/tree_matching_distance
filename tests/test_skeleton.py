# -*- coding: utf-8 -*-

import pytest
from tree_matching_distance.skeleton import fib

__author__ = "arvestad"
__copyright__ = "arvestad"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
