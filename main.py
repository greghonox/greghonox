import streamlit as st


st.set_page_config(
    layout="wide",
    initial_sidebar_state="auto",
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
            ### 🤝🏿 My name is Gregorio Honorato.
            ### 👨🏿‍💻 I am a developer and I am passionate about technology.
            ### 💁🏿‍♂️ I will got talking about my experience and my skills.
            ### 🙋🏿‍♂️ This is me.
            ### 📚 My contacts is below page.
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
            * **Others:** HTML, CSS, Bootstrap, Pandas, Numpy, Matplotlib, Seaborn, Plotly, Streamlit, and many others.
            ---
            
            ### Projects and Links here:
            1. **Schedule in Django:** (https://github.com/greghonox/AGENDA)
            2. **Bank in Django:** (https://github.com/greghonox/BRASILPREV)
            3. **FastApi:** (https://github.com/greghonox/FASTAPIZERO)
            4. **TRF with Selenium:** (https://github.com/greghonox/TRF5)
            5. **Exercises with Crawler:** (https://github.com/greghonox/desafio-crawler)
            6. **Exercises with Django and unitary tests:** (https://github.com/greghonox/TOURHOUSE)
            7. **Many projects in my Github:** (https://github.com/greghonox)
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

st.page_link("pages/app.py", label="Sales Dashboard", icon="📊")
