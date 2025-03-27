from .techniques.bicubic import bicubic_interpolation
from .techniques.bilinear import bilinear_interpolation
from .techniques.cartesiangrid import CartesianGrid
from .techniques.nearest_neoghbour import nearest_neighbor_interpolation
from .utils.image import show_image, show_images
from .utils.parser import Parser


def module_cartesiangrid():

    print("cartesian module running...")

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
    print(
        f"interpolate for given points: {grid(points[0], points[1], points[2])}"
    )


def nearest_neighbour():

    print("nearest neighbour module running...")

    # parse data
    parser = Parser(
        describition="Process images with nearest neighbour interpolation.",
        module_name="nearest_neighbour",
    )
    parser.make_parse()
    params = parser.get_params()

    image = params["image"]

    scale_factor = 10
    scaled_img = nearest_neighbor_interpolation(image, scale_factor)

    show_images(
        image,
        "Original Image",
        scaled_img,
        f"Nearest-Neighbor (Scale: {scale_factor})",
    )


def bilinear():
    print("bilinear neighbour module running...")

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

    show_images(
        image,
        "Original Image",
        scaled_img,
        f"bilinear Image (Scale: {scale_factor})",
    )


def bicubic():
    print("bicubic neighbour module running...")

    # parse data
    parser = Parser(
        describition="Process images with bicubic interpolation.",
        module_name="bicubic",
    )
    parser.make_parse()
    params = parser.get_params()

    image = params["image"]

    scale_factor = 1.1
    scaled_img = bicubic_interpolation(image, scale_factor)

    show_images(
        image,
        "Original Image",
        scaled_img,
        f"bicubic Image (Scale: {scale_factor})",
    )
