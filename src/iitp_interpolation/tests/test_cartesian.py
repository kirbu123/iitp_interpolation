import numpy as np
import pytest

from iitp_interpolation.techniques.cartesiangrid import (
    CartesianGrid,  # Replace with actual import
)


@pytest.fixture
def sample_2d_data():
    """2D test data with known values"""
    x = np.linspace(0, 10, 11)
    y = np.linspace(0, 5, 6)
    xx, yy = np.meshgrid(x, y)
    return xx + yy  # Simple linear function for testing


@pytest.fixture
def sample_3d_data():
    """3D test data with known values"""
    x = np.linspace(0, 2, 3)
    y = np.linspace(0, 2, 3)
    z = np.linspace(0, 2, 3)
    xx, yy, zz = np.meshgrid(x, y, z, indexing="ij")
    return xx + yy + zz  # Simple linear function


def test_multiple_points_interpolation(sample_2d_data):
    """Test interpolation at multiple points simultaneously"""
    grid = CartesianGrid(limits=[(0, 10), (0, 5)], values=sample_2d_data)

    # Array of points
    points = np.array([[0, 0], [5, 2.5], [10, 5], [2.5, 1.25]])

    results = grid(*points.T)
    expected = np.array([0, 7.5, 15, 3.75])
    np.testing.assert_allclose(results, expected, rtol=1e-6)
