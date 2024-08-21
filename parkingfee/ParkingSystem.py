import math
import os
from datetime import datetime

from ParkingSession import ParkingSession
from Car import Car
import json


class ParkingSystem:
    def __init__(self, pricing_file):
        self.sessions = []
        self.pricing_rules = self.load_pricing_rules(pricing_file)

    def load_pricing_rules(self, filename):
        with open(filename, 'r') as file:
            pricing_rules = json.load(file)
        return pricing_rules

    def park_car(self, car_identity, start_time, frequent_number=None):
        if not Car.validate_car_identity(car_identity):
            raise ValueError("Invalid car identity format.")
        car = Car(car_identity, frequent_number)
        session = ParkingSession(car, start_time)
        self.sessions.append(session)
        return session

    def pick_up_car(self, car_identity, end_time):
        session = next((s for s in self.sessions if s.car.car_identity == car_identity and s.end_time is None), None)
        if session is None:
            raise ValueError("No active session found for this car.")

        session.end_session(end_time)
        self.calculate_fee(session)
        return session.fee

    def calculate_fee(self, session):
        start = session.start_time
        end = datetime.strptime(session.end_time, "%Y-%m-%d %H:%M")
        duration = (end - start).total_seconds() / 3600  # duration in hours

        day_of_week = start.strftime("%A")
        prices = self.pricing_rules[day_of_week]
        fee = 0
        for period, details in prices.items():
            if "price_per_hour" in details:
                fee += min(details["max_stay_hours"], duration) * details["price_per_hour"]
                duration -= min(details["max_stay_hours"], duration)
            elif "price_one_time" in details:
                fee += details["price_one_time"]

        session.fee = math.ceil(fee * 100) / 100  # Rounding up to the nearest cent
khan
';'
    def view_history(self, car_identity):
        total_payment = sum(session.fee for session in self.sessions if session.car.car_identity == car_identity)
        file_path = f"data/{car_identity}.txt"
        if not os.path.exists('data'):
            os.makedirs('data')

        with open(file_path, 'w') as file:
            file.write(f"Total payment: ${total_payment:.2f}\n")
            file.write("Available credits: $0.00\n")  # Placeholder for actual credits logic
            file.write("Parked Dates:\n")
            for session in self.sessions:
                if session.car.car_identity == car_identity:
                    parked_dates = f"{session.start_time.strftime('%Y-%m-%d %H:%M')} – {session.end_time.strftime('%Y-%m-%d %H:%M')} ${session.fee:.2f}\n"
                    file.write(parked_dates)
        return file_path
