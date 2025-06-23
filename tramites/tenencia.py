def calcular_tenencia(estado, anio, valor, hibrido):
    """
    Calcula el monto de tenencia y refrendo de un vehículo en función del estado, año, valor y tipo.

    Parámetros:
        estado (str): Estado del vehículo ("CDMX", "Edo. de México", etc.)
        anio (int): Año del vehículo
        valor (float): Valor del vehículo en pesos mexicanos
        hibrido (bool): True si el vehículo es híbrido o eléctrico

    Retorna:
        tupla: (tenencia, refrendo, mensaje explicativo)
    """
    refrendo = 800  # Costo base aproximado del refrendo
    tenencia = 0
    mensaje = ""

    if estado == "CDMX":
        if hibrido:
            mensaje = "Vehículos híbridos o eléctricos están exentos de tenencia en CDMX, pero deben pagar refrendo."
            return 0, refrendo, mensaje
        elif valor <= 250000:
            mensaje = (
                "Podrías ser exento de tenencia en CDMX si cumples con los requisitos administrativos: "
                "ser persona física, sin adeudos, tarjeta de circulación vigente y pagar refrendo antes del 31 de marzo."
            )
            return 0, refrendo, mensaje
        else:
            tenencia = valor * 0.031  # 3.1% del valor del auto si no hay subsidio
            mensaje = "Tenencia calculada como 3.1% del valor del vehículo por no cumplir con requisitos de subsidio en CDMX."

    elif estado == "Edo. de México":
        if hibrido:
            mensaje = "Vehículos híbridos o eléctricos están exentos de tenencia en Edo. de México, pero deben pagar refrendo."
            return 0, refrendo, mensaje
        elif anio >= 2021 and valor <= 400000:
            mensaje = (
                "Podrías estar exento de tenencia en Edo. de México si cumples con los requisitos del programa Tenencia Cero."
            )
            return 0, refrendo, mensaje
        else:
            tenencia = valor * 0.035  # 3.5%
            mensaje = "Tenencia calculada como 3.5% del valor del vehículo en Edo. de México."

    else:
        # Regla general si no es CDMX ni EdoMex
        tenencia = valor * 0.04  # 4% como aproximación
        mensaje = "Tenencia estimada como 4% del valor del vehículo (valor aproximado para otros estados)."

    return round(tenencia, 2), round(refrendo, 2), mensaje


def reporte_tenencia(estado, anio, valor, hibrido):
    tenencia, refrendo, mensaje = calcular_tenencia(estado, anio, valor, hibrido)

    tipo_auto = "Híbrido/Eléctrico" if hibrido else "Convencional"
    estado = estado.upper()

    reporte = f"""
📋 **Resumen del Cálculo de Tenencia y Refrendo 2025**

🔹 **Estado:** {estado}
🔹 **Año del vehículo:** {anio}
🔹 **Valor aproximado:** ${valor:,.2f} MXN
🔹 **Tipo de vehículo:** {tipo_auto}

---

💵 **Cálculo estimado:**

- **Tenencia a pagar:** ${tenencia:,.2f} MXN
- **Refrendo a pagar:** ${refrendo:,.2f} MXN

---

📌 **Notas y consideraciones:**

{mensaje}

- El pago de tenencia suele realizarse entre **enero y marzo** de cada año.
- El **refrendo** es un pago anual obligatorio, incluso si no se paga tenencia.
- Algunos estados ofrecen **subsidios o exenciones** si estás al corriente y cumples requisitos.
- Esta herramienta es solo una estimación basada en criterios generales.

👉 Verifica siempre con el sitio oficial de tu estado.
"""
    return reporte.strip()

