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
