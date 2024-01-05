import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# Com uma visão mensal
# Faturamento por mês e por unidade
# Tipo de produto mais vendido
# Desempenho das formas de pagamento
# Avaliação média por filial

df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Mês", df["Month"].unique())

df_filtered = df[df["Month"] == month]
df_filtered

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_date = px.bar(
    df_filtered, x="Date", y="Total", color="City", title="Faturamento por Mês"
)
col1.plotly_chart(fig_date)

fig_prod = px.bar(
    df_filtered, x="Date", y="Product line", color="City", title="Faturamento por tipo de produto", orientation="h"
)
col2.plotly_chart(fig_prod)

city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()

fig_city = px.bar(
    df_filtered, x="City", y="Total", title="Faturamento por filial"
)
col3.plotly_chart(fig_city)
