import numpy as np


def nearest_neighbor_interpolation(input_img, scale_factor):
    """
    Perform nearest neighbor interpolation on an input image.
    
    Args:
        input_img: numpy array representing the input image (2D or 3D)
        scale_factor: scaling factor (>0)
        
    Returns:
        Scaled image using nearest neighbor interpolation
    """
    if scale_factor <= 0:
        raise ValueError("Scale factor must be positive")
    
    if input_img.size == 0:
        raise ValueError("Input image cannot be empty")
    
    h, w = input_img.shape[:2]
    
    # Calculate new dimensions (ensure at least 1 pixel)
    new_h = max(1, int(np.round(h * scale_factor)))
    new_w = max(1, int(np.round(w * scale_factor)))
    
    # Generate coordinate grids with proper edge alignment
    x = np.linspace(0, w - 1, new_w, endpoint=True)
    y = np.linspace(0, h - 1, new_h, endpoint=True)
    
    # Round to nearest neighbor indices
    x_idx = np.round(x).astype(int)
    y_idx = np.round(y).astype(int)
    
    # Clip indices to valid range
    x_idx = np.clip(x_idx, 0, w - 1)
    y_idx = np.clip(y_idx, 0, h - 1)
    
    # Perform interpolation
    if len(input_img.shape) == 3:
        output_img = input_img[y_idx[:, None], x_idx[None, :], :]
    else:
        output_img = input_img[y_idx[:, None], x_idx[None, :]]
    
    return output_img


__doc__ = nearest_neighbor_interpolation.__doc__