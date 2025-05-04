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
    """Process images using CartesianGrid interpolation.

    This function:
    1. Parses input arguments for CartesianGrid interpolation
    2. Loads and displays the original image
    3. Performs CartesianGrid interpolation
    4. Logs and returns the interpolation results

    The function uses the Parser class to handle command line arguments
    and configuration for the CartesianGrid interpolation process.
    """
    logger.info("cartesian module running...")

    # parse data
    parser = Parser(
        description="Process images with CartesianGrid interpolation.",
        module_name="cartesiangrid"
    )
    parser.make_parse()
    params = parser.get_params()

    image, limits, points = params["image"], params["limits"], params["points"]

    # show base image
    show_image(image)
    # does linear interpolation
    grid = CartesianGrid(limits, image)

    # interpolate for given points
    grid_result = grid(points[0], points[1], points[2])
    logger.info(f"interpolate for given points: {grid_result}")


def nearest_neighbour():
    """Perform nearest neighbor interpolation on an input image.

    This function:
    1. Parses input arguments for nearest neighbor interpolation
    2. Loads the original image
    3. Applies nearest neighbor interpolation with a scale factor of 2.5
    4. Displays original and scaled images side by side
    5. Logs the dimensions of both images

    Returns:
        None: Results are displayed visually and logged
    """
    logger.info("nearest neighbour module running...")

    # parse data
    parser = Parser(
        description="Process images with nearest neighbour interpolation.",
        module_name="nearest_neighbour"
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
    """Perform bilinear interpolation on an input image.

    This function:
    1. Parses input arguments for bilinear interpolation
    2. Loads the original image
    3. Applies bilinear interpolation with a scale factor of 2.5
    4. Displays original and interpolated images side by side
    5. Logs the dimensions of both images

    The bilinear interpolation provides smoother results than nearest neighbor
    while being computationally less intensive than bicubic interpolation.
    """
    logger.info("bilinear neighbour module running...")

    # parse data
    parser = Parser(
        description="Process images with bilinear interpolation.",
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
    """Perform bicubic interpolation on an input image.

    This function:
    1. Parses input arguments for bicubic interpolation
    2. Loads the original image
    3. Applies bicubic interpolation with a scale factor of 2.5
    4. Displays original and interpolated images side by side
    5. Logs the dimensions of both images

    Bicubic interpolation typically produces the highest quality results among
    the common interpolation methods, at the cost of higher computational
    complexity.
    """
    logger.info("bicubic neighbour module running...")

    # parse data
    parser = Parser(
        description="Process images with bicubic interpolation.",
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
    """Main entry point when script is run directly."""
    logger.info("main script started as module")
