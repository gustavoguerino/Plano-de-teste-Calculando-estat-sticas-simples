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

    @timeout_decorator.timeout(1)
    def test_valor_not_int(self):
        data = "testeDeSoftware"
        with io.BytesIO(data) as sys.stdin:
            with self.assertRaises(TypeError):
                self.assertTrue(is_sizeSqn(1))
        sys.stdin = sys.__stdin__
    
    #
    # Apartir deste teste que exige uma entrada (INPUT()) os anteriores sao quebrados, 
    # se tornando impossivel continuar continuar com TDD, sendo preciso modificar os testes anterioresm TDD, sendo preciso modificar os testes anteriores
    # para prosseguir.
    #
    # O teste nao foi corretamente escrito, nao prevendo entradas nos primeiros casos.
    # Para prosseguir apartir deste ponto os testes 1 e 2 precisariam ser reescritos passando
    # uma entrada valida.
    # 
    # Continuaremos com os testes ignorando o resultado dos dois primeiros
    #
    # Todos os testes apartir do 5 são verificando resultados, sem exemplos de entrada, e
    # verificando o resultado das operações em um retorno que deveria ser boolean.
    #
           
if __name__ == '__main__':
    unittest.main()