import csv
import random
from collections import deque

from src.consts import *
from src.data.random_data_generator import choose_random_from_file, generate_random_number, create_random_address


def generate_data(rows, file=None):
    data_dict = deque()

    id_ist = [i for i in range(START_ID, START_ID + rows)]
    randomized_ids = random.sample(id_ist, k=rows)

    for i in range(0, rows):
        data_dict.append(generate_person_info(randomized_ids[i]))

    names_list = [
        ID,
        NAME,
        AGE,
        CLASS,
        ADDRESS,
        INCOME,
        FAMILY,
        CITIZEN,
        PREVIOUS_SUBSTANCE_USE,
        TRANSPORT_METHOD,
        NEIGHBOR,
        STREET_LIFE,
        WORKING,
        STUDY_LEVEL,
        HOBBY,
        SONS_NUMBER
    ]

    if file is not None:
        with open(file + '.csv', 'w', newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=names_list)
            writer.writeheader()
            writer.writerows(data_dict)

    return data_dict


def generate_person_info(id_key):
    person_info = {
        ID: id_key,
        NAME: choose_random_from_file("sources/names.txt") + " " + choose_random_from_file(
            "sources/last_names.txt"),
        AGE: generate_random_number(13, 32),
        CLASS: generate_random_number(0, 2),
        ADDRESS: create_random_address(allow_south=False, street_max=200),
        INCOME: generate_random_number(500000, 1200000),
        FAMILY: random.choice(["Madre", "Padre", "Solo", "Familiares cercanos"]),
        CITIZEN: random.choice(["Colombia", "Venezuela"]),
        PREVIOUS_SUBSTANCE_USE: random.choice([True, False]),
        TRANSPORT_METHOD: random.choice(["Sitp", "Transmilenio", "Bicicleta"]),
        NEIGHBOR: random.choice(["Santa cecilia", "Cerro norte", "Lijaca", "Codito", "Soratama", "Verbenal"]),
        STREET_LIFE: random.choice([True, False]),
        WORKING: random.choice([True, False]),
        STUDY_LEVEL: random.choice(["Pocos estudios", "Primaria", "Secundaria", "Tecnico"]),
        HOBBY: random.choice(["Consumo de drogas", "Trabajar", "Micro futbol"]),
        SONS_NUMBER: generate_random_number(0, 2)
    }

    return person_info