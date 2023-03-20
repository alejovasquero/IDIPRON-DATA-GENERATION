#!/usr/bin/env python
# coding: utf-8


import random

def generate_random_number(minimum, maximum):
    if minimum > maximum:
        return None
    return random.randint(minimum, maximum)


def generate_random_string(length, alphabet):
    if alphabet == "" or alphabet is None:
        return None
    result_string = ""
    for i in range(0, length):
        result_string += random.choice(alphabet)
    return result_string


def choose_random_from_file(file_name):
    file = open(file_name, "r", encoding="utf-8")
    lines = file.readlines()
    file.close()

    random_line = random.randrange(0, len(lines))

    return (lines[random_line]).strip()


def create_random_id(id_size: int, min_value: int, max_value: int):
    value_set = [str(i) for i in range(min_value, max_value + 1)]

    result_id = []
    for i in range(id_size):
        if len(value_set) == 0:
            break
        random_element = random.randrange(len(value_set))

        result_id.append(value_set[random_element])
        value_set.pop(random_element)

    return result_id


def generate_random_date():
    day = random.randint(1, 29)
    month = random.randint(1, 12)
    year = random.randint(2000, 2030)

    date = "{0:02}/{1:02}/{2}".format(day, month, year)
    return date


def create_random_address(allow_south=True, street_min=1, street_max=200):
    orientations_north_south = ["Calle", "Diagonal"]
    orientations_west_easth = ["Carrera", "Transversal"]
    additions = ["A", "B", "C", "D", ""]

    first_addition = random.choice(additions)
    second_addition = random.choice(additions)

    is_south = random.choice(["", "Sur"])

    if not allow_south:
        is_south = ""

    is_bis = random.choice(["bis", ""])
    if second_addition == "":
        is_bis = ""

    main_orientation = random.choice(orientations_north_south + orientations_west_easth)
    main_number = random.randint(street_min, street_max)
    second_number = random.randint(1, 200)
    third_number = random.randint(1, 200)

    result_address = None
    format_string = ""

    if main_orientation in orientations_north_south:
        format_string = "{orientation} {first}{first_addition} {isSouth} #{second}{second_addition}{bis}-{third}"
    else:
        format_string = "{orientation} {first}{first_addition} #{second}{second_addition}{bis}-{third} {isSouth}"
    return format_string.format(orientation=main_orientation,
                                first=main_number,
                                second=second_number,
                                third=third_number,
                                isSouth=is_south,
                                first_addition=first_addition,
                                second_addition=second_addition,
                                bis=is_bis
                                )
