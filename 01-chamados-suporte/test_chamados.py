import unittest
import chamados


class TesteChamados(unittest.TestCase):
    def setUp(self):
        # banco na memória: some quando o teste termina
        self.con = chamados.conectar(":memory:")

    def test_criar_e_listar(self):
        id_novo = chamados.criar(self.con, "Impressora parada", "Sala 2")
        linhas = chamados.listar(self.con)
        self.assertEqual(len(linhas), 1)
        self.assertEqual(linhas[0][0], id_novo)
        self.assertEqual(linhas[0][2], "aberto")

    def test_titulo_vazio(self):
        with self.assertRaises(ValueError):
            chamados.criar(self.con, "   ")

    def test_atualizar_status(self):
        id_novo = chamados.criar(self.con, "Sem internet")
        self.assertTrue(chamados.atualizar_status(self.con, id_novo, "resolvido"))
        self.assertEqual(len(chamados.listar(self.con, "resolvido")), 1)
        with self.assertRaises(ValueError):
            chamados.atualizar_status(self.con, id_novo, "qualquer coisa")

    def test_apagar(self):
        id_novo = chamados.criar(self.con, "Teste")
        self.assertTrue(chamados.apagar(self.con, id_novo))
        self.assertFalse(chamados.apagar(self.con, id_novo))


if __name__ == "__main__":
    unittest.main()
