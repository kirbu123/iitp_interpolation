import numpy as np
import scipy.ndimage


class CartesianGrid(object):

    """
    Multidimensional Cartesian grid interpolation with regular spacing.

    This module provides a class for performing linear interpolation on regularly
    spaced Cartesian grids in arbitrary dimensions. The implementation uses
    scipy.ndimage.map_coordinates for efficient interpolation calculations.

    The CartesianGrid class features:
    - Support for N-dimensional data interpolation
    - Regular grid spacing with customizable bounds
    - Linear interpolation (order=1) with NaN handling for out-of-bounds values
    - Clean interface for evaluating the interpolated function at arbitrary points

    Example usage:
        >>> import numpy as np
        >>> from cartesian_grid import CartesianGrid
        >>> # Create 2D grid
        >>> x_limits = (0, 10)
        >>> y_limits = (0, 5)
        >>> values = np.random.rand(100, 50)  # 100x50 grid
        >>> grid = CartesianGrid((x_limits, y_limits), values)
        >>> # Interpolate at a point
        >>> result = grid(3.2, 1.5)
        >>> # Vectorized evaluation
        >>> points = np.array([[3.2, 1.5], [5.1, 2.3]])
        >>> results = [grid(*point) for point in points]

    Note:
        For irregular grids or higher-order interpolation, consider using
        scipy.interpolate.RectBivariateSpline (2D) or
        scipy.interpolate.RegularGridInterpolator (N-D).
    """

    def __init__(self, limits, values):
        self.values = values
        self.limits = limits

    def __call__(self, *coords):
        # transform coords into pixel values
        coords = np.asarray(coords)
        coords = [
            (c - lo) * (n - 1) / (hi - lo)
            for (lo, hi), c, n in
            zip(self.limits, coords, self.values.shape, strict=False)
        ]

        return scipy.ndimage.map_coordinates(
            self.values, coords, cval=np.nan, order=1
        )


__doc__ = CartesianGrid.__doc__
