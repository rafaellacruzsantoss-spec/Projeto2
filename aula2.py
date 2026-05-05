
st.title("Filtro de Partidos Políticos")

# 1. Upload do arquivo
uploaded_file = st.file_uploader('deputados_2022.csv', type="csv")

if uploaded_file is not None:
    # Ler o CSV
    df = pd.read_csv(uploaded_file)
    
    # 2. Criar o seletor com os partidos únicos da coluna 'partido'
    # Substitua 'partido' pelo nome exato da coluna no seu CSV
    if 'deputados_2022.csv' in df.columns:
        lista_partidos = df['partido'].unique().tolist()
        
        partido_selecionado = st.selectbox(
            "Selecione o partido para filtrar:",
            options=lista_partidos
        )

        # 3. FILTRAGEM: Criar um novo DataFrame apenas com o partido escolhido
        df_filtrado = df[df['partido'] == partido_selecionado]

        # 4. Mostrar o resultado
        st.subheader(f"Dados apenas do partido: {partido_selecionado}")
        st.write(f"Total de registros encontrados: {len(df_filtrado)}")
        st.dataframe(df_filtrado)
        
        csv_filtrado = df_filtrado.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Baixar dados filtrados (CSV)",
            data=csv_filtrado,
            file_name=f"dados_{partido_selecionado}.csv",
            mime="text/csv",
        )
    else:
        st.error("A coluna 'partido' não foi encontrada no arquivo. Verifique o nome da coluna.")
