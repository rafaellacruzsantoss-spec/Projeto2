import streamlit as st
import pandas as pd

df = pd.read_csv('deputados_2022.csv')
st.dataframe(df)
colunas_selecionadas = st.multiselect("Escolha as variáveis:", options=colunas)
if colunas_selecionadas:
    st.dataframe(df[colunas_selecionadas])
