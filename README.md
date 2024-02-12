# Python Pygame Loader

[![CI](https://github.com/kerodekroma/python-pygame-loader/actions/workflows/build_pygame.yml/badge.svg)](https://github.com/kerodekroma/python-pygame-loader/actions/workflows/build_pygame.yml/badge.svg)

This is the demo of the loader of python and pygame. LIVE DEMO LINK: https://kerodekroma.itch.io/python-pygame-loader

## Install Dependencies

```bash
pip install pygame pygbag
```

## Run the demo

Once you download this repo and their dependencies are available, run this command

```bash
python main.py
```

## Usage

These steps are part of a single intro of how to add in your code, you can find further details in the `main.py` file:

```py
from atlas_spritesheet import AtlasSpritesheet
```

Then you can just declare the proper class with the asset when your game starts

```py
    file_path = 'assets/python-pygame-loader/python-pygame-loader'
    '''
    this constructor method needs 3 params:
    - the .png file where is located the spritesheet of the animation
    - the .json file where is located the metadata of the spritesheet
    - the scale of the sprite, you can reduce/enlarge the sprite
    '''
    loader_spritesheet = AtlasSpritesheet(f'{file_path}.png', f'{file_path}.json', 4)
    '''
    the `setup` method needs 3 params:
    - the coords to show the animation
    - the frame rate of it, or how many FPS must run the animation itself
    - If the animation must be repeated or not
    '''
    self.loader_spritesheet.setup((0, 0), 20, True)
```

Finally, you can play the animation it into the game loop:

```py
    loader_spritesheet.play(my_main_creen)
```
