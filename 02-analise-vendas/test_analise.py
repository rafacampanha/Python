import unittest
import pandas as pd
import analise


class TesteAnalise(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            "data": pd.to_datetime(["2025-01-01", "2025-01-02", "2025-02-01"]),
            "produto": ["Mouse", "Mouse", "Monitor"],
            "quantidade": [2, 1, 1],
            "preco_unitario": [60, 60, 900],
        })
        self.df["faturamento"] = self.df["quantidade"] * self.df["preco_unitario"]

    def test_resumo(self):
        r = analise.resumo(self.df)
        self.assertEqual(r["faturamento_total"], 1080)
        self.assertEqual(r["itens_vendidos"], 4)
        self.assertEqual(r["produto_campeao"], "Monitor")


if __name__ == "__main__":
    unittest.main()
