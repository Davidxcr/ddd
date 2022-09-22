import unittest
from tire.tire import PirelliTire


class TestPirelli(unittest.TestCase):
    def testNeedsService(self):
        tire = PirelliTire([0.75, 0.75, 0.75, 0.75])
        self.assertTrue(tire.get_service())

    def testDoesNotNeedService(self):
        tire = PirelliTire([0.75, 0.75, 0.75, 0.74])
        self.assertFalse(tire.get_service())