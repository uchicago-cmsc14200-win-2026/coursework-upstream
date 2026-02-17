import sys
import pygame

WINDOW_WIDTH  = 800
WINDOW_HEIGHT = 400 

class Walker:

    width    : int
    height   : int
    surface  : pygame.Surface
    clock    : pygame.time.Clock
    sprite   : pygame.Surface
    sprite_x : int
    sprite_y : int
    speed    : int
    frame    : int
    
    def __init__(self):
        self.width  = WINDOW_WIDTH
        self.height = WINDOW_HEIGHT
 
    def run_app(self) -> None:
        pygame.init()
        pygame.display.set_caption("Walker")
        self.surface = pygame.display.set_mode((self.width,self.height))

        # images are loaded at this moment
        # image loading can only be done after init() and set_mode()
        self.desert = pygame.image.load('assets/images/desert.bmp').convert_alpha()
        self.idle = pygame.image.load("assets/images/idle.bmp").convert_alpha()
        self.walk_frames = [
            pygame.image.load("assets/images/walk0.bmp").convert_alpha(),
            pygame.image.load("assets/images/walk1.bmp").convert_alpha(),
            pygame.image.load("assets/images/walk2.bmp").convert_alpha(),
            pygame.image.load("assets/images/walk3.bmp").convert_alpha(),
            pygame.image.load("assets/images/walk4.bmp").convert_alpha(),
            pygame.image.load("assets/images/walk5.bmp").convert_alpha(),
            pygame.image.load("assets/images/walk6.bmp").convert_alpha(),
            pygame.image.load("assets/images/walk7.bmp").convert_alpha(),
        ]

        self.clock = pygame.time.Clock()
        self.sprite = self.idle
        self.sprite_x = WINDOW_WIDTH//2
        self.sprite_y = WINDOW_HEIGHT//2
        self.speed = 6
        self.frame = 0
        self.run_event_loop()

    def quit_app(self) -> None:
        pygame.quit()
        sys.exit()

    def draw_window(self) -> None:
        self.surface.blit(self.desert,(0,0))
        self.surface.blit(self.sprite, (self.sprite_x, self.sprite_y))
        pygame.display.update()

    def run_event_loop(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_app()

            keys = pygame.key.get_pressed()

            # --- (BEGIN) complete this part of the event loop

            # if q is pressed, quit

            # if shift+right is pressed, move right at double speed
            # - update character image to next `walk_frame`
            # - wrap around if character goes off the screen to the right

            # if shift+left is pressed, move left at double speed
            # - update character image to next `walk_frame`
            # - wrap around if character goes off the screen to the left
            
            # if right is pressed, move right at speed
            # - update character image to next `walk_frame`
            # - wrap around if character goes off the screen to the right

            # if left is pressed, move left at double speed
            # - update character image to next `walk_frame`
            # - wrap around if character goes off the screen to the left

            # if no keys are pressed, the character should appear as `idle`

            # suggestion: you can flip the character images
            # horizontally to make her actually walk left instead of
            # "walking right backwards" -- to do so, look into
            # pygame.transform.flip

            # --- (END) complete this part of the event loop

            self.draw_window()
            self.clock.tick(24)

# ============

if __name__ == "__main__":
    w = Walker()
    w.run_app()

