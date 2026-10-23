import pytest

from image import Image


# create image with w / h
# image w/h can't be changed
def test_image_construct():
    img = Image(20, 30)
    assert img.width == 20
    assert img.height == 30

    with pytest.raises(AttributeError):
        img.width = 10

    with pytest.raises(AttributeError):
        img.height = 10
