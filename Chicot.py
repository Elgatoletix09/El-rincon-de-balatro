import streamlit as st

#Para el titulo y una imagen con descripcion
st.header("El plano: Desactiva todos los efectos de las Ciegas Jefes al seleccionarlo")
st.image("Chicot.png", caption="Balatro: Chicot")

#Dividir con una linea
st.divider()

#Generar el texto de la informacion
st.write(
"""
**Chicot** es uno de los cinco Joker legendarios. Chicot desactiva todos los efectos de Ceguera de Jefe al seleccionarlo, haciendo que el jefe ciego sea simplemente una ceguera regular con una puntuación base más alta para despejar. Los Jokers legendarios solo se pueden obtener de la Carta Espectral del Alma, que tiene una pequeña probabilidad de aparecer en los Paquetes de Refuerzo Espectrales y de Arcana. No se puede encontrar en la tienda y su precio de venta es de 10. Es compatible con los efectos de los pozos y no es copiable por Lluvia de ideas o Plano.
"""
   )

#Dividir con una linea
st.divider()

#Generar el texto de la informacion
st.write(
"""
**Sinergias**

• Mazos: Cualquier mazo puede beneficiarse de Chicot, aunque el Mazo Pintado puede ser más difícil de utilizar debido a la penalización de -1 en la ranura del Joker.

• Manos de poker: Cualquier mano de póker puede beneficiarse de Chicot, pero el Color se beneficia más, ya que algunos jefes ciegos debilitan un palo entero, incluyendo cualquier carta comodín.

• Jokers: Siendo un Joker de utilidad, Chicot no sinergiza directamente con ningún otro Joker. Tiene anti-sinergia con Luchador, porque ambos deshabilitan los ciegos de los jefes, aunque Luchador solo puede hacerlo una vez. También hace que Matador sea inútil, ya que ya no hay ningún efecto que activar. Una segunda copia de Chicot en realidad hace que algunos Ciegos de Jefe tengan un efecto positivo (escala con múltiples copias):

• La Pared: la puntuación ahora se reduce (tamaño del ciego pequeño)
• El Agua: duplica los descartes
• La Manilla: +1 tamaño de mano (Este efecto es permanente)
• La Aguja: ganar manos
• Vaso Violeta: la puntuación ahora se reduce aún más (2/3 del ciego pequeño) Sin embargo, como el efecto de Chicot no puede ser duplicado por Blueprint o Brainstorm, esto es extremadamente raro. (Esta característica puede ser en realidad un error, y podría ser corregido en el futuro.)

• Vales: Chicot hace obsoletas las versiones del Director y el Retcon al desactivar todos los efectos de los Boss Blinds. Sin embargo, con múltiples copias de Chicot, puede valer la pena volver a lanzar el Boss Blind para obtener un efecto positivo, especialmente considerando los 'errores positivos' mencionados anteriormente, como el incremento permanente en el tamaño de la mano de 'La Manacle'.
"""
   )