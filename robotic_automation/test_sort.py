import pytest
from robotic_automation.sort import sort


def test_sort_rejected_by_total_measure_and_mass():
    assert sort(100, 100, 100, 22) == "REJECTED"


def test_sort_rejected_by_width_and_mass():
    assert sort(200, 25, 40, 22) == "REJECTED"


def test_sort_rejected_by_length_and_mass():
    assert sort(25, 40, 200, 22) == "REJECTED"


def test_sort_rejected_by_height_and_mass():
    assert sort(25, 200, 40, 22) == "REJECTED"


def test_sort_special_by_bulky():
    assert sort(25, 200, 40, 15) == "SPECIAL"


def test_sort_special_by_heavy():
    assert sort(25, 100, 40, 22) == "SPECIAL"


def test_sort_standard():
    assert sort(25, 100, 40, 15) == "STANDARD"


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
