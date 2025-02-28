<div align="center">
  <h1>This is the main interpolation techniques implementation directory</h1>
</div>

<div align="center">
  <h1 style="color: gold;">Description</h1>
</div>

1) ### ```cartesiangrid.py ```


    ### This code implements a linear multivariate Cartesian grid interpolation system that works in arbitrary dimensions. It transforms input coordinates from their original range (defined by limits) into normalized pixel coordinates, then uses SciPy's map_coordinates function to perform linear interpolation on a regular grid with equal spacing. The implementation allows for efficient interpolation of values at arbitrary points within an n-dimensional space by mapping between the real-world coordinate system and the discrete grid of stored values.

2) ### ``` interpn.py```

    ### This code implements two N-dimensional interpolation functions for multivariate data. The `interpn` function uses SciPy's `interp1d` to perform sequential interpolation along each dimension of a rectangular grid, while the `npinterpn` function uses NumPy's `interp` for the same purpose. Both functions take coordinate arrays that define a rectangular grid, values at those grid points, and the coordinates at which to interpolate, then recursively apply interpolation along each dimension with a specified method (defaulting to cubic interpolation). This approach allows for interpolating values at arbitrary points within an N-dimensional space defined by regularly spaced grid points.

3) ### ``` regulargrid.py```

    ### This code implements a Linear Multivariate Regular Grid interpolation system for arbitrary dimensions. The `RegularGrid` class works with grid points defined by limits and breaks (interior grid points), and performs linear interpolation using weighted combinations of surrounding grid values. When interpolating at a specific coordinate, the algorithm first locates the relevant grid cell containing the point, calculates normalized distances within that cell, and then computes a weighted sum of all surrounding grid values to determine the interpolated result. The implementation efficiently handles N-dimensional data through a systematic approach of identifying the relevant grid points and applying appropriate distance-based weights.