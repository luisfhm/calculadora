import streamlit as st
from interfaz import entrada_usuario, mostrar_resultados, pedir_email
from calculos import calcular_tenencia, reporte_tenencia  # Importa también la función reporte_tenencia

st.set_page_config(page_title="Calculadora de Tenencia 2025", page_icon="🚗")

st.title("🚗 Calculadora de Tenencia y Refrendo 2025")
st.markdown("Simula cuánto podrías pagar según tu estado, año y valor del vehículo.")

estado, anio_auto, valor_auto, es_hibrido = entrada_usuario()

if st.button("Calcular"):
    tenencia, refrendo, mensaje = calcular_tenencia(estado, anio_auto, valor_auto, es_hibrido)
    mostrar_resultados(tenencia, refrendo, mensaje)

    st.markdown("---")
    st.markdown("### Detalle del cálculo")
    texto_reporte = reporte_tenencia(estado, anio_auto, valor_auto, es_hibrido)
    st.markdown("### 📑 Reporte detallado de tenencia")
    st.markdown(texto_reporte, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### ❓ ¿Sabías que...")

    import random

    sabias_que = [
        "En la **CDMX**, si tu auto cuesta menos de $250,000 pesos y no tienes adeudos, puedes obtener un **subsidio del 100%** en la tenencia.",
        "Los autos **eléctricos** no pagan tenencia en casi ningún estado, pero sí deben cubrir el **refrendo**.",
        "El **refrendo vehicular** es un pago anual obligatorio aunque no debas tenencia.",
        "En algunos estados como **Querétaro**, los autos nuevos pagan menos tenencia el primer año por políticas locales.",
        "Los autos con más de 10 años de antigüedad pagan una **tenencia simbólica** o incluso están **exentos** en ciertos estados.",
        "Tener tu **tarjeta de circulación vigente** es requisito para acceder a subsidios en varios estados.",
    ]

    st.markdown("---")
    st.markdown("### ❓ ¿Sabías que…?")
    st.info(random.choice(sabias_que))




    st.markdown("---")
    st.markdown("¿Buscas seguro? [Cotiza con Rastreator.mx](https://www.rastreator.mx)")

pedir_email()
