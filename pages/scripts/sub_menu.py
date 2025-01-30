import streamlit as st


def menu_app():
    st.divider()
    generate_button = "https://img.shields.io/badge"
    content = f"""
    ## List of Applications
    [![Call Me]({generate_button}/call-me-blue)](call_me)
    [![Find Jobs]({generate_button}/busca-emprego-red)](busca_emprego)
    [![News Now]({generate_button}/news_now-cnn-yellow)](news_now_cnn)
    [![Dash Boards]({generate_button}/dash-boards-pink)](dashboards)
    [![Aboult]({generate_button}/sobre-red)]()    
    """
    st.write(content, unsafe_allow_html=True)
