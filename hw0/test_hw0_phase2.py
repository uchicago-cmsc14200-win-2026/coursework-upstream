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

def test_bishop_03() -> None:
  b = hw0.bishop('a8')
  s = {'b7','c6','d5','e4','f3','g2','h1'}  
  assert s==b

def test_bishop_04() -> None:
  b = hw0.bishop('h8')
  s = {'a1','b2','c3','d4','e5','f6','g7'}
  assert s==b

def test_bishop_05() -> None:
  b = hw0.bishop('h1')
  s = {'a8','b7','c6','d5','e4','f3','g2'}
  assert s==b

def test_bishop_06() -> None:
  b = hw0.bishop('a4')
  s = {'b5','c6','d7','e8','b3','c2','d1'}
  assert s==b
  
def test_bishop_07() -> None:
  b = hw0.bishop('b8')
  s = {'a7','c7','d6','e5','f4','g3','h2'}
  assert s==b

def test_bishop_08() -> None:
  b = hw0.bishop('h6')
  s = {'f8','g7','g5','f4','e3','d2','c1'}
  assert s==b

def test_bishop_09() -> None:
  b = hw0.bishop('c1')
  s = {'h6','g5','f4','e3','d2','b2','a3'}
  assert s==b
    
def test_bishop_10() -> None:
  b = hw0.bishop('d6')
  s = {'b8','c7','e5','f4','g3','h2','f8','e7','c5','b4','a3'}
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

def test_rook_03() -> None:
  r = hw0.rook('a1')
  s = {'b1','c1','d1','e1','f1','g1','h1','a2','a3','a4','a5','a6','a7','a8'}
  assert s==r

def test_rook_04() -> None:
  r = hw0.rook('g8')
  s = {'a8','b8','c8','d8','e8','f8','h8','g7','g6','g5','g4','g3','g2','g1'}
  assert s==r

def test_rook_05() -> None:
  r = hw0.rook('h2')
  s = {'h1','h3','h4','h5','h6','h7','h8','a2','b2','c2','d2','e2','f2','g2'}
  assert s==r
  
def test_rook_06() -> None:
  r = hw0.rook('e4')
  s = {'a4','b4','c4','d4','f4','g4','h4','e1','e2','e3','e5','e6','e7','e8'}
  assert s==r

def test_queen_00() -> None:
  q = hw0.queen('a1')
  assert 'a2' in q

def test_queen_01() -> None:
  q = hw0.queen('a1')
  assert 'b1' in q

def test_queen_02() -> None:
  q = hw0.queen('a1')
  r = {'b1','c1','d1','e1','f1','g1','h1','a2','a3','a4','a5','a6','a7','a8'}
  b = {'b2','c3','d4','e5','f6','g7','h8'}
  assert q==(r|b)

def test_queen_03() -> None:
  q = hw0.queen('g8')
  r = {'a8','b8','c8','d8','e8','f8','h8','g7','g6','g5','g4','g3','g2','g1'}
  b = {'h7','f7','e6','d5','c4','b3','a2'}
  assert q==(r|b)

def test_queen_04() -> None:
  q = hw0.queen('d6')
  r = {'a6','b6','c6','e6','f6','g6','h6','d8','d7','d5','d4','d3','d2','d1'}
  b = {'b8','c7','e5','f4','g3','h2','a3','b4','c5','e7','f8'}
  assert q==(r|b)


