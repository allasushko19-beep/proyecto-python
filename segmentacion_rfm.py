# Proyecto 05 · Motor de Segmentación de Clientes (RFM Simplificado)
# Ala Sushko

clientes_rfm = [
{"cliente_id": "CL01", "nombre": "Ana Silva", "frecuencia_compras": 15,
"gasto_total": 2400.0, "dias_ultima_compra": 5},
{"cliente_id": "CL02", "nombre": "Luis Gomez", "frecuencia_compras": 8,
"gasto_total": 950.0, "dias_ultima_compra": 20},
{"cliente_id": "CL03", "nombre": "Carla Ruiz", "frecuencia_compras": 12,
"gasto_total": 1850.0, "dias_ultima_compra": 110},
{"cliente_id": "CL04", "nombre": "Pedro Diaz", "frecuencia_compras": 1,
"gasto_total": 45.0, "dias_ultima_compra": 240},
{"cliente_id": "CL05", "nombre": "Elena Mora", "frecuencia_compras": 2,
"gasto_total": 180.0, "dias_ultima_compra": 12},
{"cliente_id": "CL06", "nombre": "Jorge Pino", "frecuencia_compras": 9,
"gasto_total": 1100.0, "dias_ultima_compra": 95},
{"cliente_id": "CL07", "nombre": "Sofia Lara", "frecuencia_compras": 20,
"gasto_total": 3200.0, "dias_ultima_compra": 3},
{"cliente_id": "CL08", "nombre": "Mario Soto", "frecuencia_compras": 1,
"gasto_total": 60.0, "dias_ultima_compra": 300}
]

def evaluar_rfm(cliente):

    # Evaluar Recencia
    if cliente["dias_ultima_compra"] <= 90:
        recencia = "Alta"
    elif cliente["dias_ultima_compra"] <= 180:
        recencia = "Media"
    else:
        recencia = "Baja"

    # Evaluar Frecuencia
    if cliente["frecuencia_compras"] >= 10:
        frecuencia = "Alta"
    elif cliente["frecuencia_compras"] >= 5:
        frecuencia = "Media"
    else:
        frecuencia = "Baja"

    # Evaluar Valor Monetario
    if cliente["gasto_total"] >= 2000:
        valor_monetario = "Alto"
    elif cliente["gasto_total"] >= 1000:
        valor_monetario = "Medio"
    else:
        valor_monetario = "Bajo"

    return {
        "cliente_id": cliente["cliente_id"],
        "nombre": cliente["nombre"],
        "recencia": recencia,
        "frecuencia": frecuencia,
        "valor_monetario": valor_monetario
    }


def asignar_categoria(evaluacion_rfm):
    recencia = evaluacion_rfm["recencia"]
    frecuencia = evaluacion_rfm["frecuencia"]
    valor_monetario = evaluacion_rfm["valor_monetario"]
    if recencia == "Alta" and frecuencia == "Alta" and valor_monetario == "Alto":
        return "VIP"
    elif recencia == "Baja":
        return "Inactivo"
    elif recencia == "Media":
        return "En riesgo"
    elif recencia == "Alta" and (frecuencia == "Alta" or frecuencia == "Media"):
        return "Leal"
    else:
        return "Nuevo"

def resumir_cartera(clientes):
    resumen = {}

    for cliente in clientes:
        categoria = asignar_categoria(evaluar_rfm(cliente))
        if categoria not in resumen:
            resumen[categoria] = {"clientes": 0, "ingresos": 0.0}
        resumen[categoria]["clientes"] += 1
        resumen[categoria]["ingresos"] += cliente["gasto_total"]

    return resumen

print(resumir_cartera(clientes_rfm))