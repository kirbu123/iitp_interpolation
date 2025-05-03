import logging

from .techniques.bicubic import bicubic_interpolation
from .techniques.bilinear import bilinear_interpolation
from .techniques.cartesiangrid import CartesianGrid
from .techniques.nearest_neoghbour import nearest_neighbor_interpolation
from .utils.image import show_image, show_images_original_size
from .utils.parser import Parser

# Create a logger for your module
# Initialize logging (do this ONCE at startup)
logging.basicConfig(
    level=logging.INFO,  # Set minimum log level
    format='%(levelname)s - %(message)s'  # Simple format
)

logger = logging.getLogger(__name__)

def module_cartesiangrid():

    logger.info("cartesian module running...")

    # parse data
    parser = Parser(
        describition="Process images with CartesianGrid interpolation.",
        module_name="cartesiangrid",
    )
    parser.make_parse()
    params = parser.get_params()

    image, limits, points = params["image"], params["limits"], params["points"]

    # show base image
    show_image(image)
    # does linear interpolation
    grid = CartesianGrid(limits, image)

    # interpolate for given points
    logger.info(f"interpolate for given points: {grid(points[0], points[1], points[2])}")


def nearest_neighbour():
    logger.info("nearest neighbour module running...")

    # parse data
    parser = Parser(
        describition="Process images with nearest neighbour interpolation.",
        module_name="nearest_neighbour",
    )
    parser.make_parse()
    params = parser.get_params()

    image = params["image"]

    scale_factor = 2.5
    scaled_img = nearest_neighbor_interpolation(image, scale_factor)

    logger.info(f'Original shape: {image.shape}')
    logger.info(f'Scaled shape: {scaled_img.shape}')

    show_images_original_size(
        image,
        "Original Image",
        scaled_img,
        f"Nearest-Neighbor interpolation (Scale: {scale_factor})",
    )


def bilinear():
    logger.info("bilinear neighbour module running...")

    # parse data
    parser = Parser(
        describition="Process images with bilinear interpolation.",
        module_name="bilinear",
    )
    parser.make_parse()
    params = parser.get_params()

    image = params["image"]

    scale_factor = 2.5
    scaled_img = bilinear_interpolation(image, scale_factor)

    logger.info(f'Original shape: {image.shape}')
    logger.info(f'Scaled shape: {scaled_img.shape}')

    show_images_original_size(
        image,
        "Original Image",
        scaled_img,
        f"bilinear Image (Scale: {scale_factor})",
    )


def bicubic():
    logger.info("bicubic neighbour module running...")

    # parse data
    parser = Parser(
        describition="Process images with bicubic interpolation.",
        module_name="bicubic",
    )
    parser.make_parse()
    params = parser.get_params()

    image = params["image"]

    scale_factor = 2.5
    scaled_img = bicubic_interpolation(image, scale_factor)

    logger.info(f'Original shape: {image.shape}')
    logger.info(f'Scaled shape: {scaled_img.shape}')

    show_images_original_size(
        image,
        "Original Image",
        scaled_img,
        f"bicubic Image (Scale: {scale_factor})",
    )

if __name__ == "__main__":
    logger.info("main script started as module")
