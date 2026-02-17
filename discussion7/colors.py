import sys
import pygame

rgb = tuple[int,int,int]

WINDOW_WIDTH  = 800
WINDOW_HEIGHT = 400 

class Colors:

    width    : int
    height   : int
    surface  : pygame.Surface
    clock    : pygame.time.Clock
    bgcolor  : rgb
    
    def __init__(self):
        self.width  = WINDOW_WIDTH
        self.height = WINDOW_HEIGHT
        self.bgcolor = (100,100,100)
        
    def run_app(self) -> None:
        pygame.init()
        pygame.display.set_caption("Colors")
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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_app()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r] and keys[pygame.K_b]:
                self.bgcolor = (128,0,128)
            elif keys[pygame.K_r]:
                self.bgcolor = (255,0,0)
            elif keys[pygame.K_b]:
                self.bgcolor = (0,0,255)
            elif keys[pygame.K_q]:
                self.quit_app()
            else:
                self.bgcolor = (100,100,100)
            self.draw_window()
            self.clock.tick(24)

# ============

if __name__ == "__main__":
    c = Colors()
    c.run_app()

