import numpy as np
from scipy import ndimage

from ..metrics.runtime_count import runtime_count


@runtime_count
def bicubic_interpolation(
        image: np.ndarray, scale_factor: float
) -> np.ndarray:

    """
    Bicubic interpolation implementation for RGB images.

    This module provides a function to perform bicubic interpolation on RGB images
    using scipy's ndimage.zoom function. The interpolation is applied uniformly
    across all color channels to resize the image by a given scale factor.

    The main function bicubic_interpolation() handles:
    - Input validation for RGB images and positive scale factors
    - Calculation of new dimensions
    - Application of bicubic interpolation (order=3)
    - Proper type preservation of the output image

    Example usage:
        >>> from bicubic_interpolation import bicubic_interpolation
        >>> import numpy as np
        >>> img = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
        >>> scaled_img = bicubic_interpolation(img, 1.5)
    """

    if len(image.shape) != 3 or image.shape[2] != 3:
        raise ValueError(
            "Input image must have 3 channels (H, W, 3)"
        )

    if scale_factor <= 0:
        raise ValueError("Scale factor must be positive")

    # Calculate new dimensions using scipy.ndimage.zoom method
    zoom_factors = (scale_factor, scale_factor, 1)

    # Perform bicubic interpolation for all channels at once
    output = ndimage.zoom(
        image,
        zoom_factors,
        order=3,  # bicubic interpolation
        mode='reflect'  # or 'mirror', 'constant', 'nearest'
    )

    return output.astype(image.dtype)


__doc__ = bicubic_interpolation.__doc__
