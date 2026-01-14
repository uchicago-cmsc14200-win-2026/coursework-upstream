# CS142 Winter 2026
# HW0 Sample Solution

pos = str

def valid_pos(s : str) -> bool:
  return len(s)==2 and s[0] in 'abcdefgh' and s[1] in '12345678'

# ------ functions for diagonal adjacency

# move given position by df (delta file) and dr (delta rank)
# return None if the result is off the board
# ex: movepos('a1',1,1) -> 'b2'
# ex: movepos('h4',1,0) -> None
def movepos(p : pos, df : int, dr : int) -> pos|None:
  file, rank = (p[0],int(p[1]))
  fcand = chr(ord(file)+df)
  rcand = rank+dr
  cand = f'{fcand}{rcand}'
  return cand if valid_pos(cand) else None

# add x to the set s if x is not None
def collect(s : set[pos], x : pos|None) -> None:
  if x is not None:
    s.add(x)

# diagonals radiating out of given pos in (up to) four directions
def diagonals(p : pos) -> set[pos]:
  result : set[pos] = set()
  for n in range(1,8):
    for df, dr in [(n,n),(-n,n),(n,-n),(-n,-n)]:
      collect(result, movepos(p,df,dr))
  return result

# ------ functions for orthogonal adjacency

# ex: whole_rank('2') -> {'a2','b2','c2','d2','e2','f2','g2','h2'}
def whole_rank(rank : str) -> set[pos]:
  return {f'{file}{rank}' for file in 'abcdefgh'}

# ex: whole_file('c') -> {'c1','c2','c3','c4','c5','c6','c7','c8'}
def whole_file(file : str) -> set[pos]:
  return {f'{file}{rank}' for rank in '12345678'}

# computes all positions up/down and left/right from p
def orthogonals(p : pos) -> set[pos]:
  return whole_file(p[0])|whole_rank(p[1])

# ------ chess piece functions

# these functions make use of set union (|) and set difference (-)

def rook(p : pos) -> set[pos]:
  return orthogonals(p)-{p}

def bishop(p : pos) -> set[pos]:
  return diagonals(p)-{p}

def queen(p : pos) -> set[pos]:
  return bishop(p)|rook(p)
