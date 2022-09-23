from get_service import GetService
from datetime import datetime

class Battery(GetService):
    def get_service(self):
        pass

class NubbinBattery(Battery):
    def __init__(self, current_date, date_last_serviced) -> None:
       self.date_last_serviced = date_last_serviced
       self.current_date = current_date
    def get_service(self):
        date_service_needed = self.date_last_serviced.replace(year = self.date_last_serviced + 4)
        return date_service_needed < datetime.today().date()


class SpindlerBattery(Battery):
    def __init__(self, current_date, date_last_serviced) -> None:
       self.date_last_serviced = date_last_serviced
       self.current_date = current_date
    def get_service(self):
        date_service_needed = self.date_last_serviced.replace(year = self.date_last_serviced + 2)
        return date_service_needed < datetime.today().date()