from battery.battery import Battery
from utils import date_plus_years

class NubbinBattery(Battery):
    def __init__(self, current_date, date_last_serviced) -> None:
        self.current_date = current_date
        self.date_last_serviced = date_last_serviced

    def need_service(self):
        date_service_needed = date_plus_years(self.date_last_serviced, 4)
        return date_service_needed < self.current_date