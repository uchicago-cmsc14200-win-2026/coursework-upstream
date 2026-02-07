"""
CMSC 14200, Winter 2026
Homework 5

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

import pygame
import sys
import os
from barchart import BarChart

class GraphicalBarChart(BarChart):

    def __init__(self, surface: pygame.Surface, x: int, y: int, width: int, 
                 height: int, data: list):
        super().__init__(data)

        self.surface = surface
        self.rect = pygame.Rect(x, y, width, height)

        self.current_data = list(data) # make a copy
        self.target_data = list(data) # make a copy

        self.animation_speed = 0.1


    def draw(self) -> None:
        """
        Draw a bar chart representing data from a single olympic
        year. You will need to:
        
            - draw a bar for each quantity of decorated athletes
            - determine a layout for the bars in the chart
            - label the bars in the chart using the provided flag images

        """
        raise NotImplementedError('GraphicalBarChart.draw')

        # Draw chart border
        # pygame.draw.rect(self.surface, (200, 200, 200), self.rect, 2)
