import streamlit as st

from pages.scripts import TeleGram
from pages.scripts import menu_app


st.title("Contato📩")
st.markdown(
    """
            ### Aqui você pode escrever sua mensagem e eu receberei em tempo real.
"""
)

msg_default = "Não esqueça de deixar seu contato para que eu possa responder..."
prompt = st.text_area("Escreva sua mensagem aqui:", placeholder=msg_default)
submit = st.button("Enviar", help="Clique para enviar a mensagem")

if prompt or submit:
    TeleGram(prompt)
    st.success(
        "Mensagem enviada para mim, de preferencia deixe seu contato para mim responder!"
    )

menu_app()
