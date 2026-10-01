"""Gera um CSV de vendas FICTÍCIAS para a análise (os dados não são reais).

A semente fixa (seed) faz o resultado ser sempre o mesmo.
"""
import csv
import random
from datetime import date, timedelta

random.seed(42)
PRODUTOS = {"Notebook": 3500, "Mouse": 60, "Teclado": 120, "Monitor": 900, "Headset": 200}
REGIOES = ["Sudeste", "Sul", "Nordeste", "Centro-Oeste"]

with open("vendas.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["data", "produto", "regiao", "quantidade", "preco_unitario"])
    inicio = date(2025, 1, 1)
    for dia in range(365):
        for _ in range(random.randint(1, 4)):
            produto = random.choice(list(PRODUTOS))
            escritor.writerow([
                (inicio + timedelta(days=dia)).isoformat(),
                produto,
                random.choice(REGIOES),
                random.randint(1, 5),
                PRODUTOS[produto],
            ])
print("vendas.csv gerado.")
