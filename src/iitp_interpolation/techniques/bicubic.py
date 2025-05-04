import numpy as np
from scipy import ndimage


def bicubic_interpolation(
        image: np.ndarray, scale_factor: float
) -> np.ndarray:
    """Perform bicubic interpolation on an RGB image.

    Args:
        image: Input image array with shape (H, W, 3)
        scale_factor: Scaling factor for the image

    Returns:
        Interpolated image array
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
