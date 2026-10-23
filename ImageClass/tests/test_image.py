from pathlib import Path

import pytest

from image import Image


# create image with w / h
# image w/h can't be changed
def test_image_construct():
    WIDTH = 200
    HEIGHT = 300
    img = Image(WIDTH, HEIGHT, (255, 128, 0))
    assert img.width == WIDTH
    assert img.height == HEIGHT

    with pytest.raises(AttributeError):
        img.width = 10

    with pytest.raises(AttributeError):
        img.height = 10

    assert img.pixels.shape[0] == HEIGHT
    assert img.pixels.shape[1] == WIDTH
    assert img.pixels.shape[2] == 3
    pixel = img.pixels[0, 0]
    assert pixel[0] == 255
    assert pixel[1] == 128
    assert pixel[2] == 0


def test_save_img():
    img = Image(200, 200, (255, 0, 0))
    img.save("test.png")
    assert Path("test.png").exists()
    Path("test.png").unlink()
    img.save("test.jpg")
    assert Path("test.jpg").exists()
    Path("test.jpg").unlink()


def test_pixel_access():
    img = Image(10, 10, (255, 255, 255))
    img.set_pixel(0, 0, (128, 0, 0))
    pixel = img.get_pixel(0, 0)
    assert pixel[0] == 128
    assert pixel[1] == 0
    assert pixel[2] == 0
