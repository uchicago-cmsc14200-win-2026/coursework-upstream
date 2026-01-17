"""
CMSC 14200, Winter 2026
Homework 2, Task 5

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

# Note: task5.py starts off as a copy of the Quitter from Discussion 2.
# Modify it to build the app described in the homework description.

import sys
import pygame

DEFAULT_BGCOLOR = (0,0,100)
DEFAULT_WIDTH   = 809
DEFAULT_HEIGHT  = 500

# type synonym for convenience
rgb = tuple[int,int,int]

class Quitter:

    bgcolor : rgb
    width   : int
    height  : int
    surface : pygame.Surface
    clock   : pygame.time.Clock

    def __init__(self,
                 bgcolor : rgb = DEFAULT_BGCOLOR,
                 width   : int = DEFAULT_WIDTH,
                 height  : int = DEFAULT_HEIGHT) -> None:
        self.bgcolor = bgcolor if bgcolor else DEFAULT_BGCOLOR
        self.width   = width if width else DEFAULT_WIDTH
        self.height  = height if height else DEFAULT_HEIGHT

    def run_app(self) -> None:
        pygame.init()
        pygame.display.set_caption("Quitter")
        self.surface = pygame.display.set_mode((self.width,self.height))
        self.clock = pygame.time.Clock()
        self.run_event_loop()

    def quit_app(self) -> None:
        pygame.quit()
        sys.exit()

    def draw_window(self) -> None:
        self.surface.fill(self.bgcolor)
        pygame.display.update()

    def run_event_loop(self) -> None:
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.quit_app()
                elif event.type == pygame.MOUSEMOTION:
                    pass
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pass
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass
                elif event.type == pygame.KEYDOWN:
                    pass
                elif event.type == pygame.KEYUP:
                    pass
            self.draw_window()
            self.clock.tick(24) # throttle redrawing the window at 24fps (24 frames per second)

# ========

if __name__ == "__main__":
    q = Quitter()
    q.run_app()

