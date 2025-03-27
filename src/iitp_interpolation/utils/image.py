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

def show_images(
        img_left: np.ndarray,
        title_left: str,
        img_right: np.ndarray,
        title_right: str
    ):
    # Display the image
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.title(title_left)
    plt.imshow(img_left)
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.title(title_right)
    plt.imshow(img_right)
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()

def path_to_image(image_path: str) -> np.ndarray:
    img = np.array(Image.open(image_path))
    return img