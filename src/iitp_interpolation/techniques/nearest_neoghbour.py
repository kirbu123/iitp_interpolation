import numpy as np


def nearest_neighbor_interpolation(input_img, scale_factor) -> np.ndarray:

    """
    Nearest neighbor interpolation for grayscale and color images.

    This module provides efficient nearest neighbor interpolation implementation
    that preserves original pixel values without blending. Suitable for both
    grayscale (2D) and color (3D) images, with proper edge handling and
    dimension validation.

    Key features:
    - Strict input validation for scale factor and image content
    - Automatic handling of single-channel and multi-channel images
    - Precise coordinate mapping with proper edge alignment
    - Index clipping to prevent out-of-bounds access
    - Preservation of original pixel values (no smoothing/blurring)

    Example usage:
        >>> import numpy as np
        >>> from nearest_neighbor_interpolation import nearest_neighbor_interpolation
        >>> # For a color image (RGB)
        >>> img_rgb = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
        >>> scaled_rgb = nearest_neighbor_interpolation(img_rgb, 2.0)
        >>> # For a grayscale image
        >>> img_gray = np.random.randint(0, 256, (100, 100), dtype=np.uint8)
        >>> scaled_gray = nearest_neighbor_interpolation(img_gray, 0.5)

    Note:
        This method is computationally efficient but may produce blocky results
        when upscaling. For smoother results, consider bilinear or bicubic
        interpolation methods.
    """

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
