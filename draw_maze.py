import pyxel

BLACK = 0
WHITE = 7

def display(color, pixels=None):
    if pixels is None:
        pyxel.cls(color)
    elif len(pixels) >= 1 and type(pixels[0]) == int:
        display(color, [pixels])
    else:
        for x, y in pixels:
            pyxel.pset(x, y, color)

def draw_maze(maze):
    display(BLACK)
    display(WHITE, maze)
  
