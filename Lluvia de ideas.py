import streamlit as st

#Para el titulo y una imagen con descripcion
st.header("Luvia de ideas: Copia al extremo izquierda")
st.image("Lluvia_de_ideas.png", caption="Balatro: Lluvia de ideas")

#Generar el texto de la informacion
st.write(
"""
**Lluvia de ideas** es un comodín de efecto raro que copia la habilidad del comodín mas a la izquierda. A diferencia de  Plano, Lluvia de ideas no cambiara que cosa copia, solo cuando lo copia. Para cambiar a que comodín le copia, es necesario mover otro comodín a la posición más a la izquierda. Hay algunos comodines que no se pueden copiar, y poner a Lluvia de ideas en la posición más a la izquierda no hará nada. Si Plano esta en la posición más a la izquierda, Lluvia de ideas copiara al mismo comodín que este copiando Plano. Se puede ver que comodines son combatibles con Lluvia de ideas en su descripción. Se desbloquea descartando una mano real en una partida. Tiene un precio de compra de 10 base y un precio de venta de 5 base.

En general, Lluvia de ideas no copiará los siguientes efectos:

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
**Sinergias**

• Barajas:
Lluvia de ideas funciona bien en cualquier baraja.

• Manos de Póker:
Este comodín no sinergiza directamente con ninguna mano.

• Comodines:
Debido a las diferentes formas en que copia una carta, Lluvia de ideas siempre estará a la sombra de Plano, pero no por mucho. El principal escenario en el que Lluvia de ideas es peor es que los comodines XMulti(Como  Cavendish o  Plantilla de comodín) deben colocarse completamente a la izquierda para que Lluvia de ideas los copie, lo que significa que el jugador no puede multiplicar dos veces el multi de comodines escalables como  Supernova. Por ejemplo, Supernova + Plano + El trío puntuará más que Supernova + Lluvia de ideas + El trío. Sin embargo, una Lluvia de ideas con polícroma en el extremo derecho puede copiar un comodín sin perder el beneficio completo de su efecto de edición, aunque Lluvia de ideas en sí mismo no puede copiar efectos de edición. Algunos objetivos destacados para copiar son los comodines que generan dinero a mitad de ronda, como  Reembolso por correo, los comodines que se reactivan, como  Atardecer, y los comodines XMulti, como  Barón,  Fotografía o  Heliotropo. Cuando se combinan varias copias con  Barón y  Mimo, mientras se utiliza  Baraja plasmática, los jugadores pueden alcanzar la elusiva puntuación Naneinf.

Aunque no funcionará con ellos, los comodines como  Comodín borroso y  Cuatro dedos se pueden utilizar para desbloquear Lluvia de ideas más fácilmente.
"""
   )
   
#Dividir con una linea
st.divider()

#Generar el texto de la informacion
st.write(
"""
**Antisinergias**

Hay un total de 9 comodines que son incompatibles con Plano:

• Cuatro dedos

• Caos el payaso

• Pareidolia

• Máscara de Midas

• Comodín dorado

• Sr.huesos

• Solo seises

• Comodin invisible

• Chicot

**Ciegas**:
 Bellota ambarina: Esta ciega voltea y baraja los comodines, lo que puede hacer que Lluvia de ideas copie el comodín equivocado o que no copie nada si se mueve a la posición más a la izquierda, al menos durante una mano.
"""
    )

#Dividir con una linea
st.divider()

#Generar el texto de la informacion
st.write(
"""
**Curiosidades**

• Si se copia al  Plano, Lluvia de ideas copiará el efecto que esté copiando el Plano, no el Plano en sí.

• En la ilustración, el adorno más a la izquierda del sombrero, el ojo más a la izquierda y el adorno más a la izquierda de la parte inferior están resaltados de alguna manera, en referencia a cómo Lluvia de ideas copia el Comodín más a la izquierda.

• La ilustración de la carta muestra un boceto desordenado hecho "en la parte trasera de una servilleta", un cálculo aproximado o una idea dibujada rápidamente durante una conversación en un bar o restaurante, lo que podría interpretarse como la concepción del comodín se esta copiando. Esto también refleja sus limitaciones en comparación con Plano, que muestra un dibujo técnico más deliberado y detallado.

• Este es el único comodín que tiene una esquina de 90 grados (arriba a la izquierda) en el diseño de la carta, ya que todos los demás comodín tienen una punta redondeada en todas sus esquinas.
"""
   )