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
from typing import List
import heapq
from weightedgraph import Vertex, Edge, WeightedGraph, Metric

def dijkstra(graph: WeightedGraph,
             src: Vertex, dst: Vertex, m: Metric) -> List[Edge]:
    """Find the best path in graph 'graph' between src and dst.
       Use metric m as the quantity to minimize.
       Return empty list if no path exists."""
    raise NotImplementedError
