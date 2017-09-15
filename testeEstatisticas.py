import unittest
from estatisticas import is_sizeSqn

class TesteEstatisticas(unittest.TestCase):
    def test_seqnumeros_is_int(self):
        self.assertTrue(is_sizeSqn(1))
        
    def teste_seqnumeros_not_int(self):
        with self.assertRaises(TypeError):
            is_sizeSqn("testeDeSoftware") 
           
if __name__ == '__main__':
    unittest.main()