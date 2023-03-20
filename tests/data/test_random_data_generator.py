
import unittest

from src.data.random_data_generator import generate_random_string, generate_random_number, create_random_id, \
    generate_random_date, create_random_address, choose_random_from_file


class IntervalNumberTestClass(unittest.TestCase):

    def assert_number_in_interval(self, minumum, maximum, value):
        self.assertTrue(minumum <= value <= maximum)

    def test_should_get_unique_random(self):
        number = generate_random_number(100, 100)
        self.assertEquals(number, 100)

    def test_should_get_invalid_interval(self):
        number = generate_random_number(200, 100)
        self.assertEqual(number, None)

    def test_should_get_random(self):
        number = generate_random_number(0, 10)
        self.assert_number_in_interval(0, 10, number)

        number_2 = generate_random_number(0, 10)
        self.assert_number_in_interval(0, 10, number_2)

        number_3 = generate_random_number(0, 10)
        self.assert_number_in_interval(0, 10, number_3)


if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(IntervalNumberTestClass))

import unittest


class RandomStringTestClass(unittest.TestCase):

    def test_should_get_empty_string(self):
        random_string = generate_random_string(0, "abc")
        self.assertEqual(0, len(random_string))

    def test_should_return_exact_length(self):
        random_string = generate_random_string(5, "abc")
        self.assertEqual(5, len(random_string))

        random_string = generate_random_string(10, "abc")
        self.assertEqual(10, len(random_string))

        random_string = generate_random_string(1000, "abc")
        self.assertEqual(1000, len(random_string))

    def test_should_use_alphabet(self):
        random_string = generate_random_string(5, "abc")
        self.assert_alphabet_use("abc", random_string)

        random_string = generate_random_string(50, "adccas%0||<>*-")
        self.assert_alphabet_use("adccas%0||<>*-", random_string)

        random_string = generate_random_string(1000, "adccaadsja()/4322!!s%0||<>*-")
        self.assert_alphabet_use("adccaadsja()/4322!!s%0||<>*-", random_string)

    def test_should_return_no_alphabet(self):
        random_string = generate_random_string(5, "")
        self.assertEqual(random_string, None)

    def assert_alphabet_use(self, alphabet: str, string_value: str):
        for i in string_value:
            self.assertIn(i, alphabet)


if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(RandomStringTestClass))

import unittest


class RandomIDTestClass(unittest.TestCase):

    def test_should_return_empty_id(self):
        random_id = create_random_id(0, 1, 2)
        self.assertEqual(0, len(random_id))

    def test_should_return_min_result(self):
        random_id = create_random_id(10, 1, 2)
        self.assertEqual(2, len(random_id))

    def test_should_return_non_repeated(self):
        random_id = create_random_id(10, 1, 200)
        self.assert_non_repeated(random_id, 1, 200)

    def assert_non_repeated(self, ID, minimum, maximum):
        for i in ID:
            self.assertEqual(ID.count(i), 1)
            self.assertTrue(minimum <= int(i) <= maximum)


if __name__ == "__main__":
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(RandomIDTestClass))

import unittest


class RandomDateTestClass(unittest.TestCase):

    def test_should_return_empty_id(self):
        random_date = generate_random_date()
        self.assert_validate_date(random_date)

        random_date = generate_random_date()
        self.assert_validate_date(random_date)

        random_date = generate_random_date()
        self.assert_validate_date(random_date)

        random_date = generate_random_date()
        self.assert_validate_date(random_date)

    def assert_validate_date(self, date):
        date_values = date.split("/")
        self.assertEqual(3, len(date_values))
        self.assertTrue(1 <= int(date_values[0]) <= 31)
        self.assertTrue(1 <= int(date_values[1]) <= 12)
        self.assertTrue(2000 <= int(date_values[2]) <= 2030)


if __name__ == "__main__":
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(RandomDateTestClass))

import unittest


class RandomAddressTestClass(unittest.TestCase):

    def test_should_return_address(self):
        random_address = create_random_address()
        self.assertNotEqual(None, random_address)
        self.assert_address(random_address)

        random_address = create_random_address()
        self.assertNotEqual(None, random_address)
        self.assert_address(random_address)

        random_address = create_random_address()
        self.assertNotEqual(None, random_address)
        self.assert_address(random_address)

        random_address = create_random_address()
        self.assertNotEqual(None, random_address)
        self.assert_address(random_address)

        random_address = create_random_address()
        self.assertNotEqual(None, random_address)
        self.assert_address(random_address)

        random_address = create_random_address()
        self.assertNotEqual(None, random_address)
        self.assert_address(random_address)

        random_address = create_random_address()
        self.assertNotEqual(None, random_address)
        self.assert_address(random_address)

        random_address = create_random_address()
        self.assertNotEqual(None, random_address)
        self.assert_address(random_address)

        random_address = create_random_address()
        self.assertNotEqual(None, random_address)
        self.assert_address(random_address)

        random_address = create_random_address()
        self.assertNotEqual(None, random_address)
        self.assert_address(random_address)

    def assert_address(self, address):
        self.assertTrue(
            "Calle" in address
            or "Carrera" in address
            or "Diagonal" in address
            or "Transversal" in address
        )


if __name__ == "__main__":
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(RandomAddressTestClass))

import unittest


class RandomWordDictionaryTestClass(unittest.TestCase):

    def test_should_return_word(self):
        random_word = choose_random_from_file("dict/test_dict.txt")
        self.assertNotEqual(None, random_word)
        self.assert_word_existence(random_word, "dict/test_dict.txt")

        random_word = choose_random_from_file("dict/test_dict.txt")
        self.assertNotEqual(None, random_word)
        self.assert_word_existence(random_word, "dict/test_dict.txt")

        random_word = choose_random_from_file("dict/test_dict.txt")
        self.assertNotEqual(None, random_word)
        self.assert_word_existence(random_word, "dict/test_dict.txt")

        random_word = choose_random_from_file("dict/test_dict.txt")
        self.assertNotEqual(None, random_word)
        self.assert_word_existence(random_word, "dict/test_dict.txt")

        random_word = choose_random_from_file("dict/test_dict.txt")
        self.assertNotEqual(None, random_word)
        self.assert_word_existence(random_word, "dict/test_dict.txt")

    def assert_word_existence(self, word, file_name):
        file = open(file_name, "r")
        exists = False

        for line in file.readlines():
            exists = exists or word in line
        self.assertTrue(exists)
        file.close()


if __name__ == "__main__":
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(RandomWordDictionaryTestClass))
