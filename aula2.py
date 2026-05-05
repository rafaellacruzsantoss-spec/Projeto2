import streamlit as st
import pandas as pd
st.title("Política Aplicada")
df = pd.read_csv('deputados_2022.csv')

sigla = st.text_input('Digite a sigla do partido')
uf = st.text_input('Digite a UF')

if sigla:
    df_filtrado = df[df['partido']==sigla.upper()]
else:
    df_filtrado = df

if uf:
    df_filtrado = df_filtrado[df_filtrado["uf"] == uf.upper()]

st.dataframe(df_filtrado)

st.subheader("Gráfico Geral de candidatos por partido")

grafico = df['partido'].value_counts()

st.bar_chart(grafico)

