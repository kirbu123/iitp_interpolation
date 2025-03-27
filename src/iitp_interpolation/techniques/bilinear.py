import numpy as np


def bilinear_interpolation(input_img, scale_factor):
    h, w = input_img.shape[:2]

    new_h = int(h * scale_factor)
    new_w = int(w * scale_factor)

    x_new = np.linspace(0, w - 1, new_w)
    y_new = np.linspace(0, h - 1, new_h)

    if len(input_img.shape) == 3:
        output_img = np.zeros((new_h, new_w, 3), dtype=input_img.dtype)
        for c in range(3):
            for i in range(new_h):
                for j in range(new_w):
                    x = x_new[j]
                    y = y_new[i]

                    x1, y1 = int(np.floor(x)), int(np.floor(y))
                    x2, y2 = min(x1 + 1, w - 1), min(y1 + 1, h - 1)

                    dx = x - x1
                    dy = y - y1

                    top = (1 - dx) * input_img[y1, x1, c] + dx * input_img[
                        y1, x2, c
                    ]
                    bottom = (1 - dx) * input_img[y2, x1, c] + dx * input_img[
                        y2, x2, c
                    ]

                    output_img[i, j, c] = (1 - dy) * top + dy * bottom
    else:
        output_img = np.zeros((new_h, new_w), dtype=input_img.dtype)
        for i in range(new_h):
            for j in range(new_w):
                x = x_new[j]
                y = y_new[i]

                x1, y1 = int(np.floor(x)), int(np.floor(y))
                x2, y2 = min(x1 + 1, w - 1), min(y1 + 1, h - 1)

                dx = x - x1
                dy = y - y1

                top = (1 - dx) * input_img[y1, x1] + dx * input_img[y1, x2]
                bottom = (1 - dx) * input_img[y2, x1] + dx * input_img[y2, x2]

                output_img[i, j] = (1 - dy) * top + dy * bottom

    return output_img


__doc__ = bilinear_interpolation.__doc__
