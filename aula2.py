
import streamlit as st
import pandas as pd
import plotly.express as px

# --- Carregamento dos dados ---
uploaded_file = st.file_uploader("deputados_2022.csv", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # --- Filtro de Partido ---
    if 'partido' in df.columns:
        lista_partidos = df['partido'].unique().tolist()
        partido_selecionado = st.selectbox("Selecione o Partido:", options=lista_partidos)

        # Criando o DataFrame filtrado
        df_filtrado = df[df['partido'] == partido_selecionado]

        # --- Gráfico de Colunas ---
        st.subheader(f"Análise de Colunas: {partido_selecionado}")

        # Supondo que você queira contar quantos registros tem em cada 'cargo'
        # Você pode trocar 'cargo' por qualquer outra coluna do seu CSV
        coluna_x = 'cargo' 

        if coluna_x in df_filtrado.columns:
            fig_colunas = px.bar(
                df_filtrado, 
                x=coluna_x, 
                title=f"Quantidade por {coluna_x} no partido {partido_selecionado}",
                labels={coluna_x: "Categoria", "count": "Quantidade"},
                color=coluna_x # Isso dá uma cor diferente para cada coluna
            )

            # Exibir o gráfico
            st.plotly_chart(fig_colunas)
        else:
            st.warning(f"A coluna '{coluna_x}' não foi encontrada para gerar o gráfico.")
   
