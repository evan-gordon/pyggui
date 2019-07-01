import random, sys
from pygame import Rect
from checkbox import Checkbox

def create_ui(type, *args, **kwargs):
  """
  Main function for creating a UI element with pyggui.
  currently type must be `checkbox`.
  
  see correct lambda func for kwargs needed.
  """
  factory_func = get_object_factory(type)
  return factory_func(**kwargs)

def get_object_factory(type):
  if (type == "checkbox"):
    return create_checkbox_lambda
  else:
    print(f"Error: no gui of type {type}")
    return default_ui_lambda

def create_checkbox_lambda(
    *, manager=None, register=True, id=None, x=0, y=0
):
  """
  Create the checkbox at given x, y.
  If register then register to manager with
  either passed id or generated.
  """
  if (id is None):
    id = "checkbox_" + str(random.randint(0, sys.maxsize))
  checkbox = Checkbox(
      manager.get_image_info(),
      enabled_rect=Rect(16, 0, 16, 16),
      disabled_rect=Rect(0, 0, 16, 16),
      x=x,
      y=y
  )
  if (manager is not None and register):
    manager.register_widget(id, checkbox)
  return (id, checkbox)

def default_ui_lambda(*args, **kwargs):
  None
