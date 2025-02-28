import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def show_image(img: np.ndarray):
    # Display the image
    plt.figure(figsize=(8, 8))
    plt.imshow(img)
    plt.axis("off")  # Hide the axes
    plt.tight_layout()
    plt.show()


def path_to_image(image_path: str) -> np.ndarray:
    img = np.array(Image.open(image_path))
    return img