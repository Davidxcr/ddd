from get_service import GetService

class Car(GetService):
    def __init__(self, engine, battery, tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def get_service(self):
        return self.engine.get_service() or self.battery.get_service() or self.tire.get_service()