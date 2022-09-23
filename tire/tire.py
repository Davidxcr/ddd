from get_service import GetService


class Tire(GetService):

    def get_service(self):
        pass


class SyltherinTire(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def get_service(self):
        for i in range(4):
            if (self.tire_wear[i] >= 0.9):
                return True
        return False


class PirelliTire(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def get_service(self):
        sum = 0
        for i in range(4):
            sum += self.tire_wear[i]
        return sum >= 3