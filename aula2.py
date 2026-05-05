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
# --- CRIAÇÃO DO GRÁFICO DE PIZZA ---
    
    st.subheader(f"Distribuição para o {partido_selecionado}")

    # Pergunta: Qual coluna você quer contar para o gráfico? 
    # Exemplo: 'genero', 'cargo' ou 'estado'
    coluna_para_pizza = st.selectbox(
        "Ver proporção de:", 
        options=df_filtrado.columns
    )

    # Criando o gráfico com Plotly
    fig = px.pie(
        df_filtrado, 
        names=coluna_para_pizza, 
        title=f"Proporção de {coluna_para_pizza} no {partido_selecionado}",
        hole=0.3 # Opcional: transforma em gráfico de rosca
    )

    # Exibindo no Streamlit
   st.plotly_chart(fig)
