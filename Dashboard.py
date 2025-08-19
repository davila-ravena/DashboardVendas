import pandas as pd
import matplotlib.pyplot as plt

# Função para salvar e mostrar gráfico
def salvar_grafico(fig, nome_arquivo):
    fig.savefig(nome_arquivo)
    plt.show()

# Carregar os dados
df = pd.read_csv("data/vendas.csv", parse_dates=["Data"])
df["Receita"] = df["Quantidade"] * df["Preco_Unitario"]

# 1️⃣ Vendas por Categoria
categoria = df.groupby("Categoria")["Receita"].sum()
fig1 = plt.figure(figsize=(6,6))
categoria.plot(kind="pie", autopct="%1.1f%%", shadow=True)
plt.title("Participação por Categoria")
salvar_grafico(fig1, "vendas_por_categoria.png")

# 2️⃣ Receita ao longo do tempo
receita_tempo = df.groupby("Data")["Receita"].sum()
fig2 = plt.figure(figsize=(8,5))
receita_tempo.plot(marker="o")
plt.title("Receita ao Longo do Tempo")
plt.xlabel("Data")
plt.ylabel("Receita (R$)")
plt.grid(True)
salvar_grafico(fig2, "receita_tempo.png")
