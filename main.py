import asyncio
import pygame
import atlas_spritesheet
import sys

WIDTH, HEIGHT = 480, 480

class App:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Demo of PythonPygameLoader")
    #bg gradient
    self.surface_bg = self.bg_gradient((WIDTH, HEIGHT), (85, 37, 125), (40, 18, 60), HEIGHT)
    #font
    self.font = pygame.font.Font('assets/font/PixelSimpel.otf', 32)
    # atlas setup
    file_path = 'assets/python-pygame-loader/python-pygame-loader'
    self.loader_spritesheet = atlas_spritesheet.AtlasSpritesheet(f'{file_path}.png', f'{file_path}.json', 4)
    center_pos = (WIDTH/2 - self.loader_spritesheet.get_width()/2, HEIGHT/2 - self.loader_spritesheet.get_height()/2)
    self.loader_spritesheet.setup(center_pos, 20, True)

  def bg_gradient(self, size, color, lerp_color, length):
      surface = pygame.Surface((1, length))
      _color = pygame.Color(color)
      _lerp_color = pygame.Color(lerp_color)
      for i in range(length):
          c = _color.lerp(_lerp_color, i/length)
          surface.set_at((0, i), c)
      return pygame.transform.scale(surface, size)

  async def render(self):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break

        self.screen.fill((85, 37, 125))
        # gradient bg
        self.screen.blit(self.surface_bg, (0, 0))
        # play loader
        self.loader_spritesheet.play(self.screen)

        #update the display
        pygame.display.flip()
        # clock
        pygame.time.Clock().tick(60)
        await asyncio.sleep(0)
        
asyncio.run(App().render())