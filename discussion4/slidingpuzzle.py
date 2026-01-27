import random

# Adjust N_SCRAMBLES upwards for higher difficulty.
N_SCRAMBLES=12

class SlidingPuzzle:

    # The puzzle contains integers 0 through 15 inclusive.
    puzzle : list[int]
  
    def __init__(self):
        self.puzzle = [(n+1)%16 for n in range(16)]

    def __repr__(self) -> str:
        """Present the puzzle for debugging."""
        return f'SlidingPuzzle({self.puzzle})'
  
    def __str__(self) -> str:
        """Present the puzzle for gameplay."""
        raise NotImplementedError('__str__')

    def up(self) -> None:
        """Move a tile up if possible (otherwise do nothing)."""
        raise NotImplementedError('up')
  
    def down(self) -> None:
        """Move a tile down if possible."""
        raise NotImplementedError('down')
  
    def right(self) -> None:
        """Move a tile right if possible."""
        raise NotImplementedError('right')
  
    def left(self) -> None:
        """Move a tile left is possible."""
        raise NotImplementedError('left')
    
    def scramble(self, n:int) -> None:
        """Make n random moves to scramble the puzzle."""
        raise NotImplementedError('left')

    def solved(self) -> bool:
        """Determine whether or not the puzzle is solved."""
        raise NotImplementedError('solved')
    
def play_game():
    """Play game until solved."""
    pzl = SlidingPuzzle()
    pzl.scramble(N_SCRAMBLES)
    while not pzl.solved():
        print()
        print(pzl)
        cmd = input('\n  w\na s d\n  ')
        match cmd.strip():
            case 'w':
                pzl.up()
            case 'a':
                pzl.left()
            case 's':
                pzl.down()
            case 'd':
                pzl.right()
    print()
    print(pzl)
    print('*** Well done! ***')
    print()
    
# ======

if __name__=='__main__':
   play_game()

