import unittest

class Arithmetic:
    def incriment(self,num):
        return num + 1

class ArithmeticTest(unittest.TestCase):
    def test_increment(self):
        self.assertEquals(Arithmetic().incriment(3),4)


