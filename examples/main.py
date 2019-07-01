import pygame, os, sys
sys.path.append(os.getcwd())
from typing import List, Tuple
from gui_manager import GUIManager
from factory import *

# try later: 640×480, 800×600, 960×720, 1024×768, 1280×960
SCREENWIDTH, SCREENHEIGHT = 800, 600

def init_pygame():
  pygame.init()
  pygame.display.set_caption("pygGUI-example")
  pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

def setup():
  global PYGGUI, SCREEN, FONT, CLOCK
  PYGGUI = GUIManager()
  FONT = pygame.font.SysFont("comicsansms", 24)
  SCREEN = pygame.display.get_surface()
  CLOCK = pygame.time.Clock()
  #STATE.FOOD_TEXTURE = pgh.load_image("food.png")

def handle_events():
  global PYGGUI
  state = "run"
  events = pygame.event.get()
  for event in events:
    if event.type == pygame.QUIT:
      state = "exit"
    if event.type == pygame.MOUSEBUTTONUP:
      x, y = event.pos
      selection = None #any_collide_with_point(STATE.critters, x, y)
      if (selection is not None):
        True
  PYGGUI.update(events)
  return state

def render_ui():
  """
  Renders some basic state information to the screen.
  Also blits pygGUI managed objects.
  """
  global PYGGUI, CLOCK, SCREEN, FONT
  ui_info = f"{round(CLOCK.get_fps())}fps"
  ui_font = FONT.render(ui_info, True, (0, 0, 0))
  example_toggle = "Toggle"
  toggle_font = FONT.render(example_toggle, True, (0, 0, 0))
  SCREEN.blit(ui_font, (0, 0))
  SCREEN.blit(toggle_font, (18, 16))
  #blit pygGUI
  PYGGUI.draw(SCREEN)

def any_collide_with_point(group, x, y):
  for obj in group:
    if obj.rect.collidepoint(x, y):
      return obj
  else:
    return None

if __name__ == "__main__":
  init_pygame()
  setup()
  print("finished loading")
  state = "run"
  (_, cbox) = create_ui("checkbox", manager=PYGGUI, y=16)
  while ("exit" != state):
    CLOCK.tick(60)
    state = handle_events()
    SCREEN.fill((255, 255, 255))
    render_ui()
    pygame.display.flip()
  print("exiting")
