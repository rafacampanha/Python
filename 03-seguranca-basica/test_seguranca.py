import socket
import unittest
import portas
import senhas


class TesteSenhas(unittest.TestCase):
    def test_senha_fraca_e_forte(self):
        self.assertLess(senhas.avaliar_senha("abc")[0], 3)
        self.assertEqual(senhas.avaliar_senha("Abc123!@#xyz9")[0], 5)

    def test_hash_confere(self):
        sal, h = senhas.gerar_hash("minhaSenha!1", iteracoes=1000)
        self.assertTrue(senhas.conferir_senha("minhaSenha!1", sal, h, iteracoes=1000))
        self.assertFalse(senhas.conferir_senha("outra", sal, h, iteracoes=1000))

    def test_senha_gerada(self):
        self.assertEqual(len(senhas.gerar_senha(20)), 20)


class TestePortas(unittest.TestCase):
    def test_porta_aberta_local(self):
        servidor = socket.socket()
        servidor.bind(("127.0.0.1", 0))
        servidor.listen(1)
        porta = servidor.getsockname()[1]
        try:
            self.assertTrue(portas.porta_aberta("127.0.0.1", porta))
        finally:
            servidor.close()
        self.assertFalse(portas.porta_aberta("127.0.0.1", porta))


if __name__ == "__main__":
    unittest.main()
