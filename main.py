
# Financial Data Analysis Project
# Proyecto de análisis de datos financieros

# 1. Datos iniciales / Initial data
transacciones = [
    {"fecha": "2026-10-01", "tipo": "ingreso",
        "categoria": "salario", "importe": 18000.00},
    {"fecha": "2026-10-02", "tipo": "gasto",
        "categoria": "comida", "importe": 250.00},
    {"fecha": "2026-10-03", "tipo": "gasto",
        "categoria": "transporte", "importe": 120.00},
    {"fecha": "2026-10-05", "tipo": "gasto",
        "categoria": "vivienda", "importe": 4500.00},
    {"fecha": "2026-10-08", "tipo": "ingreso",
        "categoria": "freelance", "importe": 2500.00},
    {"fecha": "2026-10-10", "tipo": "gasto",
        "categoria": "comida", "importe": 380.00},
    {"fecha": "2026-10-12", "tipo": "gasto",
        "categoria": "transporte", "importe": 200.00},
    {"fecha": "2026-10-15", "tipo": "gasto",
        "categoria": "entretenimiento", "importe": 450.00},
]


# 2. Calcular el total por tipo / Calculate total by type
def calcular_total(transacciones, tipo):
    """Calcula el total de ingresos o gastos."""
    return sum(
        transaccion["importe"]
        for transaccion in transacciones
        if transaccion["tipo"] == tipo
    )


# 3. Calcular el balance / Calculate the balance
def calcular_balance(ingresos, gastos):
    """Calcula la diferencia entre ingresos y gastos."""
    return ingresos - gastos


# 4. Contar transacciones / Count transactions
def contar_transacciones(transacciones):
    """Devuelve el número de transacciones registradas."""
    return len(transacciones)


# 5. Generar el reporte / Generate the report
def mostrar_reporte(transacciones):
    """Calcula y muestra el resumen financiero."""

    ingresos = calcular_total(transacciones, "ingreso")
    gastos = calcular_total(transacciones, "gasto")
    balance = calcular_balance(ingresos, gastos)
    cantidad = contar_transacciones(transacciones)

    print("=== REPORTE FINANCIERO / FINANCIAL REPORT ===")
    print(f"Total de ingresos / Total income: ${ingresos:,.2f}")
    print(f"Total de gastos / Total expenses: ${gastos:,.2f}")
    print(f"Balance final / Net balance: ${balance:,.2f}")
    print(f"Número de transacciones / Number of transactions: {cantidad}")


# 6. Ejecutar el programa / Run the program
mostrar_reporte(transacciones)
