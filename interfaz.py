import streamlit as st
from db import guardar_email


def mostrar_resultados(tenencia, refrendo, mensaje):
    st.subheader("💰 Resultados")
    st.write(f"**Tenencia estimada:** ${tenencia:,.2f} MXN")
    st.write(f"**Refrendo estimado:** ${refrendo:,.2f} MXN")
    if mensaje:
        st.info(mensaje)

def entrada_usuario():
    estado = st.selectbox("Selecciona tu estado", [
        "CDMX", "Edo. de México", "Jalisco", "Nuevo León", "Querétaro", "Otro"
    ])

    anio_auto = st.number_input("¿De qué año es tu auto?", min_value=2000, max_value=2025, value=2020)
    valor_auto = st.number_input("Valor aproximado del auto (MXN)", min_value=10000, value=200000, step=1000)
    es_hibrido = st.checkbox("¿Tu auto es híbrido o eléctrico?")

    return estado, anio_auto, valor_auto, es_hibrido

def pedir_email():
    st.subheader("📩 Recibe un recordatorio anual")
    email = st.text_input("Déjanos tu correo electrónico:")
    if st.button("Guardar correo"):
        if "@" in email and "." in email:
            if guardar_email(email):
                st.success("Correo guardado con éxito, ¡gracias!")
            else:
                st.error("Error guardando el correo, intenta más tarde.")
        else:
            st.error("Por favor ingresa un correo válido.")
