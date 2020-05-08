# -*- coding: utf-8 -*-

import pytest
from tree_matching_distance.main import distance
from ete3 import Tree

__author__ = "arvestad"
__copyright__ = "arvestad"
__license__ = "gpl3"


def test_distance():
    t1 = Tree('((a, b), (c, d));')
    t2 = Tree('((a, c), (b, d));')

    assert distance(t1, t1) == 0
    assert distance(t1, t2) == 2

    small_tree = Tree('(a, (b, c));')
    with pytest.raises(ValueError):
        distance(small_tree, small_tree)
