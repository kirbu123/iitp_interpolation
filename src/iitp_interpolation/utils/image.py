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
    """Display two images side by side with titles.

    Args:
        img_left: Left image array
        title_left: Title for left image
        img_right: Right image array
        title_right: Title for right image
    """
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


def show_images_original_size(
        img_left: np.ndarray,
        title_left: str,
        img_right: np.ndarray,
        title_right: str
):
    # Create figure with flexible layout
    fig = plt.figure(figsize=(10, 8), constrained_layout=True)

    # Create a grid:
    # 1 row, 2 columns with width ratios proportional to image widths
    gs = fig.add_gridspec(
        1, 2, width_ratios=[img_left.shape[1], img_right.shape[1]]
    )

    # Plot each image in its original aspect ratio
    ax1 = fig.add_subplot(gs[0])
    ax1.imshow(img_left)
    ax1.set_title(title_left)
    ax1.axis('off')

    ax2 = fig.add_subplot(gs[1])
    ax2.imshow(img_right)
    ax2.set_title(title_right)
    ax2.axis('off')

    plt.show()


def path_to_image(image_path: str) -> np.ndarray:
    img = np.array(Image.open(image_path))
    return img
