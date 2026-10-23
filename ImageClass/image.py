from turtle import back

import numpy as np
from PIL import Image as PILImage


class Image:
    def __init__(self, width: int, height: int, background_colour: tuple):
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
        return self._pixels.shape[1]

    @property
    def height(self):
        return self._pixels.shape[0]

    def save(self, file_name: str):
        PILImage.fromarray(self._pixels).save(file_name)

    def set_pixel(self, x: int, y: int, colour: tuple):
        self._pixels[y, x] = np.array((colour[0], colour[1], colour[2]), dtype=np.uint8)

    def get_pixel(self, x: int, y: int) -> tuple:
        pixel = self._pixels[y, x]
        return tuple(pixel[:])


if __name__ == "__main__":
    import random

    WIDTH = 500
    HEIGHT = 500
    img = Image(WIDTH, HEIGHT, (255, 255, 255))

    for _ in range(2000000):
        x = random.randint(0, WIDTH - 1)
        y = random.randint(0, HEIGHT - 1)
        colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        img.set_pixel(x, y, colour)

    img.save("random.png")
