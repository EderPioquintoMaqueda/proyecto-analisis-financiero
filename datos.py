
# Data loading
# Carga de datos

from pathlib import Path

import pandas as pd


def cargar_transacciones():
    """Carga las transacciones financieras desde un archivo CSV."""

    ruta_archivo = Path(__file__).with_name("transacciones.csv")

    df = pd.read_csv(ruta_archivo)

    columnas_esperadas = {
        "fecha",
        "tipo",
        "categoria",
        "importe",
    }

    if not columnas_esperadas.issubset(df.columns):
        raise ValueError(
            "El CSV debe contener las columnas: "
            "fecha, tipo, categoria, importe."
        )

    if df[list(columnas_esperadas)].isnull().any().any():
        raise ValueError(
            "El CSV contiene valores vacíos en columnas requeridas."
        )

    if not df["tipo"].isin(["ingreso", "gasto"]).all():
        raise ValueError(
            "La columna 'tipo' solo acepta 'ingreso' o 'gasto'."
        )

    if (df["importe"] < 0).any():
        raise ValueError("Los importes no pueden ser negativos.")

    return df
