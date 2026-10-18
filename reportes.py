# Financial reports
# Reportes financieros

from finanzas import (
    calcular_total,
    calcular_balance,
    contar_transacciones,
)


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
    print(
        "Número de transacciones / "
        f"Number of transactions: {cantidad}"
    )
