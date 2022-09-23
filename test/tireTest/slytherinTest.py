import unittest
from tire.tire import Syltherin


class TestSyltherin(unittest.TestCase):
    def testNeedsService(self):
        tire = SyltherinTire([0, 0, 0, 0.9])
        self.assertTrue(tire.get_service())

    def testDoesNotNeedService(self):
        tire = SyltherinTire([0.2, 0.3, 0.4, 0.5])
        self.assertFalse(tire.get_service())