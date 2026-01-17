from __future__ import annotations

"""
CMSC 14200, Winter 2026
Homework 2, Task 3

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

from abc import abstractmethod
from bst import BST

import task1

# Note: The following implementation of BSTEmpty is essentially
# identical to the one found in task2.

class BSTEmpty(BST):
    """
    Class to represent an empty BST.
    """
    # No constructor needed

    def is_empty(self) -> bool:
        """See BST"""
        return True

    def is_leaf(self) -> bool:
        """See BST"""
        return False

    def root(self) -> int:
        """See BST"""
        raise TypeError('root() not supported for empty BST')

    def left(self) -> BST:
        """See BST"""
        raise TypeError('left() not supported for empty BST')

    def right(self) -> BST:
        """See BST"""
        raise TypeError('right() not supported for empty BST')

    def elements(self) -> list[int]:
        """See BST"""
        return []

    def contains(self, n: int) -> bool:
        """See BST"""
        return False

    def insert(self, n: int) -> BSTNodePre:
        """See BST"""
        return BSTNodePre(n, self, self)

    def num_nodes(self) -> int:
        """See BST"""
        return 0

    def height(self) -> int:
        """See BST"""
        return 0

    def min(self) -> int|None:
        """See BST"""
        return None

    def max(self) -> int|None:
        """See BST"""
        return None

    def mean(self) -> float|None:
        """See BST"""
        return None

    def median(self) -> int|tuple[int,int]|None:
        """See BST"""
        return None
      
class BSTNodePre(BST):
    """
    Class to represent a node in a BST with precomputed statistics.
    """
    _root: int
    _left: BST
    _right: BST
    # The following attributes are for storing precomputed statistics.
    _num_nodes : int
    _height : int
    _min : int
    _max : int
    _mean : float
    _median : int|tuple[int,int]
    
    def __init__(self, n: int, left: BST, right: BST):
        """
        Constructor

        Inputs:
            n (int): the root at this node
            left (BST): the left child
            right (BST): the right child
        """
        self._root = n
        self._left = left
        self._right = right
        ## TODO: Add precomputation code here in the constructor...
        self._num_nodes = 'fixme'
        self._height = 'fixme'
        self._min = 'fixme'
        self._max = 'fixme'
        self._mean = 'fixme'
        self._median = 'fixme'
        
    def is_empty(self) -> bool:
        """See BST"""
        return False

    def is_leaf(self) -> bool:
        """See BST"""
        return self._left.is_empty() and self._right.is_empty()

    def root(self) -> int:
        """See BST"""
        return self._root

    def left(self) -> BST:
        """See BST"""
        return self._left

    def right(self) -> BST:
        """See BST"""
        return self._right

    def elements(self) -> list[int]:
        """See BST"""
        return self._left.elements() + [self._root] + self._right.elements()

    def contains(self, n: int) -> bool:
        """See BST"""
        if n < self._root:
            return self._left.contains(n)
        elif n > self._root:
            return self._right.contains(n)
        else:
            return True

    def insert(self, n: int) -> "BSTNodePre":
        """See BST"""
        if n < self._root:
            return BSTNodePre(self._root, self._left.insert(n), self._right)
        elif n > self._root:
            return BSTNodePre(self._root, self._left, self._right.insert(n))
        else:
            return self

    def num_nodes(self) -> int:
        """
        Returns precomputed answer; please do not edit this!
        """
        return self._num_nodes

    def height(self) -> int:
        """
        Returns precomputed answer; please do not edit this!
        """
        return self._height

    def min(self) -> int|None:
        """
        Returns precomputed answer; please do not edit this!
        """
        return self._min

    def max(self) -> int|None:
        """
        Returns precomputed answer; please do not edit this!
        """
        return self._max

    def mean(self) -> float|None:
        """
        Returns precomputed answer; please do not edit this!
        """
        return self._mean

    def median(self) -> int|tuple[int,int]|None:
        """
        Returns precomputed answer; please do not edit this!
        """
        return self._median
      
