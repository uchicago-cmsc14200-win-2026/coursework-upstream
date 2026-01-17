"""
CMSC 14200
Winter 2026
HW2 Phase1 tests
"""
        
import pytest

from bst import BST

import task1
import task2
import task3
import task4

# --- Task 1

def test_task1_mean_01() -> None:
  assert task1.mean([]) is None

def test_task1_mean_02() -> None:
  assert task1.mean([1]) == 1

def test_task1_median_01() -> None:
  assert task1.median([]) is None

def test_task1_median_02() -> None:
  assert task1.median([1]) == 1
  
def test_task1_median_03() -> None:
  assert task1.median([1,2]) in ((1,2),(2,1))

def test_task1_mode_01() -> None:
  assert task1.mode([]) == []

def test_task1_mode_02() -> None:
  assert task1.mode([1]) == [1]

# --- Task 2

def test_task2_is_empty_00() -> None:
  t = task2.BSTNode(2,task2.BSTEmpty(),task2.BSTEmpty())
  assert not t.is_empty()

def test_task2_is_leaf_00() -> None:
  t = task2.BSTNode(2,task2.BSTEmpty(),task2.BSTEmpty())
  assert t.is_leaf()

def test_num_nodes_00() -> None:
  t = task2.BSTNode(2,task2.BSTEmpty(),task2.BSTEmpty())
  assert t.num_nodes()==1

def test_height_00() -> None:
  t = task2.BSTNode(2,task2.BSTEmpty(),task2.BSTEmpty())
  assert t.height()==1

def test_elements_00() -> None:
  t = task2.BSTNode(2,task2.BSTEmpty(),task2.BSTEmpty())
  assert t.elements()==[2]

def test_elements_01() -> None:
  t = task2.BSTNode(2,task2.BSTEmpty(),task2.BSTEmpty())
  assert t.insert(3).elements()==[2,3]

def test_task2_min_00() -> None:
  t = task2.BSTNode(1,task2.BSTEmpty(),task2.BSTEmpty())
  assert t.min() == 1
  
def test_task2_max_00() -> None:
  t = task2.BSTNode(1,task2.BSTEmpty(),task2.BSTEmpty())
  assert t.max() == 1

def test_task2_mean_00() -> None:
  t = task2.BSTNode(1,task2.BSTEmpty(),task2.BSTEmpty())
  assert t.mean() == 1

def test_task2_median_00() -> None:
  t = task2.BSTNode(1,task2.BSTEmpty(),task2.BSTEmpty())
  assert t.median() == 1

# --- Task 3

def test_task3_num_nodes_01() -> None:
  t = task3.BSTNodePre(1,task3.BSTEmpty(),task3.BSTEmpty())
  assert t._num_nodes==1 and t.num_nodes()==1
  
def test_task3_height_01() -> None:
  t = task3.BSTNodePre(1,task3.BSTEmpty(),task3.BSTEmpty())
  assert t._height==1 and t.height()==1

def test_task3_min_01() -> None:
  t = task3.BSTNodePre(1,task3.BSTEmpty(),task3.BSTEmpty())
  assert t._min==1 and t.min()==1

def test_task3_max_01() -> None:
  t = task3.BSTNodePre(1,task3.BSTEmpty(),task3.BSTEmpty())
  assert t._max==1 and t.max()==1

def test_task3_mean_00() -> None:
  t = task3.BSTNodePre(1,task2.BSTEmpty(),task2.BSTEmpty())
  assert t._mean==1 and t.mean()==1

def test_task3_median_00() -> None:
  t = task3.BSTNodePre(1,task2.BSTEmpty(),task2.BSTEmpty())
  assert t._median==1 and t.median()==1
  
# --- Task 4

def test_task4_01() -> None:
  assert task4.int_to_path(0)==[]

def test_task4_02() -> None:
  assert task4.int_to_path(1)==[task4.Step.LEFT]

def test_task4_03() -> None:
  assert task4.int_to_path(2)==[task4.Step.RIGHT]
