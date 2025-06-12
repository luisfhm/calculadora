def calcular_tenencia(estado, anio, valor, hibrido):
    refrendo = 800  # Base fija (ejemplo)
    tenencia = 0

    if estado == "CDMX":
        if anio >= 2019 and valor <= 250000 and not hibrido:
            return 0, refrendo, "Exento de tenencia si cumples los requisitos."
        elif hibrido:
            return 0, refrendo, "Exento de tenencia por ser híbrido o eléctrico."
        else:
            tenencia = valor * 0.03
    elif estado == "Edo. de México":
        if anio >= 2021 and valor <= 400000 and not hibrido:
            return 0, refrendo, "Exento por programa Tenencia Cero."
        elif hibrido:
            return 0, refrendo, "Exento por auto verde."
        else:
            tenencia = valor * 0.035
    else:
        tenencia = valor * 0.04

    return round(tenencia, 2), round(refrendo, 2), ""
