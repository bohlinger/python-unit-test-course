import numpy as np


class Field:
    x = None
    y = None
    xx = None
    yy = None

    def __init__(self, x, y):
        self.xx, self.yy = np.meshgrid(x, y)
        self.x = x
        self.y = y

    def grid(self):
        return self.xx, self.yy


def test_docs_Field():
    """
    Plots field for testing doctest-module

    >>> f = Field(np.linspace(0, 100), np.linspace(0, 100))
    >>> assert f.xx.shape == (50, 50)
    """
    return

def test_np_assert():
    A = np.ones([10,10])
    B = A * 0.999
    np.testing.assert_allclose(A,B,rtol=1e-2)

def test_field():
    f = Field(np.linspace(0, 100), np.linspace(0, 100))
    assert f.xx.shape == (50, 50)
