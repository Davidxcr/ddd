from car import Car
from engine.engine import CapuletEngine, WilloughbyEngine, SternmanEngine
from battery.battery import NubbinBattery, SpindlerBattery
from tire.tire import SyltherinTire, PirelliTire


class allCars():
    def create_calliope(self, current_date, date_last_serviced, current_mileage, last_service_mileage, tire_wear):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(date_last_serviced, current_date)
        tire = SyltherinTire(tire_wear)
        car = Car(engine, battery, tire)
        return car

    def create_glissade(self, current_date, date_last_serviced, current_mileage, last_service_mileage, tire_wear):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(date_last_serviced, current_date)
        tire = PirelliTire(tire_wear)
        car = Car(engine, battery, tire)
        return car

    def create_palindrome(self, current_date, date_last_serviced, warning_light_on, tire_wear):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(date_last_serviced, current_date)
        tire = SyltherinTire(tire_wear)
        car = Car(engine, battery, tire)
        return car

    def create_rorschach(self, current_date, date_last_serviced, current_mileage, last_service_mileage, tire_wear):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(date_last_serviced, current_date)
        tire = PirelliTire(tire_wear)
        car = Car(engine, battery, tire)
        return car

    def create_thovex(self, current_date, date_last_serviced, current_mileage, last_service_mileage, tire_wear):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(date_last_serviced, current_date)
        tire = SyltherinTire(tire_wear)
        car = Car(engine, battery, tire)
        return car