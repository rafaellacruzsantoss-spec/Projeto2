import streamlit as st
import pandas as pd

st.title("Seletor de Colunas CSV")

# 1. Componente para o usuário subir o arquivo
uploaded_file = st.file_uploader("Envie seu arquivo CSV", type=["csv"])

if uploaded_file is not None:
    # 2. Ler o arquivo com pandas
    df = pd.read_csv(uploaded_file)
    
    # 3. Criar a lista de opções baseada nas colunas do DataFrame
    colunas = df.columns.tolist()
    
    # 4. Pedir ao usuário para escolher a variável
    variavel_escolhida = st.selectbox("Selecione a variável que deseja analisar:", options=colunas)
    
    # 5. Usar a variável escolhida
    st.write(f"Você selecionou a coluna: **{variavel_escolhida}**")
    st.write(df[variavel_escolhida])
df = pd.read_csv('deputados_2022.csv')
st.dataframe(df)
