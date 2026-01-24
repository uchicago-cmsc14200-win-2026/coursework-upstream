"""
CMSC 14200
Winter 2026
Tests for Homework #1
"""

import pytest
import task1
import task2
import task3
from tree import TreeNode
from typing import Any


### TASK 1 TESTS ###

@pytest.mark.parametrize(
    "n, expected",
    [
        (14200, [1, 4, 2, 0, 0]),
        (0, [0]),
        (12345, [1, 2, 3, 4, 5]),
        (840840840, [8, 4, 0, 8, 4, 0, 8, 4, 0]),
    ],
)
def test_task1_digits_of_int(n: int, expected: list[int]) -> None:
    assert task1.digits_of_int(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (9876, 2),
        (12345, 2),
        (840840840, 2),
    ],
)
def test_task1_additive_persistence(n: int, expected: list[int]) -> None:
    assert task1.additive_persistence(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (9876, 3),
        (12345, 6),
        (840840840, 9),
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
    assert task1.digital_roots(0, 3) == expected


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


def test_task1_digital_roots_0_9() -> None:
    expected = {
        0: [0],
        1: [1],
        2: [2],
        3: [3],
        4: [4],
        5: [5],
        6: [6],
        7: [7],
        8: [8],
        9: [9],
    }
    assert task1.digital_roots(0, 9) == expected


def test_task1_digital_roots_0_117() -> None:
    expected = {
        0: [0],
        1: [1, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100, 109],
        2: [2, 11, 20, 29, 38, 47, 56, 65, 74, 83, 92, 101, 110],
        3: [3, 12, 21, 30, 39, 48, 57, 66, 75, 84, 93, 102, 111],
        4: [4, 13, 22, 31, 40, 49, 58, 67, 76, 85, 94, 103, 112],
        5: [5, 14, 23, 32, 41, 50, 59, 68, 77, 86, 95, 104, 113],
        6: [6, 15, 24, 33, 42, 51, 60, 69, 78, 87, 96, 105, 114],
        7: [7, 16, 25, 34, 43, 52, 61, 70, 79, 88, 97, 106, 115],
        8: [8, 17, 26, 35, 44, 53, 62, 71, 80, 89, 98, 107, 116],
        9: [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117],
    }
    assert task1.digital_roots(0, 117) == expected


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (
            200,
            300,
            {
                0: [],
                1: [208, 217, 226, 235, 244, 253, 262, 271, 280, 289, 298],
                2: [200, 209, 218, 227, 236, 245, 254, 263, 272, 281, 290, 299],
                3: [201, 210, 219, 228, 237, 246, 255, 264, 273, 282, 291, 300],
                4: [202, 211, 220, 229, 238, 247, 256, 265, 274, 283, 292],
                5: [203, 212, 221, 230, 239, 248, 257, 266, 275, 284, 293],
                6: [204, 213, 222, 231, 240, 249, 258, 267, 276, 285, 294],
                7: [205, 214, 223, 232, 241, 250, 259, 268, 277, 286, 295],
                8: [206, 215, 224, 233, 242, 251, 260, 269, 278, 287, 296],
                9: [207, 216, 225, 234, 243, 252, 261, 270, 279, 288, 297],
            },
        ),
        (
            14200,
            14250,
            {
                0: [],
                1: [14203, 14212, 14221, 14230, 14239, 14248],
                2: [14204, 14213, 14222, 14231, 14240, 14249],
                3: [14205, 14214, 14223, 14232, 14241, 14250],
                4: [14206, 14215, 14224, 14233, 14242],
                5: [14207, 14216, 14225, 14234, 14243],
                6: [14208, 14217, 14226, 14235, 14244],
                7: [14200, 14209, 14218, 14227, 14236, 14245],
                8: [14201, 14210, 14219, 14228, 14237, 14246],
                9: [14202, 14211, 14220, 14229, 14238, 14247],
            },
        ),
    ],
)
def test_task1_digital_roots(
    start: int, end: int, expected: dict[int, list[int]]
) -> None:
    assert task1.digital_roots(start, end) == expected


### TASK 2 TESTS ###

@pytest.mark.parametrize("list_of_dicts, expected",
                         [([{"a": 2}, {"a": 3}], {"a": 3}),
                          ([{"a": 4, "b": 1}, {"a": 5, "c": 2}], {"a": 5, "b": 1, "c": 2}),
                          ([{"b": 1}, {"c": 2}], {"b": 1, "c": 2}),
                          ([{"a": 4, "b": 1, "c": 10}, {"a": 5, "b": 20, "c": 2}], {"a": 5, "b": 20, "c": 10}),
                          ([{"a": 2, "b": 3}, {}], {"a": 2, "b": 3}),
                          ([{}, {}], {})])
def test_task2(list_of_dicts: list[dict[str, int]], expected: dict[str, int]) -> None:
    assert task2.merge_dictionaries(list_of_dicts) == expected


### TASK 3 TESTS ###

def task3_tester(tree: TreeNode, expected: list[list[int]]) -> None:
    """Test the incrementing_paths function on a given tree"""

    actual = task3.increasing_paths(tree)

    # Sort both lists to make comparison easier
    actual.sort()
    expected.sort()

    assert actual == expected

def test_task3_some_increasing() -> None:
    """
    Tests a tree where some (but not all) paths have increasing values:

        1
       / \\
      3   4
     /   / \\
    5   6   7
       / \\  \\
      1   8   3
    """

    n1 = TreeNode(1)
    n2 = TreeNode(3); n3 = TreeNode(4)
    n4 = TreeNode(5); n5 = TreeNode(6); n6 = TreeNode(7)
    n7 = TreeNode(1); n8 = TreeNode(8); n9 = TreeNode(3)

    n1.add_child(n2); n1.add_child(n3)
    n2.add_child(n4); n3.add_child(n5); n3.add_child(n6)
    n5.add_child(n7); n5.add_child(n8); n6.add_child(n9)

    task3_tester(n1, [[1, 3, 5], [1, 4, 6, 8]])

def test_task3_single_increasing() -> None:
    """
    Tests a tree with a single path with increasing values:

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

def test_task3_all_increasing() -> None:
    """
    Tests a tree where every possible path has increasing values
         1
       /   \\
      2     3
     / \\   / \\
    4   5 7   9
    """
    n1 = TreeNode(1)
    n2 = TreeNode(2); n3 = TreeNode(3)
    n4 = TreeNode(4); n5 = TreeNode(5); n6 = TreeNode(7); n7 = TreeNode(9)

    n1.add_child(n2); n1.add_child(n3)
    n2.add_child(n4); n2.add_child(n5)
    n3.add_child(n6); n3.add_child(n7)

    task3_tester(n1, [[1, 2, 4], [1, 2, 5], [1, 3, 7], [1, 3, 9]])


def test_task3_none_increasing() -> None:
    """
    Tests a tree with no paths with increasing values

         10
       /   \\
      20    3
     / \\   / \\
    4   5 7   9
    """
    n1 = TreeNode(10)
    n2 = TreeNode(20); n3 = TreeNode(3)
    n4 = TreeNode(4); n5 = TreeNode(5); n6 = TreeNode(7); n7 = TreeNode(9)

    n1.add_child(n2); n1.add_child(n3)
    n2.add_child(n4); n2.add_child(n5)
    n3.add_child(n6); n3.add_child(n7)

    task3_tester(n1, [])


def test_task3_strictly_increasing() -> None:
    """
    Tests that we are looking for strictly increasing paths,
    and we did not mistakenly include paths where a value is
    equal (but not greater) than its parent's.

    We use this tree:

         1
       /   \\
      2     3
     / \\   / \\
    1   2 1   3
    """
    n1 = TreeNode(1)
    n2 = TreeNode(2); n3 = TreeNode(3)
    n4 = TreeNode(1); n5 = TreeNode(2); n6 = TreeNode(1); n7 = TreeNode(3)

    n1.add_child(n2); n1.add_child(n3)
    n2.add_child(n4); n2.add_child(n5)
    n3.add_child(n6); n3.add_child(n7)

    task3_tester(n1, [])