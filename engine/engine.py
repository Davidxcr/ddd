from get_service import GetService

class Engine(GetService):
    def get_service(self):
       pass

class CapuletEngine(Engine):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def get_service(self):
        return self.current_mileage - self.last_service_mileage > 30000

class WilloughbyEngine(Engine):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def get_service(self):
        return self.current_mileage - self.last_service_mileage > 60000

class SternmanEngine(Engine):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date)
        self.warning_light_is_on = warning_light_is_on

    def engine_should_be_serviced(self):
        return self.warning_light_is_on