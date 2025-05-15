import numpy as np

from ..metrics.runtime_count import runtime_count


@runtime_count
def bilinear_interpolation(image, scale_factor):

    """
    Bilinear interpolation implementation for grayscale and color images.

    This module provides a function to perform bilinear interpolation on images,
    supporting both grayscale (2D) and color (3D) arrays. The implementation
    manually computes the interpolation weights and applies them to neighboring
    pixels to produce a smoothly scaled output image.

    The main function bilinear_interpolation() handles:
    - Input validation for 2D or 3D arrays
    - Dynamic calculation of new dimensions based on scale factor
    - Proper coordinate mapping between original and scaled images
    - Weighted averaging of neighboring pixels
    - Type preservation of the output image

    Example usage:
        >>> from bilinear_interpolation import bilinear_interpolation
        >>> import numpy as np
        >>> # For color image (3 channels)
        >>> img_color = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
        >>> scaled_color = bilinear_interpolation(img_color, 1.5)
        >>> # For grayscale image
        >>> img_gray = np.random.randint(0, 256, (100, 100), dtype=np.uint8)
        >>> scaled_gray = bilinear_interpolation(img_gray, 1.5)
    """

    if len(image.shape) != 3:
        raise ValueError("Input must be 2D (grayscale) or 3D (color) array")

    h, w = image.shape[:2]
    new_h = int(np.round(h * scale_factor))
    new_w = int(np.round(w * scale_factor))

    # Create grid of new coordinates
    x_new = np.linspace(0, w - 1, new_w)
    y_new = np.linspace(0, h - 1, new_h)

    # Get floor and ceiling coordinates
    x0 = np.floor(x_new).astype(int)
    x1 = np.minimum(x0 + 1, w - 1)
    y0 = np.floor(y_new).astype(int)
    y1 = np.minimum(y0 + 1, h - 1)

    # Calculate weights with proper shapes
    wx = (x_new - x0).reshape(1, -1, 1)  # Shape (1, new_w, 1)
    wy = (y_new - y0).reshape(-1, 1, 1)    # Shape (new_h, 1, 1)

    # Get pixel values
    Ia = image[y0][:, x0]  # Shape (new_h, new_w, C)
    Ib = image[y1][:, x0]
    Ic = image[y0][:, x1]
    Id = image[y1][:, x1]

    # Perform interpolation with proper broadcasting
    item1 = (1 - wy) * (1 - wx) * Ia
    item2 = (1 - wy) * wx * Ic
    item3 = wy * (1 - wx) * Ib
    item4 = wy * wx * Id
    output = (
        item1 + item2 + item3 + item4
    )

    return output.astype(image.dtype)


__doc__ = bilinear_interpolation.__doc__
