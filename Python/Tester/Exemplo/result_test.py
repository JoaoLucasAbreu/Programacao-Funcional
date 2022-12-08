import unittest
from ex3 import *

class TestResult(unittest.TestCase):
    
    def test_sum(self):
        obtido = sum([1, 2, 3])
        desejado = 6
        msg = "Should be 6"
        self.assertEqual(obtido, desejado, msg)
        
    def test_sum_tuple(self):
        self.assertNotEqual(sum((1, 2, 3)), 5, "Should not be 6")
        
    def test_cont(self):
        obtido = cont()
        desejado = 34
        msg = "Deu erro"
        self.assertEqual(obtido, desejado, msg)
        
if __name__ == '__main__':
    unittest.main()
    
# unittest.main(argv=[''], verbosity=2, exit=False)
# Substituir pelo if __name__ caso rodar no jupyter notebooks