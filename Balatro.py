import streamlit as st

#Para generar el titulo, el icono y centrarlo
st.set_page_config(
    page_title="El Rincón de Balatro ",
    page_icon=":red_heart:",
    layout="centered",
)
#Al cargar este archivo se cargan todos los demas y empieza a funcionar
pg = st.navigation(["homepage.py", "el plano.py", "Lluvia de ideas.py", "Triboulet.py", "Chicot.py", "Quienesbalatrobalatrez.py"])
pg.run()