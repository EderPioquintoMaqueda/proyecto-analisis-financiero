
# Financial Data Analysis Project
# Proyecto de análisis de datos financieros

# 1. Datos iniciales / Initial data
transacciones = [
    {"fecha": "2026-10-01", "tipo": "ingreso", "categoria": "salario", "importe": 18000.00},
    {"fecha": "2026-10-02", "tipo": "gasto", "categoria": "comida", "importe": 250.00},
    {"fecha": "2026-10-03", "tipo": "gasto", "categoria": "transporte", "importe": 120.00},
    {"fecha": "2026-10-05", "tipo": "gasto", "categoria": "vivienda", "importe": 4500.00},
    {"fecha": "2026-10-08", "tipo": "ingreso", "categoria": "freelance", "importe": 2500.00},
    {"fecha": "2026-10-10", "tipo": "gasto", "categoria": "comida", "importe": 380.00},
    {"fecha": "2026-10-12", "tipo": "gasto", "categoria": "transporte", "importe": 200.00},
    {"fecha": "2026-10-15", "tipo": "gasto", "categoria": "entretenimiento", "importe": 450.00},
]

# 2. Calcular ingresos y gastos
# Calculate income and expenses
ingresos = sum(
    t["importe"] for t in transacciones
    if t["tipo"] == "ingreso"
)

gastos = sum(
    t["importe"] for t in transacciones
    if t["tipo"] == "gasto"
)

# 3. Calcular el balance / Calculate the balance
balance = ingresos - gastos

# 4. Mostrar el reporte / Display the report
print("=== REPORTE FINANCIERO / FINANCIAL REPORT ===")
print(f"Total de ingresos / Total income: ${ingresos:,.}")
print(f"Total de gastos / Total expenses: ${gastos:,.2f}")
print(f"Balance final / Final balance: ${balance:,.2f}")
print(f"Número de transacciones / Number of transactions: {len(transacciones)}")
