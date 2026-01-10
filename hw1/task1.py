"""
CMSC 14200, Winter 2026
Homework #1, Task #1

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""


def digits_of_int(n: int) -> list[int]:
    """Compute the list of digits of a non-negative integer."""
    raise NotImplementedError("TODO: digits_of_int")


def additive_persistence(n: int) -> int:
    """Compute the additive persistence of a non-negative integer."""
    raise NotImplementedError("TODO: additive_persistence")


def digital_root(n: int) -> int:
    """Compute the digital root of a non-negative integer."""
    raise NotImplementedError("TODO: digital_root")


def digital_roots(start: int, end: int) -> dict[int, list[int]]:
    """
    Compute the digital roots of all numbers starting from start
    to end (both inclusive), and group the numbers in this range
    based on their digital root.

    For example, the resulting dictionary will map the digit 3 to
    the list of numbers in the input range whose digital root is 3.
    The numbers in each list should appear in increasing order.

    Inputs:
      start: An int
      end: An int

    Returns: A dictionary mapping each digit i to the list of
    numbers in the input range whose digital root is i.
    """
    raise NotImplementedError("TODO: digital_roots")
