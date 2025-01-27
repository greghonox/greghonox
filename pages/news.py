import streamlit as st
import pandas as pd
from pages.scripts import NewCNNBrasil


st.title("Solicitação de Dados📩")
st.markdown(
    """
    #### Aqui você pode solicitar alguns dados externos, abaixo esta alguns link para conferir os dados que estão sendo usados.
    ---
    ### Link que estão sendo usados:
    - [Politica no CNN Brasil](https://www.cnnbrasil.com.br/politica/)
    
    ---    
    """
)


def get_news_cnn_brasil():
    return NewCNNBrasil().show_news()


if st.button("Solicitar ultimas mensagens do grupo de vagas no telegram..."):
    with st.spinner("Buscando dados..."):
        news = get_news_cnn_brasil()
    for item in news:
        st.markdown(
            f"""
            <div style="display: flex; align-items: center; margin-bottom: 20px;">
                <img src="{item['thumbnail']}" width="100" style="margin-right: 20px;">
                <div>
                    <a href="{item['link']}" target="_blank"><h5>{item['content']}</h5></a>
                    <p>{item['date']}</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.success("Dados carregados com sucesso!")
