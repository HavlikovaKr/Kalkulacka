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




@pytest.mark.parametrize(
    "x, y, result",
    [
        (5, 3, 2),
        (-1, -1, 0),
        (8, 3, 5),
        (0, 5, -5)

    ],
)

def test_odcitani_subtract(x, y, result):
    assert calculator.subtract(x,y) == result



@pytest.mark.parametrize(
    "x, y, result",
    [
        (2, 3, 6),
        (2, 15, 30),
        (-1, -1, 1),
        (0, 2, 0)
    ],
)

def test_nasobeni_multiply(x, y, result):
    assert calculator.multiply(x, y) == result



@pytest.mark.parametrize(
    "x, y, result",
    [
        (6, 3, 2),
        (-1, -1, 1),
        (9, 3, 3),
        (2, 0, "Error! Division by zero."),
        (8, 3, 2.7)

    ],
)

def test_deleni_divide(x, y, result):
    assert calculator.divide(x, y) == result

