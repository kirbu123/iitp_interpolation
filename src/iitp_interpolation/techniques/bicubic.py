import numpy as np


def cubic(x, a=-0.5):
    x = np.abs(x)
    return ((a + 2) * x**3 - (a + 3) * x**2 + 1) * (x <= 1) + (
        a * x**3 - 5 * a * x**2 + 8 * a * x - 4 * a
    ) * ((x > 1) & (x <= 2))


def bicubic_interpolation(input_img, scale_factor):
    h, w = input_img.shape[:2]
    new_h = int(h * scale_factor)
    new_w = int(w * scale_factor)

    if len(input_img.shape) == 3:
        output_img = np.zeros((new_h, new_w, 3), dtype=input_img.dtype)
        channels = 3
    else:
        output_img = np.zeros((new_h, new_w), dtype=input_img.dtype)
        channels = 1

    x_new = np.linspace(0, w - 1, new_w)
    y_new = np.linspace(0, h - 1, new_h)

    for c in range(channels):
        for i in range(new_h):
            for j in range(new_w):
                x = x_new[j]
                y = y_new[i]

                x_floor = int(np.floor(x))
                y_floor = int(np.floor(y))

                pixels = []
                for m in range(-1, 3):
                    row = []
                    for n in range(-1, 3):
                        xn = min(max(x_floor + n, 0), w - 1)
                        ym = min(max(y_floor + m, 0), h - 1)
                        if channels == 3:
                            row.append(input_img[ym, xn, c])
                        else:
                            row.append(input_img[ym, xn])
                    pixels.append(row)
                pixels = np.array(pixels)

                dx = x - x_floor
                dy = y - y_floor

                horizontal = []
                for k in range(4):
                    dist_x = np.array([1 + dx, dx, 1 - dx, 2 - dx])
                    weights_x = cubic(dist_x)
                    horizontal.append(np.sum(pixels[k] * weights_x))

                dist_y = np.array([1 + dy, dy, 1 - dy, 2 - dy])
                weights_y = cubic(dist_y)
                interpolated = np.sum(np.array(horizontal) * weights_y)

                interpolated = np.clip(interpolated, 0, 255)

                if channels == 3:
                    output_img[i, j, c] = interpolated
                else:
                    output_img[i, j] = interpolated

    return output_img.astype(input_img.dtype)


__doc__ = bicubic_interpolation.__doc__
