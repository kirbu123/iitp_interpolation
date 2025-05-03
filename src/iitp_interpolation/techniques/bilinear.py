import numpy as np


def bilinear_interpolation(image, scale_factor):
    if len(image.shape) != 3:
        raise ValueError("Input must be 2D (grayscale) or 3D (color) array")
    
    h, w = image.shape[:2]
    new_h = int(np.round(h * scale_factor))
    new_w = int(np.round(w * scale_factor))
    
    # Create grid of new coordinates
    x_new = np.linspace(0, w-1, new_w)
    y_new = np.linspace(0, h-1, new_h)
    
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
    output = (
        (1 - wy) * (1 - wx) * Ia +
        (1 - wy) * wx * Ic +
        wy * (1 - wx) * Ib +
        wy * wx * Id
    )
    
    return output.astype(image.dtype)


__doc__ = bilinear_interpolation.__doc__
