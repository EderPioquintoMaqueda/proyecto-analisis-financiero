
# Financial charts
# Gráficas financieras

from collections import defaultdict

import matplotlib.pyplot as plt


def mostrar_grafica_gastos(transacciones):
    """Muestra los gastos agrupados por categoría, de mayor a menor."""

    gastos_por_categoria = defaultdict(float)

    # Agrupar los gastos por categoría.
    for transaccion in transacciones:
        if transaccion["tipo"] == "gasto":
            categoria = transaccion["categoria"]
            importe = transaccion["importe"]

            gastos_por_categoria[categoria] += importe

    # Ordenar las categorías por importe, de mayor a menor.
    categorias_ordenadas = sorted(
        gastos_por_categoria,
        key=gastos_por_categoria.get,
        reverse=True,
    )

    # Obtener los importes en el mismo orden de las categorías.
    importes_ordenados = [
        gastos_por_categoria[categoria]
        for categoria in categorias_ordenadas
    ]

    # Crear la gráfica de barras.
    plt.figure(figsize=(9, 5))

    plt.bar(categorias_ordenadas, importes_ordenados)

    plt.title("Gastos por categoría / Expenses by category")
    plt.xlabel("Categoría / Category")
    plt.ylabel("Importe / Amount ($)")

    plt.xticks(rotation=20)
    plt.tight_layout()

    plt.show()
