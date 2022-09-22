import unittest
from engine.engine import SternmanEngine


class TestSternman(unittest.TestCase):
    def testNeedsService(self):
        engine = SternmanEngine(warning_light_on=True)
        self.assertTrue(engine.get_service())

    def testDoesNotNeedService(self):
        engine = SternmanEngine(warning_light_on=False)
        self.assertFalse(engine.get_service())