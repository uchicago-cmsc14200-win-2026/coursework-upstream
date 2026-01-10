"""
CMSC 14200
Winter 2026
Phase 1 Tests for Homework #1
"""

import pytest

import task1
import task2
import task3

from tree import TreeNode

## TASK 1

# NOTE: You can add more tests by adding to the lists that appear in
# the @pytest.mark.parametrize annotations before each test.

@pytest.mark.parametrize("n, expected", [(14200, [1, 4, 2, 0, 0]), 
                                         (0, [0])])
def test_task1_digits_of_int(n: int, expected: list[int]) -> None:
    assert task1.digits_of_int(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 0),
        (9876, 2)
    ],
)
def test_task1_additive_persistence(n: int, expected: list[int]) -> None:
    assert task1.additive_persistence(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1),
        (9876, 3)
    ],
)
def test_task1_digital_root(n: int, expected: list[int]) -> None:
    assert task1.digital_root(n) == expected


def test_task1_digital_roots_0_3() -> None:
    expected = {
        0: [0],
        1: [1],
        2: [2],
        3: [3],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
    }
    assert task1.digital_roots(0,3) == expected


def test_task1_digital_roots_0_10() -> None:
    expected = {
        0: [0],
        1: [1,10],
        2: [2],
        3: [3],
        4: [4],
        5: [5],
        6: [6],
        7: [7],
        8: [8],
        9: [9],
    }
    assert task1.digital_roots(0,10) == expected


## TASK 2

@pytest.mark.parametrize("list_of_dicts, expected",
                         [([{"a": 2}, {"a": 3}], {"a": 3})])
def test_task2(list_of_dicts: list[dict[str, int]], expected: dict[str, int]) -> None:
    """Do a single test for Task 1: merge_dictionaries"""
    assert task2.merge_dictionaries(list_of_dicts) == expected


## TASK 3

def task3_tester(tree: TreeNode, expected: list[list[int]]) -> None:
    """Test the incrementing_paths function on a given tree"""

    actual = task3.increasing_paths(tree)

    # Sort both lists to make comparison easier
    actual.sort()
    expected.sort()

    assert actual == expected


def test_task3() -> None:
    """
    Tests the tree:

         3
       /   \\
      4     1
     / \\   / \\
    1   5 4   3
    """
    n1 = TreeNode(3)
    n2 = TreeNode(4); n3 = TreeNode(1)
    n4 = TreeNode(1); n5 = TreeNode(5); n6 = TreeNode(4); n7 = TreeNode(3)

    n1.add_child(n2); n1.add_child(n3)
    n2.add_child(n4); n2.add_child(n5)
    n3.add_child(n6); n3.add_child(n7)

    task3_tester(n1, [[3, 4, 5]])
