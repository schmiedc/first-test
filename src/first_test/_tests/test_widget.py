import numpy as np
from first_test import thresholding


# make_napari_viewer is a pytest fixture that returns a napari viewer object
def test_thresholding():

    input_image = np.random.random((100, 100))

    # this time, our widget will be a MagicFactory or FunctionGui instance
    output = thresholding(input_image, 100.0)

    assert type(output) == tuple, "output should be a tuple"
