======================
tree_matching_distance
======================


An implementation of the tree distance metric suggested by Lin, Rajan, and Moret, at ISBRA 2011.


Description
===========

This package contains a function to import and provides a command-line tool that compares two given
trees and return a distance between them.

Usage
=====

Run the program like::

  tree_matching_distance t1.tree t2.tree

where the two file parameters contain trees in Newick format on the same taxa.

To use the distance method from within your own code, write::

  from ete3 import Tree
  from tree_matching_distance import distance
  t1 = Tree('((a, b), (c, d));')
  t2 = Tree('((a, c), (b, d));')
  d = distance(t1, t2)
  print(d)

for a simple test. Note that this package requires ETE3 trees.
