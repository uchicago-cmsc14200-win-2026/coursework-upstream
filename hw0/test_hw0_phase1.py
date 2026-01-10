import pytest
import hw0

def test_bishop_00() -> None:
  b = hw0.bishop('a1')
  assert 'b2' in b

def test_bishop_01() -> None:
  b = hw0.bishop('a1')
  assert {'b2','c3'}.issubset(b)

def test_bishop_02() -> None:
  b = hw0.bishop('a1')
  s = {'b2','c3','d4','e5','f6','g7','h8'}  
  assert s==b

def test_rook_00() -> None:
  r = hw0.rook('a1')
  assert 'a2' in r

def test_rook_01() -> None:
  r = hw0.rook('a1')
  assert {'a2','a3'}.issubset(r)

def test_rook_02() -> None:
  r = hw0.rook('a1')
  assert {'a'+str(f) for f in range(2,9)}.issubset(r)

def test_queen_00() -> None:
  q = hw0.queen('a1')
  assert 'a2' in q

def test_queen_01() -> None:
  q = hw0.queen('a1')
  assert 'b1' in q
