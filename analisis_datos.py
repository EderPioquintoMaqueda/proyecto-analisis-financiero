
# Tabular data analysis
# Análisis tabular de datos

import pandas as pd


def mostrar_analisis_tabular(transacciones):
    """Muestra las transacciones y un resumen de gastos por categoría."""

    # Convertir la lista de diccionarios en una tabla.
    df = pd.DataFrame(transacciones)

    print("\n=== TABLA DE TRANSACCIONES ===")
    print(df.to_string(index=False))

    # Seleccionar únicamente los gastos.
    gastos = df[df["tipo"] == "gasto"]

    # Agrupar los gastos y sumar los importes por categoría.
    resumen_gastos = (
        gastos.groupby("categoria", as_index=False)["importe"]
        .sum()
        .sort_values("importe", ascending=False)
    )

    print("\n=== GASTOS POR CATEGORÍA ===")
    print(resumen_gastos.to_string(index=False))

    # Calcular el total de ingresos y gastos con pandas.
    total_ingresos = df.loc[
        df["tipo"] == "ingreso", "importe"
    ].sum()

    total_gastos = gastos["importe"].sum()

    print("\n=== RESUMEN CON PANDAS ===")
    print(f"Total de ingresos: ${total_ingresos:,.2f}")
    print(f"Total de gastos:   ${total_gastos:,.2f}")
    print(f"Balance:           ${total_ingresos - total_gastos:,.2f}")
