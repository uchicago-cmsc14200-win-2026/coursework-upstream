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
import sys
import pygame
import pygame.gfxdraw

from weightedgraph import Vertex, Edge, WeightedGraph, Metric
from dijkstra import dijkstra

BACKGROUND = (128, 128, 128)
VERTEX_RADIUS = 8
VERTEX_FILL = (255, 255, 255)
VERTEX_SELECTED = (255, 255, 0)
VERTEX_BORDER = (0, 0, 0)
EDGE_COLOR = (0, 0, 0)
PATH_EDGE_COLOR = (0, 0, 255)

WIDTH = 1000
HEIGHT = 500
BORDER = 60
SCALE = 1


class DrawGraph:

    surface: pygame.surface.Surface
    clock: pygame.time.Clock

    def __init__(self) -> None:
        # Initialize Pygame
        pygame.init()
        pygame.display.set_caption("DrawGraph")
        self.surface = pygame.display.set_mode((WIDTH + 2*BORDER,
                                               HEIGHT + 2*BORDER))
        self.clock = pygame.time.Clock()

        self.event_loop()

    def draw_window(self) -> None:
        self.surface.fill(BACKGROUND)

    def event_loop(self) -> None:
        while True:
            # Process Pygame events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    pass
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass

            # Update the display
            self.draw_window()
            pygame.display.update()
            self.clock.tick(24)


if __name__ == "__main__":
    DrawGraph()
