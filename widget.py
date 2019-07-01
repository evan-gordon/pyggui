from pygame import Sprite, Rect

class Widget:

  def __init__(self, texture=None, **kwargs):
    Sprite.__init__(self)
    if (texture is None):
      raise ValueError('Missing kwarg texture=Surface()')
    self.rect = Rect((0, 0), (0, 0))
    self.state = ""