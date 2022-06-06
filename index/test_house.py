import unittest
from .house import House

class HouseTestCase(unittest.TestCase):

    def test_house_with_name_koen(self):
        home = House("Koen", 10)

        self.assertEqual(home.name.upper(), "KOEN")

    def test_house_with_age_10(self):
        home = House("Koen", 10)

        self.assertEqual(home.age, 10)
