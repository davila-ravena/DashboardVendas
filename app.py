import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Título do Dashboard
st.title("📊 Dashboard de Vendas")

# Carregar dados
df = pd.read_csv("data/vendas.csv", parse_dates=["Data"])
df["Receita"] = df["Quantidade"] * df["Preco_Unitario"]

# Filtros interativos
categorias = df["Categoria"].unique()
categoria_selecionada = st.multiselect("Selecione a categoria:", categorias, default=categorias)

df_filtrado = df[df["Categoria"].isin(categoria_selecionada)]

# Receita total
st.subheader("Receita Total")
st.write(f"R$ {df_filtrado['Receita'].sum():,.2f}")

# Gráfico: Receita ao longo do tempo
st.subheader("Receita ao longo do tempo")
receita_tempo = df_filtrado.groupby("Data")["Receita"].sum()
fig1, ax1 = plt.subplots()
receita_tempo.plot(marker="o", ax=ax1)
ax1.set_ylabel("Receita (R$)")
ax1.set_xlabel("Data")
ax1.grid(True)
st.pyplot(fig1)

# Gráfico: Participação por categoria
st.subheader("Participação por Categoria")
categoria_sum = df_filtrado.groupby("Categoria")["Receita"].sum()
fig2, ax2 = plt.subplots()
categoria_sum.plot(kind="pie", autopct="%1.1f%%", shadow=True, ax=ax2)
ax2.set_ylabel("")
st.pyplot(fig2)

