"""
CMSC 14200, Winter 2026
Homework #4

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""
import csv
from typing import Set
from enum import Enum


Metric = Enum("Metric", ["Distance", "Time", "Toll", "Ugly"])


class Vertex:
    """Class to represent a vertex in a graph.
       Vertices have names and two-dimensional Cartesian coordinates."""

    name: str
    x: int
    y: int
    edges: Set["Edge"]

    def __init__(self, name: str, x: int, y: int):
        """Constructor; starts with empty edges set"""
        self.name = name
        self.x = x
        self.y = y
        self.edges = set()


class Edge:
    """Class to represent an edge in an undirected graph.
       'a' and 'b' (the connected vertices) are in no particular order.
       Edges store speed, toll, and ugliness.
       Distance is calculated using Euclidean distance.
       Travel time is calculated using distance and speed.
       Toll and ugliness are directly available."""

    a: Vertex
    b: Vertex
    # distance implicit
    speed: int
    # time implicit
    toll: int
    ugly: int

    def __init__(self, a: Vertex, b: Vertex, speed: int, toll: int, ugly: int):
        """Constructor"""
        self.a = a
        self.b = b
        self.speed = speed
        self.toll = toll
        self.ugly = ugly

    def weight(self, metric: Metric) -> float:
        """Return the edge weight according to the desired metric"""
        raise NotImplementedError


class WeightedGraph:
    """Class to represent an undirected, weighted graph"""

    # maps from vertex name to vertex object
    vertices: dict[str, Vertex]

    def __init__(self, cityfile: str, roadfile: str):
        """Constructor.
           Initialize graph based on two CSV files.
           City file contains lines in the format:
               Name,x,y
           Road file contains lines in the format:
               City A,City B,Speed,Toll,Ugliness
        """
        raise NotImplementedError
