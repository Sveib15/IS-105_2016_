import unittest
from is105 import pluss


class TestPluss(unittest.TestCase):
    def setUp(self):
        pass
    def test_nummer_5_7(self):
        self.assertEqual(pluss(5,7), 11)
        
    if __name__ == '__main__':
        unittest.main()
        
        

 