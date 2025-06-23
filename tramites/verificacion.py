def info_verificacion(estado, tipo_auto):
    if estado == "CDMX":
        if tipo_auto == "Híbrido/Eléctrico":
            return "Los vehículos híbridos o eléctricos están exentos de verificación por 8 años en CDMX."
        else:
            return "Tu auto debe verificarse dos veces al año. Consulta tu calendario según el engomado."
    return "Consulta las fechas y requisitos en el sitio de tu gobierno estatal."
