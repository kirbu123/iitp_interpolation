import numpy as np
from scipy import ndimage


def bicubic_interpolation(image: np.ndarray, scale_factor: float) -> np.ndarray:
    if len(image.shape) != 3 or image.shape[2] != 3:
        raise ValueError("Input image must have 3 channels (H, W, 3)")

    if scale_factor <= 0:
        raise ValueError("Scale factor must be positive")
    
    # Calculate new dimensions using the same method scipy.ndimage.zoom uses
    height, width = image.shape[:2]
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
