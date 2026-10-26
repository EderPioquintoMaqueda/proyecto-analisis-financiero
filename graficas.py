
# Financial charts
# Gráficas financieras

from collections import defaultdict

import matplotlib.pyplot as plt


def mostrar_grafica_gastos(transacciones):
    """Muestra los gastos agrupados por categoría."""

    gastos_por_categoria = defaultdict(float)

    for transaccion in transacciones:
        if transaccion["tipo"] == "gasto":
            categoria = transaccion["categoria"]
            importe = transaccion["importe"]

            gastos_por_categoria[categoria] += importe

    categorias = list(gastos_por_categoria.keys())
    importes = list(gastos_por_categoria.values())

    plt.figure(figsize=(9, 5))

    plt.bar(categorias, importes)

    plt.title("Gastos por categoría / Expenses by category")
    plt.xlabel("Categoría / Category")
    plt.ylabel("Importe / Amount ($)")

    plt.xticks(rotation=20)
    plt.tight_layout()

    plt.show()
