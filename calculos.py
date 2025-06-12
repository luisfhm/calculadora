def calcular_tenencia(estado, anio, valor, hibrido, es_nuevo=True):
    """
    Calcula el monto de tenencia y refrendo dependiendo del estado, año, valor del vehículo,
    si es híbrido o eléctrico y si el auto es nuevo o no.
    
    Args:
        estado (str): Nombre del estado (e.g., "CDMX", "Edo. de México").
        anio (int): Año del vehículo.
        valor (float): Valor del vehículo en pesos.
        hibrido (bool): Si el vehículo es híbrido o eléctrico.
        es_nuevo (bool): Si el auto es nuevo (importante para aplicar el 3.1%).
        
    Returns:
        tuple: (monto_tenencia, monto_refrendo, mensaje)
    """
    refrendo = 800  # Monto fijo del refrendo
    tenencia = 0
    mensaje = ""

    estado = estado.strip().lower()

    if hibrido:
        mensaje = "Exento de tenencia por ser vehículo híbrido o eléctrico."
        return 0, refrendo, mensaje

    if estado == "cdmx":
        if es_nuevo and valor <= 613213:
            tenencia = valor * 0.031
            mensaje = "Tenencia calculada con tasa preferente del 3.1% para auto nuevo."
        else:
            # Suponemos una depreciación del 10% por año si no es nuevo
            antiguedad = 2025 - anio
            valor_depreciado = valor * (0.9 ** antiguedad)
            tenencia = valor_depreciado * 0.03
            mensaje = f"Tenencia calculada con depreciación para auto modelo {anio}."

        # Posible exención por subsidio si valor <= 250,000 y anio >= 2019
        if anio >= 2019 and valor <= 250000:
            return 0, refrendo, "Exento de tenencia por subsidio si cumples con los requisitos adicionales."

    elif estado in ["edo. de méxico", "estado de méxico"]:
        if anio >= 2021 and valor <= 400000:
            mensaje = "Exento de tenencia por programa Tenencia Cero (Edomex)."
            return 0, refrendo, mensaje
        else:
            tenencia = valor * 0.035
            mensaje = "Tenencia calculada con tasa del 3.5% para Edomex."

    else:
        tenencia = valor * 0.04
        mensaje = f"Tenencia calculada con tasa general del 4% para estado: {estado.title()}."

    return round(tenencia, 2), round(refrendo, 2), mensaje
