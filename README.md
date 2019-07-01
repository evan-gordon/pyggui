# pygGUI

A simple gui for use with pygame.

The idea behind this project was really just to make a gui library that did the bare minimum for me. A lot of other libraries will try to do it all for you, but that really wasn't what I needed, so here are a few goals I want to achieve with pygGUI.

* Optionally have pygGUI group manage all objects
* Allow for users to load in their own image files but provide defaults
* If pygGUI is managing your UI object, allow easy named lookup

## Planned features

* delete from manager
* button widget
* slider bar
* parent window that can be moved

## Environment

Written in python `3.7`

Make sure you have `pipenv` installed.

To enable, run:

```bash
pipenv shell
```

## Up and Running

main n:

```bash
python main.py
```

run tests:

```bash
pytest -q

# with code coverage
pytest --cov tests/

# generate coverage report
pytest --cov --cov-report html tests/
```
