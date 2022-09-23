import unittest
from engine.engine import WilloughbyEngine


class TestWilloughby(unittest.TestCase):
    def testNeedsService(self):
        last_service_mileage = 0
        current_mileage = 60001
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.get_service())

    def testDoesNotNeedService(self):
        last_service_mileage = 0
        current_mileage = 60000
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.get_service())