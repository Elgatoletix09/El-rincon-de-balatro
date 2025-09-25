import streamlit as st

#Para el titulo, un icono decorativo y un texto abajo
st.title("El rincón de balatro")
st.badge("Casual", color="green", icon=":material/chevron_right:")
st.write("Balatro no es un juego, es un estilo de vida")

#Otro mini titulo y generar una imagen
st.image("balatro-1.png", caption="Balatro")
st.header("Resumen", divider=True)

#Dividir con una linea
st.divider()

st.write(
"""
**Musica**

Tema principal de balatro para reproducir y escuchar

Balatro: **Main Theme**
"""
   )

st.video("Balatro Main Theme.mp3")

st.divider()
#Generar el texto de la informacion
st.write(
"""
**Balatro:**

Balatro es un videojuego que ha capturado la atención de los jugadores por su innovadora mezcla de géneros. A primera vista, parece un simple juego de póker, pero rápidamente se revela como un adictivo "roguelike de construcción de mazos". Esto significa que cada partida es única y el progreso se basa en la adquisición y combinación de cartas para crear sinergias cada vez más poderosas. El objetivo principal es superar una serie de rondas llamadas "ciegas", logrando un puntaje determinado con las manos de póker que vayas formando.

**¿De qué se trata?**

En Balatro, no solo se trata de formar las mejores manos de póker tradicionales. El verdadero giro del juego se encuentra en las cartas especiales, como los Jokers (Comodines), que otorgan efectos únicos, las cartas de Tarot y las cartas Planetarias, que te permiten mejorar tu baraja y potenciar la puntuación de tus manos. Con el dinero que ganas al superar cada ciega, puedes comprar y mejorar estas cartas, lo que te permite crear combos cada vez más extravagantes y poderosos. La clave está en la experimentación y en encontrar las sinergias correctas para "romper" el juego y alcanzar puntuaciones astronómicas. El juego termina al superar un número de rondas, pero puedes seguir jugando en el modo infinito.

**Algunas caracteristicas sobre el videojuego**

Creador: El juego fue desarrollado por una sola persona bajo el seudónimo de LocalThunk.

Fecha de lanzamiento: Balatro se lanzó el 20 de febrero de 2024 para Microsoft Windows, Nintendo Switch, PlayStation 4, PlayStation 5, Xbox One y Xbox Series X/S. Posteriormente, se lanzó para macOS el 1 de marzo de 2024 y para Android e iOS el 26 de septiembre de 2024.

Género: Es una mezcla de géneros que incluye "roguelike", "deck-building" (construcción de mazos) y juego de cartas.

Estilo artístico: Cuenta con un atractivo estilo retro de pixel art que evoca la estética de los monitores CRT, acompañado de una relajante banda sonora.

Rejugabilidad: Gracias a la gran variedad de comodines, mazos y modificadores, cada partida es completamente diferente, lo que lo convierte en un juego extremadamente rejugable.
"""
   )

st.divider()
st.write(
"""
Aqui un tutorial muy util para entender lo mas basico del videojuego:
"""
   )
st.video("https://youtu.be/mEl06UfPtw4")

#Dividir con una linea y crear dos columnas, cada unba con una imagen y una descripcion
st.divider()
col1, col2 = st.columns(2)
col1.image("new_project_-_2024-02-14t133713.png", caption="Update and new image: 1 millon de copias vedidas")
col2.image("OIP (2).png", caption="Imagen variante")

#Dividir con una linea
st.divider()

#Generar el texto de la informacion
st.write(
"""
• 📚 El Rincón de Balatro

• En este espacio se habla de todo tipo de temas, pero principalmente encontrarás información útil relacionada con:

• 🃏 Comodines

• 🌌 Cartas de Planeta

• 🔮 Cartas del Tarot

• ✨ Efectos especiales y mecánicas del juego

Además, se irán añadiendo páginas con detalles, consejos y explicaciones para ayudarte a entender mejor el juego y mejorar tu estrategia.
"""
   )