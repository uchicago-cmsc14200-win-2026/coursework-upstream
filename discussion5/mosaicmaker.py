import sys
import pygame
import rich

class MosaicMaker:

    width    : int
    height   : int
    surface  : pygame.Surface
    clock    : pygame.time.Clock
    filename : str
    photo    : pygame.Surface
    
    def __init__(self, filename:str):
        self.filename = filename
        
    def run_app(self) -> None:
        pygame.init()
        pygame.display.set_caption("MosaicMaker")
        self.photo   = pygame.image.load(self.filename)
        self.width   = self.photo.get_width()
        self.height  = self.photo.get_height()
        self.surface = pygame.display.set_mode((self.width,self.height))
        self.clock   = pygame.time.Clock()
        self.run_event_loop()

    def quit_app(self) -> None:
        pygame.quit()
        sys.exit()

    def mosaic(self, tile_size:int) -> None:
        raise NotImplementedError('mosaic')
    
    def draw_window(self) -> None:
        self.surface.blit(self.photo,(0,0))
        pygame.display.update()

    def run_event_loop(self) -> None:
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.quit_app()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                      self.quit_app()
                    elif event.key == pygame.K_m:
                      self.mosaic(12)
            self.draw_window()
            self.clock.tick(24) # throttle redraws at 24fps (frames per second)

# ========

if __name__ == "__main__":
    mm = MosaicMaker('images/robin.bmp')
    mm.run_app()
