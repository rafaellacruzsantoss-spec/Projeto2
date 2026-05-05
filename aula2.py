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
 if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
 if 'partido' in df.columns:
        # Tudo aqui dentro deve estar alinhado na mesma coluna
        lista_partidos = df['partido'].unique().tolist()
        partido_selecionado = st.selectbox("Escolha o partido:", options=lista_partidos)
        
        # O FILTRO:
        df_filtrado = df[df['partido'] == partido_selecionado]

        # A LINHA QUE DEU ERRO: (Certifique-se que ela está alinhada com o df_filtrado)
        st.subheader(f"Distribuição para o {partido_selecionado}")
        
        # Gráfico...
        fig = px.pie(df_filtrado, names='sua_coluna_aqui')
        st.plotly_chart(fig) 
   
