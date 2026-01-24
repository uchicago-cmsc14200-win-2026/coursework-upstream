"""
CMSC 14200, Winter 2026
Homework #3

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""
from typing import Optional
from graph import UndirectedGraph


class PrecompGraph(UndirectedGraph):
    """
    Class to represent a graph over words in a language.
    Words are vertices.
    Edges connect words of the same length that are identical except at one
    letter.
    Vertices and information about adjacent vertices are explicitly stored.
    """

    def __init__(self, wordfile: str, maxlen: int):
        """Construct a new graph based on the specified file listing words,
           ignoring any words longer than specified length"""
        raise NotImplementedError


class LetterSeqGraph(UndirectedGraph):
    """
    Class to represent a graph over strings comprised exclusively of
    lower-case letters.
    Strings, representing pseudo-words, are vertices.
    Edges connect strings of the same length that are identical except at one
    letter.
    Adjacency is determined on demand and not stored.
    """

    def __init__(self, wordfile: str):
        """Construct a new graph based on the specified file listing words"""
        raise NotImplementedError


class LazyGraph(UndirectedGraph):
    """
    Class to represent a graph over words in a language.
    Words are vertices.
    Edges connect words of the same length that are identical except at one
    letter.
    Adjacency is determined on demand and not stored.
    """

    def __init__(self, wordfile: str):
        """Construct a new graph based on the specified file listing words"""
        raise NotImplementedError


def variations(graph: UndirectedGraph, start: str, distance: int,
               same_spot: bool = True) -> set[str]:
    """Determine the set of words in a graph the given distance away from the
       given starting vertex.
       If same_spot is True, the same index can be changed multiple times"""
    raise NotImplementedError


def shortest_word_path(
    graph: UndirectedGraph, start: str, dest: str
) -> Optional[list[str]]:
    """Determine the shortest path between words in a graph, if a path exists.
       If there is more than one shortest path, one is chosen arbitrarily.
       If no paths exist, none is returned."""
    raise NotImplementedError
