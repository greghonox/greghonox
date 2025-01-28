import streamlit as st
from pages.scripts import TeleGram

st.title("Contato📩")
st.markdown(
    """
            ### Aqui você pode escrever sua mensagem e eu receberei em tempo real.
"""
)

msg_default = "Não esqueça de deixar seu contato para que eu possa responder..."
prompt = st.chat_input("Escreva algo que receberei no telegram..." + msg_default)
if prompt:
    TeleGram(prompt)
    st.success("Mensagem enviada com sucesso!")
