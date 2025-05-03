import numpy as np


def nearest_neighbor_interpolation(input_img, scale_factor) -> np.ndarray:
    if scale_factor <= 0:
        raise ValueError("Scale factor must be positive")
    
    if input_img.size == 0:
        raise ValueError("Input image cannot be empty")
    
    # Calculate original dimensions
    h, w = input_img.shape[:2]

    # Calculate new dimensions (ensure at least 1 pixel)
    new_h = max(1, int(np.round(h * scale_factor)))
    new_w = max(1, int(np.round(w * scale_factor)))
    
    # Generate coordinate grids with proper edge alignment
    x_new = np.linspace(0, w - 1, new_w, endpoint=True)
    y_new = np.linspace(0, h - 1, new_h, endpoint=True)
    
    # Round to nearest neighbor indices
    x_idx = np.round(x_new).astype(int)
    y_idx = np.round(y_new).astype(int)
    
    # Clip indices to valid range
    x_idx = np.clip(x_idx, 0, w - 1)
    y_idx = np.clip(y_idx, 0, h - 1)
    
    # Perform interpolation
    if len(input_img.shape) == 3:
        output = input_img[y_idx[:, None], x_idx[None, :], :]
    else:
        output = input_img[y_idx[:, None], x_idx[None, :]]

    return output


__doc__ = nearest_neighbor_interpolation.__doc__