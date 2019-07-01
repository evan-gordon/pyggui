import pygame

class Checkbox(pygame.sprite.Sprite):
  """
  UI checkbox class
  It maintain it's own state, and shows image based on state
  can also query state.
  """

  def __init__(
      self,
      image_info,
      *,
      default_state=False,
      enabled_rect=pygame.Rect((0, 0), (0, 0)),
      disabled_rect=pygame.Rect((0, 0), (0, 0)),
      x=0,
      y=0
  ):
    pygame.sprite.Sprite.__init__(self)
    self.enabled = default_state
    img, rect = image_info
    self.texture, self.ori_rect = img.copy(), rect.copy()
    self.texture.set_colorkey((0, 0, 0))
    self.x, self.y = x, y
    self.enabled_rect = enabled_rect.copy()
    self.disabled_rect = disabled_rect.copy()
    self._set_rect()

  def update(self, *, click=False):
    if (click):
      self.enabled = not self.enabled
      self._set_rect()

  def _set_rect(self):
    if (self.enabled):
      self.rect = self.enabled_rect.copy()
    else:
      self.rect = self.disabled_rect.copy()
    self.image = self.texture.copy().subsurface(self.rect)
    self.rect.x, self.rect.y = self.x, self.y

  def move():
    pass
