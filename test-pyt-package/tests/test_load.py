from ahoi.ship import *
import numpy

def test_load_data(norkyst):
    print(norkyst)

def test_field():
    f = Field(np.linspace(0, 100), np.linspace(0, 100))
    assert f.xx.shape == (50, 50)

def test_field_plot(plot):
    f = Field(np.linspace(0, 100), np.linspace(0, 100))
    A = np.ones([100,100])
    if plot:
        import matplotlib.pyplot as plt
        plt.imshow(A)
        plt.show()
