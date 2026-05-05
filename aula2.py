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
# Criando o gráfico de pizza
        # Troque 'cargo' pelo nome da coluna que você quer ver no gráfico
        fig = px.pie(df_filtrado, names='partidos', title=f"Divisão por partidos: {escolha}")
        st.plotly_chart(fig)
        
    else:
        st.error("Erro: Não achei uma coluna chamada 'partido' no seu arquivo.")
   
