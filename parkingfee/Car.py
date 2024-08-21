import re


class Car:
    def __init__(self, car_identity, frequent_parking_number=None):
        self.car_identity = car_identity
        self.frequent_parking_number = frequent_parking_number

    @staticmethod
    def validate_car_identity(car_identity):
        return bool(re.match(r'\d{2}[A-Z]-\d{5}', car_identity))

    @staticmethod
    def validate_frequent_parking_number(number):
        # Implement a simple modulo 11 validation as placeholder
        try:
            digits = list(map(int, number[:-1]))
            checksum = sum(digits) % 11 == int(number[-1])
            return checksum
        except:
            return False
