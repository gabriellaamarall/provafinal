import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read("censo_1872.xlsx")
df = df.drop_duplicates()

st.set_page_config (page_title="Censo de 1872", layout="wide")

df = pd.DataFrame("censo_1872.xlsx")


df_filtrado = df[
    (df["ID"].isin(["id_provincia", "id_municipio"])) &
    (df["LIVRES"] == "")
].copy()

df_tabela = df_filtrado[["NOMEUP", "ANO", "IQVU"]]


st.title("Censo de 1872, População livre e população escravizada")

st.sidebar.header("Controles")
opcao = st.sidebar.radio("Selecione a visualização:", ["Tabela", "Gráficos"])

if opcao == "Tabela":
    st.header("Tabela do IQVU (Série Histórica)")
    st.dataframe(df_tabela, use_container_width=True, hide_index=True)

elif opcao == "Gráficos":
    st.header("Gráficos do IQVU — id e Santa Inês")

st.subheader("1. Gráfico de Linha — id")
df_id= df_tabela[df_tabela["NOMEUP"] == "id"]

fig_linha_id = px.line(
        df_id,
        x="ANO",
        y="IQVU",
        markers=True,
        title="Evolução do IQVU — id (1994 a 2016)",
        template="plotly_dark"
    )
fig_linha_id.update_traces(line_color="#FF6B6B", line_width=3, marker_size=8)
fig_linha_id.update_xaxes(type="category")
fig_linha_id.update_layout(paper_bgcolor="#111827", plot_bgcolor="#111827")
st.plotly_chart(fig_linha_id, use_container_width=True)