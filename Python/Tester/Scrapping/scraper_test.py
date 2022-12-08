import unittest
from scraper import *

class TestGetInfo(unittest.TestCase):
           
    def test_nomes(self):
        obtido = getNomes()
        msgEr = "ERRO - Elementos vazios inseridos na lista!"
        msgCorr = "CORRETO - Todos os nomes dos times mostrados na página, inseridos na lista!"
        #self.assertNotIn(' ', obtido, msgEr)
        #self.assertIn(' ', obtido, msgCorr)
        self.assertEqual(obtido[0], 'Palmeiras', 'CERTO')
        
    def test_pontos(self):
        obtido = getPontos()
        msgEr = "ERRO - Elementos vazios inseridos na lista!"
        msgCorr = "CORRETO - Todos os pontos dos times mostrados na página, inseridos na lista!"
        self.assertNotIn(' ', obtido, msgEr)
        
if __name__ == '__main__':
    unittest.main()
    
# unittest.main(argv=[''], verbosity=2, exit=False)
# Substituir pelo if __name__ caso rodar no jupyter notebooks