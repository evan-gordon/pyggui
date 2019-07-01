import pygame, os, sys

#
#
#
class GUIManager():
  """
  The purpose of this class is to be able to:
  * register a widget
  * receive updates from pygame
  * query state of widget by name
  * draw to screen
  """
  _widget = {}
  _widget_rects = {}
  _default_image_info = None

  def __init__(self, font="comicsansms", font_size=24, load_defaults=True):
    self.font = pygame.font.SysFont(font, font_size)
    self._widgets_group = pygame.sprite.Group()

    if (load_defaults):
      self._default_image_info = load_image("uielements.png")
      # might not need the following
      self._widget_rects["checkbox"] = {
          "enabled": pygame.Rect((32, 0), (32, 32)),
          "disabled": pygame.Rect((0, 0), (32, 32))
      }

  def update(self, events):
    """
    Update all widgets managed by manager.
    Designed to only update one widget per update call.
    """
    for event in events:
      if (event.type == pygame.MOUSEBUTTONUP):
        x, y = event.pos
        selection = any_collide_with_point(self._widgets_group, x, y)
        if (selection is not None):
          selection.update(click=True)
          break
    else:
      # update hovered state
      pass

  def draw(self, screen):
    self._widgets_group.draw(screen)

  def register_widget(self, key: str, element):
    self._widget[key] = element
    self._widgets_group.add(element)

  def get_widget(self, key: str):
    return self._widget[key]

  def get_widget_rects(self, key: str):
    return _widget_rects[key]

  def get_image_info(self):
    """
    If load_defaults=True 
    pyggui will load some default images for the guis.
    Otherwise that will need to be specified manually.
    Returns (image, rect) tuple.
    """
    return self._default_image_info

def load_image(name, colorkey=None, filepath=None):
  try:
    if (filepath is None):
      pyggui_dir = os.path.dirname(os.path.abspath(__file__))
      filepath = os.path.join(pyggui_dir, 'images', name)
    image = pygame.image.load(filepath).convert()
  except:
    print('Cannot load image:', filepath)
    sys.exit(-1)
  image = image.convert()
  if colorkey is not None:
    if colorkey is -1:
      colorkey = image.get_at((0, 0))
    image.set_colorkey(colorkey, RLEACCEL)
  return image, image.get_rect()

def any_collide_with_point(group, x: int, y: int):
  """
  given a (x,y) point determine if any
  object in the given group collides with
  that point.
  """
  for obj in group:
    if obj.rect.collidepoint(x, y):
      return obj
  else:
    return None
