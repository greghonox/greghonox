import streamlit as st
from pages.scripts import JobCampinas

st.title("💻Busca de Emprego 🏢")
st.title("Vou te ajudar a buscar emprego! 🚀")
st.divider()

left, right = st.columns(2, vertical_alignment="bottom")

job = left.text_input(
    "Escreva o cargo que deseja buscar:", placeholder="motorista, vendedor, etc..."
)
submit_button = right.button("Buscar Emprego")

if submit_button:
    search_job = JobCampinas(job)
    for page in range(2):
        search_job.navigate_jobs(page)
    if search_job.job_listings:
        st.dataframe(search_job.job_listings)
    st.success("A sua buscar terminou com sucesso !!!")
