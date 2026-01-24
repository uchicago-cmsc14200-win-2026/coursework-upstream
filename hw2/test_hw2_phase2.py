"""
CMSC 14200
Winter 2026
HW2 Phase2 tests
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
  assert task1.mean([1]) == pytest.approx(1)

def test_task1_mean_03() -> None:
  assert task1.mean([1,2]) == pytest.approx(1.5)

def test_task1_mean_04() -> None:
  assert task1.mean([1,2,3]) == pytest.approx(2)
  
def test_task1_mean_05() -> None:
  assert task1.mean([1,-1,2,-2]) == pytest.approx(0)

def test_task1_mean_06() -> None:
  assert task1.mean([15,1,-1,2,-2]) == pytest.approx(3)

def test_task1_mean_07() -> None:
  assert task1.mean([10,11]) == pytest.approx(10.5)
  
def test_task1_median_01() -> None:
  assert task1.median([]) is None

def test_task1_median_02() -> None:
  assert task1.median([1]) == 1

def test_task1_median_03() -> None:
  assert task1.median([1,2]) in ((1,2),(2,1))

def test_task1_median_04() -> None:
  assert task1.median([1,2,3]) == 2

def test_task1_median_05() -> None:
  assert task1.median([1,3,2]) == 2

def test_task1_median_06() -> None:
  assert task1.median([2,1,3]) == 2

def test_task1_median_07() -> None:
  assert task1.median([4,2,1,3]) in ((2,3),(3,2))

def test_task1_median_08() -> None:
  assert task1.median([1,4,2,3]) in ((2,3),(3,2))

def test_task1_median_09() -> None:
  assert task1.median([1,3,4,2]) in ((2,3),(3,2))

def test_task1_median_0A() -> None:
  assert task1.median([1,3,4,2,5]) == 3

def test_task1_median_0B() -> None:
  assert task1.median([5,1,3,4,2]) == 3

def test_task1_median_0C() -> None:
  assert task1.median([100,1,1,1,0]) == 1

def test_task1_median_0D() -> None:
  assert task1.median([100,1,1,1,1000]) == 1

def test_task1_median_0E() -> None:
  assert task1.median([100,1,1,1,1000,100]) in ((1,100),(100,1))

def test_task1_median_0F() -> None:
  assert task1.median([7,7,7,7,7,7,7,7]) == (7,7)

def test_task1_mode_01() -> None:
  assert task1.mode([]) == []

def test_task1_mode_02() -> None:
  assert task1.mode([1]) == [1]

def test_task1_mode_03() -> None:
  assert sorted(task1.mode([1,2])) == [1,2]

def test_task1_mode_04() -> None:
  assert task1.mode([2,2]) == [2]

def test_task1_mode_05() -> None:
  assert task1.mode([1,2,2]) == [2]

def test_task1_mode_06() -> None:
  assert task1.mode([2,1,2]) == [2]

def test_task1_mode_07() -> None:
  assert task1.mode([2,2,1]) == [2]

def test_task1_mode_08() -> None:
  assert sorted(task1.mode([1,2,2,1])) == [1,2]

def test_task1_mode_09() -> None:
  assert task1.mode([1,2,3,1]) == [1]

def test_task1_mode_0A() -> None:
  assert sorted(task1.mode([1,2,3,1,3])) == [1,3]

# --- Task 2

def sing(n:int) -> BST:
  """convenience method for singleton BSTs"""
  return task2.BSTNode(n,task2.BSTEmpty(),task2.BSTEmpty())

def bstfrom(nums:list[int]) -> BST:
  """build a BST from given integers"""
  t : BST = task2.BSTEmpty()
  for num in nums:
    t = t.insert(num)
  return t

def test_task2_is_empty_00() -> None:
  t = sing(2)
  assert not t.is_empty()

def test_task2_is_leaf_00() -> None:
  t = sing(2)
  assert t.is_leaf()

def test_task2_is_leaf_01() -> None:
  t = task2.BSTNode(4,sing(2),task2.BSTEmpty())
  assert not t.is_leaf()

def test_task2_is_leaf_02() -> None:
  t = task2.BSTNode(0,task2.BSTEmpty(),sing(2))
  assert not t.is_leaf()

def test_task2_is_leaf_03() -> None:
  t = task2.BSTNode(2,sing(0),sing(99))
  assert not t.is_leaf()

def test_task2_num_nodes_00() -> None:
  t = sing(2)
  assert t.num_nodes()==1

def test_task2_num_nodes_01() -> None:
  t = task2.BSTNode(4,sing(2),task2.BSTEmpty())
  assert t.num_nodes()==2

def test_task2_num_nodes_02() -> None:
  t = task2.BSTNode(0,task2.BSTEmpty(),sing(2))
  assert t.num_nodes()==2

def test_task2_num_nodes_03() -> None:
  t = task2.BSTNode(10,sing(8),sing(11))
  assert t.num_nodes()==3

def test_task2_height_00() -> None:
  t = sing(2)
  assert t.height()==1
  
def test_task2_height_01() -> None:
  t = bstfrom([2,0])
  assert t.height()==2

def test_task2_elements_00() -> None:
  t = sing(2)
  assert t.elements()==[2]

def test_task2_elements_01() -> None:
  t = bstfrom([2,3])
  assert t.elements()==[2,3]

def test_task2_elements_02() -> None:
  t = bstfrom([2,1])
  assert t.elements()==[1,2]

def test_task2_elements_03() -> None:
  t = bstfrom([2,1,3])
  assert t.elements()==[1,2,3]

def test_task2_elements_04() -> None:
  t = bstfrom([2,1,3,0])
  assert t.elements()==[0,1,2,3]

def test_task2_elements_05() -> None:
  t = bstfrom([0,2,1,3])
  assert t.elements()==[0,1,2,3]

def test_task2_elements_06() -> None:
  t = bstfrom([3,2,0,1])
  assert t.elements()==[0,1,2,3]

def test_task2_elements_07() -> None:
  t = bstfrom([3,2,0,1,9,4,8,5,6,7])
  assert t.elements()==[0,1,2,3,4,5,6,7,8,9]

def test_task2_min_00() -> None:
  t = sing(1)
  assert t.min() == 1

def test_task2_min_01() -> None:
  t = bstfrom([0,1])
  assert t.min() == 0

def test_task2_min_02() -> None:
  t = bstfrom([1,0])
  assert t.min() == 0
  
def test_task2_min_03() -> None:
  t = bstfrom([1,0,2])
  assert t.min() == 0

def test_task2_min_04() -> None:
  t = bstfrom([2,1,0])
  assert t.min() == 0

def test_task2_min_05() -> None:
  t = bstfrom([0,1,2])
  assert t.min() == 0

def test_task2_min_06() -> None:
  t = bstfrom([5,6,9,8,7,0,1,2,4,3])
  assert t.min() == 0

def test_task2_max_00() -> None:
  t = sing(1)
  assert t.max() == 1

def test_task2_max_01() -> None:
  t = bstfrom([1,0])
  assert t.max() == 1

def test_task2_max_02() -> None:
  t = bstfrom([0,1])
  assert t.max() == 1

def test_task2_max_03() -> None:
  t = bstfrom([0,2,1])
  assert t.max() == 2
  
def test_task2_max_04() -> None:
  t = bstfrom([2,1,0])
  assert t.max() == 2
  
def test_task2_max_05() -> None:
  t = bstfrom([2,0,1])
  assert t.max() == 2
  
def test_task2_max_06() -> None:
  t = bstfrom([0,1,2,9,8,7,4,5,3,6,7,99,22,33,44])
  assert t.max() == 99

def test_task2_mean_00() -> None:
  t = sing(1)
  assert t.mean() == pytest.approx(1)

def test_task2_mean_01() -> None:
  t = bstfrom([1,2])
  assert t.mean() == pytest.approx(1.5)

def test_task2_mean_02() -> None:
  t = bstfrom([2,1])
  assert t.mean() == pytest.approx(1.5)

def test_task2_mean_03() -> None:
  t = bstfrom([2,1,3])
  assert t.mean() == pytest.approx(2.0)

def test_task2_mean_04() -> None:
  t = bstfrom([2,3,1])
  assert t.mean() == pytest.approx(2.0)

def test_task2_mean_05() -> None:
  t = bstfrom([1,2,3])
  assert t.mean() == pytest.approx(2.0)

def test_task2_mean_06() -> None:
  t = bstfrom([1,2,3,4,5,-1,-2,-3,-4,-5])
  assert t.mean() == pytest.approx(0.0)

def test_task2_mean_07() -> None:
  t = bstfrom([1,2,3,4,5,-1,-2,-3,-4,-5,11])
  assert t.mean() == pytest.approx(1.0)

def test_task2_median_00() -> None:
  t = sing(1)
  assert t.median() == 1

def test_task2_median_01() -> None:
  t = bstfrom([1,3])
  assert t.median() in ((1,3),(3,1))

def test_task2_median_02() -> None:
  t = bstfrom([1,3,2])
  assert t.median() == 2

def test_task2_median_03() -> None:
  t = bstfrom([3,2,1])
  assert t.median() == 2

def test_task2_median_04() -> None:
  t = bstfrom([1,2,3])
  assert t.median() == 2

def test_task2_median_05() -> None:
  t = bstfrom([1,2,3,20,21,22,11])
  assert t.median() == 11

def test_task2_median_06() -> None:
  t = bstfrom([12,1,2,3,20,21,22,11])
  assert t.median() in ((11,12),(12,11))

# --- Task 3

# Same convenience methods, but for task3.

# Note: these return BSTNodePre objects so we can test attributes like
# _min and _max.

def sing3(n:int) -> task3.BSTNodePre:
  """convenience method for singleton BSTs"""
  return task3.BSTNodePre(n,task3.BSTEmpty(),task3.BSTEmpty())

def bstfrom3(nums:list[int]) -> task3.BSTNodePre:
  """build a BST from given integers"""
  if len(nums)==0:
    raise ValueError('please supply some integers')
  t = sing3(nums[0])
  for num in nums[1:]:
    t = t.insert(num)
  return t

def test_task3_num_nodes_01() -> None:
  t = sing3(1)
  assert t._num_nodes==1 and t.num_nodes()==1

def test_task3_num_nodes_02() -> None:
  t = bstfrom3([10,5,55])
  assert t._num_nodes==3 and t.num_nodes()==3

def test_task3_num_nodes_03() -> None:
  t = bstfrom3([1,2,3,9,8,7,4,5,6])
  assert t._num_nodes==9 and t.num_nodes()==9

def test_task3_height_01() -> None:
  t = sing3(1)
  assert t._height==1 and t.height()==1

def test_task3_height_02() -> None:
  t = bstfrom3([1,2,3])
  assert t._height==3 and t.height()==3
  
def test_task3_height_03() -> None:
  t = bstfrom3([3,2,1])
  assert t._height==3 and t.height()==3

def test_task3_height_04() -> None:
  t = bstfrom3([2,3,1])
  assert t._height==2 and t.height()==2

def test_task3_min_01() -> None:
  t = sing3(1)
  assert t._min==1 and t.min()==1

def test_task3_min_02() -> None:
  t = bstfrom3([1,2,3])
  assert t._min==1 and t.min()==1

def test_task3_min_03() -> None:
  t = bstfrom3([3,2,1])
  assert t._min==1 and t.min()==1
  
def test_task3_min_04() -> None:
  t = bstfrom3([9,99,999,9999,0,22,222,2222,22222])
  assert t._min==0 and t.min()==0

def test_task3_max_01() -> None:
  t = sing3(1)
  assert t._max==1 and t.max()==1

def test_task3_max_02() -> None:
  t = bstfrom3([1,2,3])
  assert t._max==3 and t.max()==3

def test_task3_max_03() -> None:
  t = bstfrom3([3,2,1])
  assert t._max==3 and t.max()==3
  
def test_task3_max_04() -> None:
  t = bstfrom3([9,99,999,9999,0,22,222,2222,22222])
  assert t._max==22222 and t.max()==22222

def test_task3_mean_00() -> None:
  t = sing3(1)
  assert t._mean==pytest.approx(1) and t.mean()==pytest.approx(1)

def test_task3_mean_01() -> None:
  t = bstfrom3([1,0,2,-1,3])
  assert t._mean==pytest.approx(1) and t.mean()==pytest.approx(1)

def test_task3_mean_02() -> None:
  t = bstfrom3([2,1,3])
  assert t._mean==pytest.approx(2) and t.mean()==pytest.approx(2)

def test_task3_mean_03() -> None:
  t = bstfrom3([1,-1,2,-2,3,-3,4,-4,5,-5])
  assert t._mean==pytest.approx(0) and t.mean()==pytest.approx(0)

def test_task3_mean_04() -> None:
  t = bstfrom3([1,-1,2,-2,3,-3,4,-4,5,-5,110])
  assert t._mean==pytest.approx(10) and t.mean()==pytest.approx(10)
  
def test_task3_median_00() -> None:
  t = sing3(1)
  assert t._median==1 and t.median()==1

def test_task3_median_01() -> None:
  t = bstfrom3([1,2])
  expected = ((1,2),(2,1))
  assert t._median in expected and t.median() in expected

def test_task3_median_02() -> None:
  t = bstfrom3([1,2,3])
  assert t._median==2 and t.median()==2

def test_task3_median_03() -> None:
  t = bstfrom3([4,1,2,3])
  expected = ((2,3),(3,2))
  assert t._median in expected and t.median() in expected

def test_task3_median_04() -> None:
  t = bstfrom3([4,1,2,3,0])
  assert t._median==2 and t.median()==2
  
# --- Task 4

# convenience methods for paths

def quickpath(s : str) -> list[task4.Step]:
  result = []
  for x in s:
    match x:
      case 'L':
        result.append(task4.Step.LEFT)
      case 'R':
        result.append(task4.Step.RIGHT)
      case _:
        raise ValueError('path')
  return result

def checkpath(n : int, p : str) -> bool:
  return task4.int_to_path(n)==quickpath(p)
  
def test_task4_01() -> None:
  assert task4.int_to_path(0)==[]

def test_task4_02() -> None:
  assert task4.int_to_path(1)==[task4.Step.LEFT]

def test_task4_03() -> None:
  assert task4.int_to_path(2)==[task4.Step.RIGHT]
  
def test_task4_04() -> None:
  assert checkpath(3,'LL')

def test_task4_05() -> None:
  assert checkpath(4,'LR')
  
def test_task4_06() -> None:
  assert checkpath(5,'RL')

def test_task4_07() -> None:
  assert checkpath(6,'RR')

def test_task4_08() -> None:
  assert checkpath(7,'LLL')

def test_task4_09() -> None:
  assert checkpath(8,'LLR')
  
def test_task4_0A() -> None:
  assert checkpath(9,'LRL')

def test_task4_0B() -> None:
  assert checkpath(10,'LRR')

def test_task4_0C() -> None:
  assert checkpath(14,'RRR')

def test_task4_0D() -> None:
  assert checkpath(15,'LLLL')
