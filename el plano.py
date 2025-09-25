import streamlit as st

#Para el titulo y una imagen con descripcion
st.header("Plano: Copia a tu derecha")
st.image("Plano.png", caption="Balatro: Plano")

#Dividir con una linea
st.divider()

#Generar el texto de la informacion
st.write(
"""
**Plano** es un cómodin raro que copia el efecto del comodín que esta a su derecha. No todos los comodines don compatibles con Plano, como este no puedo copiar "efectos pasivos", aunque el propio Plano sí es compatible. La compatibilidad de Plano con otros Comodines puede verse en su descripción emergente. Se desbloquea ganando una partida. Su precio de compra es de 10 y su precio de venta es de 5.

**En general, Plano no copiará los siguientes efectos:**

• Cualquier cosa que se active al final de una ronda (Ejemplo:  Comodín Dorado)

• Comodines debilitados

• Efectos de Ediciones de cartas

• Efectos de Stickers

• Destrucción

• Escalado de comodines (solo se copia el resultado final)

• Cambios en las manos, descartes, tamaño de la mano o tipo de mano (Excepto  Ladrón, que se activa después de que se inicie la ciega)

• Efectos pasivos (como  Chicot o  Pareidolia)
"""
   )

#Dividir con una linea
st.divider()

#Generar el texto de la informacion
st.write(
"""
**Hay un total de 9 comodines que son incompatibles con Plano:**

• Cuatro dedos

• Caos el payaso

• Pareidolia

• Máscara de Midas

• Comodín dorado

• Sr.huesos

• Solo seises

• Comodin invisible

• Chicot
"""
   )