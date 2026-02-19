import streamlit as st


st.set_page_config(page_title="Machine Learning Portfolio", page_icon=":bar_chart:", layout="wide")

#st.title("Machine Learning Portfolio")
#st.write("Bem vindo ao meu portfólio de Aprendizado de Máquina! Aqui planejo colocar meus projetos e conhecimentos adquiridos sobre essa área ")
    
st.sidebar.title("Menu")
st.sidebar.write("Projetos e Exemplos Úteis")

projetos = {
    "Home": "home",
    "Regressão Linear": "regressao",
    "Classificação": "classificacao",
}

with st.sidebar:
    escolha = st.radio("Navegação", list(projetos.keys()))
if escolha == "Home":
    st.write("Bem vindo ao meu portfólio de Aprendizado de Máquina! Aqui planejo colocar meus projetos e conhecimentos adquiridos sobre essa área ")

elif escolha == "Regressão Linear":
    st.write("Aqui estão alguns projetos de Regressão Linear que desenvolvi:")
    st.markdown("- [Projeto 1: Previsão de Preços de Casas]")

elif escolha == "Classificação": 
    st.write("Aqui estão alguns projetos de Classificação que desenvolvi:")
    st.markdown("- [Projeto 1: Classificação de Imagens]")