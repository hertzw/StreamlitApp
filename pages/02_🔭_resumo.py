import streamlit as st
from st_aggrid import AgGrid

st.header("Resumo dos Dados")

if 'dados' not in st.session_state:
    st.error("Os dados não foram carregados")
else:
    dados = st.session_state['dados'].describe().reset_index()
    st.write(dados)