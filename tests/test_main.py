import pytest

from src.main import calculate_average


def test_calculate_average():
    with pytest.raises(ValueError):
        calculate_average([])
