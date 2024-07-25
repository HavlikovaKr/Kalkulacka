import pytest
from src import calculator

@pytest.mark.parametrize(
    "x, y, result",
    [
        (2, 3, 5),
        (1, 1, 2),
        (-1, -1, -2),
        (5, 0, 5)
    ],
)

def test_scitani_add(x, y, result):
    assert calculator.add(x, y) == result


