import streamlit as st

#Para el titulo y una imagen con descripcion
st.title("¿Quienes somos?")
st.image("Imagenmemebalatro.png", caption="Meme de balatro")

st.divider()

st.write(
"""
Mi nombre es **Balatro Balatrez** y soy el creador de esta pagina, tengo 8πα años, ¡gracias por llegar hasta aqui!

¡Si tienes alguna **Sugerencia** no dudes en contactar al creador de esta pagina!

E-mail:g7842813@gmail.com

Direccion: Condado de Lincoln, Nevada

Mis coordenadas: 37°14′06″N, 115°48′40″O

¡Si no me encuentras ahi por favor viajar hasta este otro lugar!

direccion 2: Timbuctú, Tombuctú en Mali.

Mis coordenadas: 23°04′47′′N, 12°36′00′′W
"""
   )

st.divider()

col1, col2 = st.columns(2)
col1.image("Horadebalatro.png", caption="Meme de balatro")
col2.image("salebalatro.png", caption="Meme de balatro")