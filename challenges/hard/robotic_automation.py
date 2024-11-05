import pytest


def sort(width, height, length, mass) -> str:
    if (
        not width
        or width <= 0
        or not height
        or height <= 0
        or not length
        or length <= 0
        or not mass
        or mass <= 0
    ):
        raise ValueError("Invalid package information")

    is_bulky = (
        width * height * length >= 1000000
        or width >= 150
        or height >= 150
        or length >= 150
    )

    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    return "STANDARD"


def test_sort_rejected_by_total_measure_and_mass():
    assert "REJECTED" == sort(100, 100, 100, 22)


def test_sort_rejected_by_width_and_mass():
    assert "REJECTED" == sort(200, 25, 40, 22)


def test_sort_rejected_by_length_and_mass():
    assert "REJECTED" == sort(25, 40, 200, 22)


def test_sort_rejected_by_height_and_mass():
    assert "REJECTED" == sort(25, 200, 40, 22)


def test_sort_special_by_bulky():
    assert "SPECIAL" == sort(25, 200, 40, 15)


def test_sort_special_by_heavy():
    assert "SPECIAL" == sort(25, 100, 40, 22)


def test_sort_standard():
    assert "STANDARD" == sort(25, 100, 40, 15)


def test_sort_invalid_data():
    # Invalid width
    with pytest.raises(ValueError) as excinfo:
        sort(0, 100, 40, 22)
    assert str(excinfo.value) == "Invalid package information"

    # Invalid height
    with pytest.raises(ValueError) as excinfo:
        sort(100, 0, 40, 22)
    assert str(excinfo.value) == "Invalid package information"

    # Invalid length
    with pytest.raises(ValueError) as excinfo:
        sort(100, 40, -2, 22)
    assert str(excinfo.value) == "Invalid package information"

    # Invalid mass
    with pytest.raises(ValueError) as excinfo:
        sort(100, 40, 25, -1)
    assert str(excinfo.value) == "Invalid package information"


def test_sort_missing_data():
    # Missing width
    with pytest.raises(ValueError) as excinfo:
        sort(width=None, height=100, length=40, mass=22)
    assert str(excinfo.value) == "Invalid package information"

    # Missing height
    with pytest.raises(ValueError) as excinfo:
        sort(width=25, height=None, length=40, mass=22)
    assert str(excinfo.value) == "Invalid package information"

    # Missing length
    with pytest.raises(ValueError) as excinfo:
        sort(width=25, height=100, length=None, mass=22)
    assert str(excinfo.value) == "Invalid package information"

    # Missing mass
    with pytest.raises(ValueError) as excinfo:
        sort(width=25, height=100, length=40, mass=None)
    assert str(excinfo.value) == "Invalid package information"
