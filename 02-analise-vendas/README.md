# Análise de vendas com Python (pandas + matplotlib)

Lê um CSV de vendas, calcula indicadores e gera gráficos.
**Os dados são fictícios**, criados pelo script `gerar_dados.py` só para estudo.

**O que pratica:** leitura e limpeza de dados, agrupamentos (`groupby`), indicadores
(faturamento, ticket médio, produto campeão) e visualização.

## Como rodar
```bash
pip install -r requirements.txt
python gerar_dados.py      # cria vendas.csv
python analise.py          # imprime os indicadores e salva os gráficos (.png)
python -m unittest -v      # testes
```

## Ideias para evoluir
Usar dados reais (por exemplo, séries do Banco Central), comparar regiões, montar o
mesmo painel no Power BI e documentar as medidas.
