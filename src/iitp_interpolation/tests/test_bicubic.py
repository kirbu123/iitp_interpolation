import numpy as np
import pytest

from iitp_interpolation.techniques.bicubic import (
    bicubic_interpolation,
)


@pytest.fixture
def sample_grayscale_image():
    """4x4 grayscale test image"""
    return np.array(
        [
            [10, 20, 30, 40],
            [50, 60, 70, 80],
            [90, 100, 110, 120],
            [130, 140, 150, 160],
        ],
        dtype=np.uint8,
    )


@pytest.fixture
def sample_rgb_image():
    """4x4 RGB test image"""
    return np.array(
        [
            [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
            [[13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24]],
            [[25, 26, 27], [28, 29, 30], [31, 32, 33], [34, 35, 36]],
            [[37, 38, 39], [40, 41, 42], [43, 44, 45], [46, 47, 48]],
        ],
        dtype=np.uint8,
    )


def test_bicubic_identity_scale(sample_rgb_image):
    """Test scale factor 1.0 (no change)"""
    result = bicubic_interpolation(sample_rgb_image, 1.0)
    np.testing.assert_array_equal(result, sample_rgb_image)


def test_bicubic_typization(sample_rgb_image):
    """Test scale factor 1.0 (no change)"""
    result = bicubic_interpolation(sample_rgb_image, 2.5)
    assert result.dtype == sample_rgb_image.dtype
