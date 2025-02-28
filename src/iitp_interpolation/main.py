from .techniques.cartesiangrid import CartesianGrid
from .utils.image import show_image
from .utils.parser import Parser


def module_cartesiangrid():

    print("cartesian module running...")

    # parse data
    parser = Parser(describition='Process images with CartesianGrid interpolation.', module_name='cartesiangrid')
    parser.make_parse()
    params = parser.get_params()

    image, limits, points = params['image'], params['limits'], params['points']

    # show base image
    show_image(image)
    # does linear interpolation
    grid = CartesianGrid(limits, image)

    # interpolate for given points
    print(f'interpolate for given points: {grid(points[0], points[1], points[2])}')


def module_interp():
    print("interp module running...")


def module_regulargrid():
    print("regulargrid module running...")
