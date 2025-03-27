import pytest
import numpy as np
from iitp_interpolation.techniques.nearest_neoghbour import nearest_neighbor_interpolation

@pytest.fixture
def sample_grayscale_image():
    return np.array([
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ])

@pytest.fixture
def sample_rgb_image():
    return np.array([
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
        [[19, 20, 21], [22, 23, 24], [25, 26, 27]]
    ])

def test_nearest_neighbor_upscale_grayscale(sample_grayscale_image):
    """Test upscaling grayscale image"""
    scale_factor = 2.0
    result = nearest_neighbor_interpolation(sample_grayscale_image, scale_factor)
    
    expected = np.array([
        [10, 10, 20, 20, 30, 30],
        [10, 10, 20, 20, 30, 30],
        [40, 40, 50, 50, 60, 60],
        [40, 40, 50, 50, 60, 60],
        [70, 70, 80, 80, 90, 90],
        [70, 70, 80, 80, 90, 90]
    ])
    
    assert result.shape == (6, 6)
    np.testing.assert_array_equal(result, expected)

def test_nearest_neighbor_downscale_grayscale(sample_grayscale_image):
    """Test downscaling grayscale image"""
    scale_factor = 0.5
    result = nearest_neighbor_interpolation(sample_grayscale_image, scale_factor)
    
    expected = np.array([
        [10, 30],
        [70, 90]
    ])
    
    assert result.shape == (2, 2)
    np.testing.assert_array_equal(result, expected)

def test_nearest_neighbor_upscale_rgb(sample_rgb_image):
    """Test upscaling RGB image"""
    scale_factor = 2.0
    result = nearest_neighbor_interpolation(sample_rgb_image, scale_factor)
    
    expected = np.array([
        [[1, 2, 3], [1, 2, 3], [4, 5, 6], [4, 5, 6], [7, 8, 9], [7, 8, 9]],
        [[1, 2, 3], [1, 2, 3], [4, 5, 6], [4, 5, 6], [7, 8, 9], [7, 8, 9]],
        [[10,11,12],[10,11,12],[13,14,15],[13,14,15],[16,17,18],[16,17,18]],
        [[10,11,12],[10,11,12],[13,14,15],[13,14,15],[16,17,18],[16,17,18]],
        [[19,20,21],[19,20,21],[22,23,24],[22,23,24],[25,26,27],[25,26,27]],
        [[19,20,21],[19,20,21],[22,23,24],[22,23,24],[25,26,27],[25,26,27]]
    ])
    
    assert result.shape == (6, 6, 3)
    np.testing.assert_array_equal(result, expected)

def test_nearest_neighbor_scale_factor_one(sample_grayscale_image):
    """Test scale factor of 1.0 (no scaling)"""
    result = nearest_neighbor_interpolation(sample_grayscale_image, 1.0)
    np.testing.assert_array_equal(result, sample_grayscale_image)

def test_nearest_neighbor_non_integer_scale(sample_grayscale_image):
    """Test non-integer scale factor"""
    scale_factor = 1.5
    result = nearest_neighbor_interpolation(sample_grayscale_image, scale_factor)
    
    expected = np.array([
        [10, 20, 20, 30],
        [40, 50, 50, 60],
        [40, 50, 50, 60],
        [70, 80, 80, 90]
    ])
    
    assert result.shape == (4, 4)
    np.testing.assert_array_equal(result, expected)

def test_nearest_neighbor_empty_input():
    """Test with empty input"""
    with pytest.raises(ValueError):
        nearest_neighbor_interpolation(np.array([]), 2.0)

def test_nearest_neighbor_invalid_scale_factor(sample_grayscale_image):
    """Test invalid scale factors"""
    with pytest.raises(ValueError):
        nearest_neighbor_interpolation(sample_grayscale_image, 0.0)
    
    with pytest.raises(ValueError):
        nearest_neighbor_interpolation(sample_grayscale_image, -1.0)