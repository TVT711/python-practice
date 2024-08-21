import unittest
from car import Car


class TestCar(unittest.TestCase):
    def test_valid_car_identity(self):
        car = Car("01A-12345")
        self.assertEqual(car.car_identity, "01A-12345")

    def test_invalid_car_identity_raises_exception(self):
        with self.assertRaises(ValueError):
            Car("invalid_identity")


if __name__ == '__main__':
    unittest.main()
