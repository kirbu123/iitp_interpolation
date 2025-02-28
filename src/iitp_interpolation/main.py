import numpy as np
from .techniques.cartesiangrid import CartesianGrid
from .techniques.interpn import interpn, npinterpn
from .techniques.regulargrid import RegularGrid
from .utils.image import show_image, path_to_image
from .utils.parser import Parser


def cartesiangrid():

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


def interpn():
    print("interp module running...")


def regulargrid():
    print("regulargrid module running...")
