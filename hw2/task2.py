from __future__ import annotations

"""
CMSC 14200, Winter 2026
Homework 2, Task 2

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

    def insert(self, n: int) -> BSTNode:
        """See BST"""
        return BSTNode(n, self, self)

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
      
class BSTNode(BST):
    """
    Class to represent a node in a BST.
    """

    _root: int
    _left: BST
    _right: BST
    # Please don't add additional attributes to BST.
    
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

    def is_empty(self) -> bool:
        """See BST"""
        raise NotImplementedError('TODO: is_empty')

    def is_leaf(self) -> bool:
        """See BST"""
        raise NotImplementedError('TODO: is_leaf')

    def root(self) -> int:
        """See BST"""
        return self._root

    def left(self) -> BST:
        """See BST"""
        return self._left

    def right(self) -> BST:
        """See BST"""
        return self._right

    def num_nodes(self) -> int:
        """See BST"""
        raise NotImplementedError('TODO: num_nodes')

    def height(self) -> int:
        """See BST"""
        raise NotImplementedError('TODO: height')

    def elements(self) -> list[int]:
        """See BST"""
        raise NotImplementedError('TODO: elements')

    def contains(self, n: int) -> bool:
        """See BST"""
        if n < self._root:
            return self._left.contains(n)
        elif n > self._root:
            return self._right.contains(n)
        else:
            return True

    def insert(self, n: int) -> BSTNode:
        """See BST"""
        if n < self._root:
            return BSTNode(self._root, self._left.insert(n), self._right)
        elif n > self._root:
            return BSTNode(self._root, self._left, self._right.insert(n))
        else:
            return self

    def min(self) -> int|None:
        """
        Implements BST.min, exploiting BST ordering property for efficiency.
        """
        raise NotImplementedError('TODO: min')

    def max(self) -> int|None:
        """
        Implements BST.max, exploiting BST ordering property for efficiency.
        """
        raise NotImplementedError('TODO: max')

    def mean(self) -> float|None:
        """See BST"""
        raise NotImplementedError('TODO: mean')

    def median(self) -> int|tuple[int,int]|None:
        """See BST"""
        raise NotImplementedError('TODO: median')

