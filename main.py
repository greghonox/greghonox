import streamlit as st


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

col1, col2 = st.columns(2)

with col1:
    st.image("img/my.png", width=600)
with col2:
    st.markdown(
        """
            # Welcome! You be view my Resume 📄
            ### My name is Gregorio Honorato
            ### I am a developer and I am passionate about technology.
"""
    )

st.markdown(
    """
            ---
            ### Skills:
            * **Languages Favorite :** Python, SQL, JavaScript
            * **Frameworks:** Django, Flask, FastAPI, Selenium, Pytest, and many others.
            * **Tools:** Git, Docker, Gcp, Heroku
            * **Databases:** PostgreSQL, MongoDB, Mysql, Sqlite
            ---
            
            ### Projects and Links here:
            1. **asdfasdfasdfasd
            2. **asdfasdfasdfasd
            3. **asdfasdfasdfasd
            ---
            
            ### Call me:
            * 📫**Email:** greghono@gmail.com
            * 🪪**LinkedIn:** (https://www.linkedin.com/in/gregorio-honorato-78803989/)
            * 📱**Whatsapp:** (https://web.whatsapp.com/send/?phone=5519992509913).
            * 📻**Telegram:** (https://t.me/greghono)
            ---
            * **Soft skills:** I liked squad worked, i am very communication, solved problems.
"""
)
