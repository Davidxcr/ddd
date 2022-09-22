import unittest
from datetime import date
from battery.battery import NubbinBattery


class TestNubbin(unittest.TestCase):
    def testNeedsService(self):
        current_date = date.today()
        date_last_serviced = current_date.replace(year=self.year - 4)
        battery = NubbinBattery(current_date, date_last_serviced)
        self.assertTrue(battery.get_service())

    def testDoesNotNeedService(self):
        current_date = date.today()
        date_last_serviced = current_date.replace(year=self.year - 3)
        battery = NubbinBattery(current_date, date_last_serviced)
        self.assertFalse(battery.get_service())