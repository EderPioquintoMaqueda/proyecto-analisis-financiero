
# Financial charts
# Gráficas financieras

from collections import defaultdict

import matplotlib.pyplot as plt

from finanzas import calcular_total


def mostrar_graficas_financieras(transacciones):
    """Muestra gráficas de gastos y comparación financiera."""

    # 1. Agrupar los gastos por categoría.
    gastos_por_categoria = defaultdict(float)

    for transaccion in transacciones:
        if transaccion["tipo"] == "gasto":
            categoria = transaccion["categoria"]
            importe = transaccion["importe"]

            gastos_por_categoria[categoria] += importe

    if not gastos_por_categoria:
        print("No hay gastos registrados para graficar.")
        return

    # 2. Ordenar las categorías de mayor a menor gasto.
    categorias_ordenadas = sorted(
        gastos_por_categoria,
        key=gastos_por_categoria.get,
        reverse=True,
    )

    importes_ordenados = [
        gastos_por_categoria[categoria]
        for categoria in categorias_ordenadas
    ]

    # 3. Calcular los ingresos y los gastos totales.
    ingresos = calcular_total(transacciones, "ingreso")
    gastos = calcular_total(transacciones, "gasto")

    # 4. Gráfica de barras: gastos por categoría.
    plt.figure(figsize=(9, 5))

    plt.bar(categorias_ordenadas, importes_ordenados)

    plt.title("Gastos por categoría / Expenses by category")
    plt.xlabel("Categoría / Category")
    plt.ylabel("Importe / Amount ($)")
    plt.xticks(rotation=20)
    plt.tight_layout()

    # 5. Gráfica circular: distribución porcentual.
    plt.figure(figsize=(8, 8))

    plt.pie(
        importes_ordenados,
        labels=categorias_ordenadas,
        autopct="%1.1f%%",
        startangle=90,
    )

    plt.title("Distribución de gastos / Expense distribution")
    plt.axis("equal")
    plt.tight_layout()

    # 6. Gráfica comparativa: ingresos frente a gastos.
    conceptos = ["Ingresos / Income", "Gastos / Expenses"]
    importes = [ingresos, gastos]

    plt.figure(figsize=(8, 5))

    barras = plt.bar(conceptos, importes)

    plt.title("Ingresos vs. gastos / Income vs. expenses")
    plt.ylabel("Importe / Amount ($)")

    # Mostrar el importe encima de cada barra.
    plt.bar_label(
        barras,
        labels=[f"${importe:,.2f}" for importe in importes],
        padding=3,
    )

    plt.tight_layout()

    # 7. Mostrar las tres gráficas.
    plt.show()
