from turtle import back

import numpy as np


class Image:
    def __init__(self, width: int, height: int, background_colour: tuple):
        self._width = width
        self._height = height
        self._pixels = np.empty((height, width, 3), dtype=np.uint8)
        self.clear(background_colour)

    def clear(self, colour: tuple):
        self._pixels[:] = np.array((colour[0], colour[1], colour[2]), dtype=np.uint8)

    @property
    def pixels(self):
        view = self._pixels.view()
        view.flags.writeable = False
        return view

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height
