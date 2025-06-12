def calcular_tenencia(estado, anio, valor, hibrido):
    """
    Calcula el monto de tenencia y refrendo dependiendo del estado, año, valor del vehículo y si es híbrido o no.
    
    Args:
        estado (str): Nombre del estado (e.g., "CDMX", "Edo. de México").
        anio (int): Año del vehículo.
        valor (float): Valor del vehículo en pesos.
        hibrido (bool): Si el vehículo es híbrido o eléctrico.
        
    Returns:
        tuple: (monto_tenencia, monto_refrendo, mensaje)
    """
    refrendo = 800  # Monto fijo de refrendo (puede ajustarse)
    tenencia = 0
    mensaje = ""

    estado = estado.strip().lower()

    if estado == "cdmx":
        if hibrido:
            mensaje = "Exento de tenencia por ser híbrido o eléctrico."
        elif anio >= 2019 and valor <= 250000:
            mensaje = "Exento de tenencia si cumples los requisitos (valor <= 250 mil y año >= 2019)."
        else:
            tenencia = valor * 0.03
    elif estado in ["edo. de méxico", "estado de méxico"]:
        if hibrido:
            mensaje = "Exento por auto verde (híbrido o eléctrico)."
        elif anio >= 2021 and valor <= 400000:
            mensaje = "Exento de tenencia por programa Tenencia Cero (valor <= 400 mil y año >= 2021)."
        else:
            tenencia = valor * 0.035
    else:
        # Otros estados: no hay exención, tasa general del 4%
        tenencia = valor * 0.04

    return round(tenencia, 2), round(refrendo, 2), mensaje
