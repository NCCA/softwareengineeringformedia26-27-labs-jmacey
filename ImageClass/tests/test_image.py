import pytest

from image import Image


# create image with w / h
# image w/h can't be changed
def test_image_construct():
    WIDTH = 200
    HEIGHT = 300
    img = Image(WIDTH, HEIGHT)
    assert img.width == WIDTH
    assert img.height == HEIGHT

    with pytest.raises(AttributeError):
        img.width = 10

    with pytest.raises(AttributeError):
        img.height = 10

    assert img.pixels.shape[0] == HEIGHT
    assert img.pixels.shape[1] == WIDTH
    assert img.pixels.shape[2] == 3
