import unittest

from src.bundle.generate import generate_data
from src.consts import ID


class GenerateTest(unittest.TestCase):

    def test_should_create_number_of_rows(self):
        data = generate_data(10)
        self.assertEqual(10, len(data))

        data = generate_data(15)
        self.assertEqual(15, len(data))

        data = generate_data(100)
        self.assertEqual(100, len(data))

        data = generate_data(100)
        self.assertEqual(100, len(data))

    def test_should_id_be_unique(self):
        data = generate_data(10000)
        self.assertEqual(10000, len(data))

        id_set = set()

        for element in data:
            if element[ID] in id_set:
                self.fail("Repeated element " + str(element[ID]))
            id_set.add(element[ID])

        data = generate_data(10)
        self.assertEqual(10, len(data))

        id_set = set()

        for element in data:
            if element[ID] in id_set:
                self.fail("Repeated element " + str(element[ID]))
            id_set.add(element[ID])

    def test_should_save_to_file(self):
        data = generate_data(10000, file="out")
        self.assertEqual(10000, len(data))
