# CS142 HW0 Winter 2026 (not graded)

# Don't worry about the lack of docstrings in this code. Also, because
# it's didactic, this code is unusually heavy on comments.
 
# The strings that are valid for chess board positions are exactly the
# 64 strings of the form 'a1', 'a2', ..., 'a8', 'b1', ..., 'h8'. More
# precisely, they are strings of length two, the first character of
# which is a letter between 'a' and 'h' (lowercase) inclusive, and the
# second of which is a digit between '1' and '8' inclusive. The
# following image illustrates this coordinate system:
#   https://tinyurl.com/yc78vxr5

# This is a type alias (aka type synonym):

pos = str

# The type alias "pos" is synonymous with "str"; we use "pos" as a
# type in the code below to make clear when a particular string is
# meant to represent a location on a chess board (as opposed to being
# any arbitrary string).

# These are tasks that a) can be coded many different ways, and b)
# rewards good code design, since the logic for the three chess piece
# operations has many commonalities. In other words: think about how
# to craft a flexible toolbox to share among the functions. In still
# other words: write helpers!

# -------- warm-up problem

# valid_pos: ensure that a string is among 'a1', 'a2', ..., 'h8'.
# Don't allow capital letters; 'A1' is not valid, for example.
# Write the code without enumerating all 64 possibilities.
# (In code, fully enumerating all possibilities should be avoided when
# easy to avoid.)

def valid_pos(s : str) -> bool:
    raise NotImplementedError('valid_pos')

# -------- main problems

# "GIGO" means "garbage in, garbage out." It means that if a given
# input is "garbage" (i.e., doesn't meet expected constraints), then
# the function can behave in any arbitrary way thereafter. (Raising a
# ValueError is a reasonable thing to do, but not mandated.)

# The following functions return sets because a) we don't want
# duplicates among the answers, and b) order doesn't matter in the
# answers.

# rook: produce all locations a rook could move to from the given
# location. Assume the board is empty; i.e., there are no obstacles
# anywhere.
# If p is not a valid chess position, GIGO.

def rook(p : pos) -> set[pos]:
    raise NotImplementedError('rook')

# bishop: produce all locations a bishop could move to from the given
# location. Assume the board is empty; i.e., there are no obstacles
# anywhere.
# If p is not a valid chess position, GIGO.

def bishop(p : pos) -> set[pos]:
    raise NotImplementedError('bishop')

# queen: produce all locations a queen could move to from the given
# location.  Assume the board is empty; i.e., there are no obstacles
# anywhere.
# If p is not a valid chess position, GIGO.

def queen(p : pos) -> set[pos]:
    raise NotImplementedError('queen')
