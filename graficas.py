
# Financial charts
# Gráficas financieras

from collections import defaultdict

import matplotlib.pyplot as plt


def mostrar_grafica_gastos(transacciones):
    """Muestra los gastos por categoría y su distribución porcentual."""

    gastos_por_categoria = defaultdict(float)

    # 1. Agrupar los gastos por categoría.
    for transaccion in transacciones:
        if transaccion["tipo"] == "gasto":
            categoria = transaccion["categoria"]
            importe = transaccion["importe"]

            gastos_por_categoria[categoria] += importe

    # Evitar generar gráficas si no existen gastos.
    if not gastos_por_categoria:
        print("No hay gastos registrados para graficar.")
        return

    # 2. Ordenar las categorías de mayor a menor gasto.
    categorias_ordenadas = sorted(
        gastos_por_categoria,
        key=gastos_por_categoria.get,
        reverse=True,
    )

    # 3. Preparar los importes en el mismo orden.
    importes_ordenados = [
        gastos_por_categoria[categoria]
        for categoria in categorias_ordenadas
    ]

    # 4. Crear la gráfica de barras.
    plt.figure(figsize=(9, 5))

    plt.bar(categorias_ordenadas, importes_ordenados)

    plt.title("Gastos por categoría / Expenses by category")
    plt.xlabel("Categoría / Category")
    plt.ylabel("Importe / Amount ($)")

    plt.xticks(rotation=20)
    plt.tight_layout()

    # 5. Crear la gráfica circular.
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

    # 6. Mostrar ambas gráficas.
    plt.show()
