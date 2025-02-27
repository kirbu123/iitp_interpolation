import numpy
import scipy.ndimage

class CartesianGrid(object):
	"""
	Linear Multivariate Cartesian Grid interpolation in arbitrary dimensions
	This is a regular grid with equal spacing.
	"""
	def __init__(self, limits, values):
		self.values = values
		self.limits = limits
	
	def __call__(self, *coords):
		# transform coords into pixel values
		coords = numpy.asarray(coords)
		coords = [(c - lo) * (n - 1) / (hi - lo) for (lo, hi), c, n in zip(self.limits, coords, self.values.shape)]
		
		return scipy.ndimage.map_coordinates(self.values, coords, 
			cval=numpy.nan, order=1)

__doc__ = CartesianGrid.__doc__

def main():
	limits = [(0, 1), (0, 1), (0, 1)]
	x = numpy.linspace(0, 1, 8)
	y = numpy.linspace(0, 1, 9)
	z = numpy.linspace(0, 1, 10)

	Z, Y = numpy.meshgrid(z, y)
	X = numpy.array([[x]]).transpose()

	# our grid values
	values = X**2 + Y - Z

	# does linear interpolation
	grid = CartesianGrid(limits, values)

	# interpolate for one point
	print(grid([0.1], [0.5], [0.3]))
	# interpolate many
	print(grid([0.1, 0.3], [0.5, 0.5], [0.3, 0.2]))
