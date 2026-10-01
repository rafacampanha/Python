"""Análise de vendas com pandas e matplotlib.

Passos: ler os dados -> limpar -> calcular -> gerar gráficos.
Antes, gere os dados:  python gerar_dados.py
"""
import pandas as pd
import matplotlib

matplotlib.use("Agg")  # salva as imagens sem abrir janela
import matplotlib.pyplot as plt


def carregar(caminho="vendas.csv"):
    """Lê o CSV, converte a data e cria a coluna de faturamento."""
    df = pd.read_csv(caminho, parse_dates=["data"])
    df = df.dropna()  # remove linhas incompletas
    df["faturamento"] = df["quantidade"] * df["preco_unitario"]
    df["mes"] = df["data"].dt.to_period("M").astype(str)
    return df


def resumo(df):
    """Devolve indicadores simples (KPIs)."""
    return {
        "faturamento_total": float(df["faturamento"].sum()),
        "ticket_medio": float(df["faturamento"].mean()),
        "itens_vendidos": int(df["quantidade"].sum()),
        "produto_campeao": df.groupby("produto")["faturamento"].sum().idxmax(),
    }


def grafico_mensal(df, saida="faturamento_mensal.png"):
    mensal = df.groupby("mes")["faturamento"].sum()
    ax = mensal.plot(kind="bar", color="#4a7c59", figsize=(10, 5))
    ax.set_title("Faturamento por mês")
    ax.set_xlabel("Mês")
    ax.set_ylabel("R$")
    plt.tight_layout()
    plt.savefig(saida)
    plt.close()


def grafico_produto(df, saida="faturamento_produto.png"):
    por_produto = df.groupby("produto")["faturamento"].sum().sort_values()
    ax = por_produto.plot(kind="barh", color="#6695A3", figsize=(8, 4))
    ax.set_title("Faturamento por produto")
    ax.set_xlabel("R$")
    plt.tight_layout()
    plt.savefig(saida)
    plt.close()


if __name__ == "__main__":
    dados = carregar()
    for nome, valor in resumo(dados).items():
        print(f"{nome}: {valor:,.2f}" if isinstance(valor, float) else f"{nome}: {valor}")
    grafico_mensal(dados)
    grafico_produto(dados)
    print("Gráficos salvos: faturamento_mensal.png e faturamento_produto.png")
