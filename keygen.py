# UNIVERSAL WINDOWS95 ACTIVATOR: This script generates random keys. By default, nothing
# happens if ran by itself, its only purpose is to be called by either uwact.py or gui.py

import random


def generate_random_number(length: int) -> str:
    return ''.join(str(random.randint(0, 9)) for _ in range(length))


def generate_cd_key() -> str:
    site = generate_random_number(3)

    while int(site) in (333, 444, 555, 666, 777, 888, 999):
        site = generate_random_number(3)

    rest = generate_random_number(7)

    while sum(int(digit) for digit in rest) % 7 != 0 or int(rest[0]) >= 8:
        rest = generate_random_number(7)

    return f"{site}-{rest}"


def generate_oem_key() -> str:
    date = f"{random.randint(1, 366)}{random.randint(95, 103)}"
    year = random.randint(95, 103)
    year_str = str(year) if year >= 10 else f"0{year}"
    rest = generate_random_number(15)

    return f"{date}-OEM-{year_str}-{rest}"