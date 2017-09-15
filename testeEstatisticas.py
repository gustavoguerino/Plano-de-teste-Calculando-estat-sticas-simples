import unittest, io, sys, timeout_decorator

from estatisticas import is_sizeSqn

class TesteEstatisticas(unittest.TestCase):
    @timeout_decorator.timeout(1)
    def test_seqnumeros_is_int(self):
        self.assertTrue(is_sizeSqn(1))
        
    @timeout_decorator.timeout(1)
    def test_seqnumeros_not_int(self):
        with self.assertRaises(TypeError):
            is_sizeSqn("testeDeSoftware") 
            is_sizeSqn("7.0") 

    @timeout_decorator.timeout(1)
    def test_valor_is_int(self):
        data = "2"
        with io.BytesIO(data) as sys.stdin:
            self.assertTrue(is_sizeSqn(1))
        sys.stdin = sys.__stdin__
           
if __name__ == '__main__':
    unittest.main()