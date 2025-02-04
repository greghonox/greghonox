import streamlit as st


def menu_app():
    st.divider()
    generate_button = "https://img.shields.io/badge"
    content = f"""
    ## List of Applications
    
    [![Find Jobs]({generate_button}/busca-emprego-red?style=flat&logo=framework)](busca_emprego)👈🏿 Busca de empregos...
    
    [![News Now]({generate_button}/news_now-cnn-yellow?style=flat&logo=cnn)](news_now_cnn)👈🏿 Noticias da CNN...
    
    [![Dash Boards]({generate_button}/dash-boards-pink?style=flat&logo=streamlit)](dashboards)👈🏿 Alguns aplicativos com dashboard...

    [![Call Me]({generate_button}/call-me-blue?style=flat&logo=telegram&)](call_me)👈🏿  Pode me chamar clicando ai...    
    
    [![About]({generate_button}/about-me-red?style=flat&logo=rubocop)](/)👈🏿 Sobre o autor e seu curriculo...    
    """
    st.write(content, unsafe_allow_html=True)
