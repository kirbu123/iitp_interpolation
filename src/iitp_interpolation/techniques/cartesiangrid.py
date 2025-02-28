import numpy as np
import argparse
import scipy.ndimage
from PIL import Image
import matplotlib.pyplot as plt


class CartesianGrid(object):
    """
    Linear Multivariate Cartesian Grid interpolation in arbitrary dimensions
    This is a regular grid with equal spacing.
    """

    def __init__(self, limits, values):
        self.values = values
        self.limits = limits

    def __call__(self, *coords):
        # transform coords into pixel values
        coords = np.asarray(coords)
        coords = [
            (c - lo) * (n - 1) / (hi - lo)
            for (lo, hi), c, n in zip(self.limits, coords, self.values.shape)
        ]

        return scipy.ndimage.map_coordinates(
            self.values, coords, cval=np.nan, order=1
        )


__doc__ = CartesianGrid.__doc__