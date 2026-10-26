
# Financial reports
# Reportes financieros

from finanzas import (
    calcular_total,
    calcular_balance,
    contar_transacciones,
)

from estadisticas import (
    calcular_promedio,
    calcular_desviacion_estandar,
)


def mostrar_reporte(transacciones):
    """Calcula y muestra el resumen financiero."""

    ingresos = calcular_total(transacciones, "ingreso")
    gastos = calcular_total(transacciones, "gasto")
    balance = calcular_balance(ingresos, gastos)
    cantidad = contar_transacciones(transacciones)

    importes_gastos = [
        transaccion["importe"]
        for transaccion in transacciones
        if transaccion["tipo"] == "gasto"
    ]

    promedio_gasto = calcular_promedio(importes_gastos)
    desviacion_gasto = calcular_desviacion_estandar(importes_gastos)

    print("=== REPORTE FINANCIERO / FINANCIAL REPORT ===")
    print(f"Total de ingresos / Total income: ${ingresos:,.2f}")
    print(f"Total de gastos / Total expenses: ${gastos:,.2f}")
    print(f"Balance final / Net balance: ${balance:,.2f}")
    print(
        "Número de transacciones / "
        f"Number of transactions: {cantidad}"
    )
    print(f"Promedio por gasto / Average expense: ${promedio_gasto:,.2f}")
    print(
        "Desviación estándar / Standard deviation: "
        f"${desviacion_gasto:,.2f}"
    )
