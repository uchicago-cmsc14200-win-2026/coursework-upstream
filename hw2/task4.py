from __future__ import annotations

"""
CMSC 14200, Winter 2026
Homework 2, Task 4

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

from bst import BST
from enum import Enum
from task2 import BSTEmpty, BSTNode

Step = Enum("Step", ["LEFT", "RIGHT"])
Path = list[Step]

def int_to_path(i: int) -> Path:
    """
    Convert a tree index to a path, denoted as a list of
    left or right steps.

    Raises: ValueError, if i is negative
    """
    raise NotImplementedError('TODO: int_to_path')
