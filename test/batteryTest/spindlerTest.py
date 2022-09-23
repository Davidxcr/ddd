import unittest
from datetime import date
from battery.battery import SpindlerBattery


class TestSpindler(unittest.TestCase):
    def testNeedsService(self):
        current_date = date.today()
        date_last_serviced = current_date.replace(year=self.year - 2)
        battery = SpindlerBattery(current_date, date_last_serviced)
        self.assertTrue(battery.get_service())

    def testDoesNotNeedService(self):
        current_date = date.today()
        date_last_serviced = current_date.replace(year=self.year - 1)
        battery = SpindlerBattery(current_date, date_last_serviced)
        self.assertFalse(battery.get_service())