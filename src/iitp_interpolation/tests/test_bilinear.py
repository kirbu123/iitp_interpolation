import numpy as np
import pytest

from iitp_interpolation.techniques.bilinear import bilinear_interpolation


@pytest.fixture
def sample_grayscale_image():
    return np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]], dtype=np.uint8)


@pytest.fixture
def sample_rgb_image():
    return np.array(
        [
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
            [[19, 20, 21], [22, 23, 24], [25, 26, 27]],
        ],
        dtype=np.uint8,
    )


def test_bilinear_upscale_grayscale(sample_rgb_image):
    """Test upscaling grayscale image (2x)"""
    result = bilinear_interpolation(sample_rgb_image, 2.0)
    assert result.shape == (6, 6, 3)
    assert result[0, 0, 0] == 1


def test_bilinear_non_integer_scale(sample_rgb_image):
    """Test non-integer scale factor (1.5x)"""
    result = bilinear_interpolation(sample_rgb_image, 1.5)
    assert result.shape == (4, 4, 3)  # 3x3 * 1.5 = 4.5 -> rounds to 4
    assert 10 <= result[2, 2, 2] <= 20  # Middle value range


def test_bilinear_identity_scale(sample_rgb_image):
    """Test scale factor 1.0 (no change)"""
    result = bilinear_interpolation(sample_rgb_image, 1.0)
    np.testing.assert_array_equal(result, sample_rgb_image)


def test_bilinear_rgb_image(sample_rgb_image):
    """Test RGB image interpolation"""
    result = bilinear_interpolation(sample_rgb_image, 1.5)
    assert result.shape == (4, 4, 3)
    assert not np.array_equal(result[:, :, 0], result[:, :, 1])


def test_bilinear_invalid_input():
    """Test invalid input handling"""
    with pytest.raises(ValueError):
        bilinear_interpolation(np.array([]), 1.0)

    with pytest.raises(ValueError):
        bilinear_interpolation(np.zeros((3, 3)), -1.0)
