import numpy as np


def nearest_neighbor_interpolation(input_img, scale_factor):
    h, w = input_img.shape[:2]

    new_h = int(h * scale_factor)
    new_w = int(w * scale_factor)

    x = np.linspace(0, w - 1, new_w)
    y = np.linspace(0, h - 1, new_h)

    x_idx = np.round(x).astype(int)
    y_idx = np.round(y).astype(int)

    if len(input_img.shape) == 3:
        output_img = input_img[y_idx[:, None], x_idx[None, :], :]
    else:
        output_img = input_img[y_idx[:, None], x_idx[None, :]]

    return output_img


__doc__ = nearest_neighbor_interpolation.__doc__
