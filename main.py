
# Financial Data Analysis Project
# Proyecto de análisis de datos financieros

from datos import cargar_transacciones
from reportes import mostrar_reporte
from analisis_datos import mostrar_analisis_tabular
from graficas import mostrar_graficas_financieras


def main():
    """Coordina la carga, el análisis y la visualización."""

    df = cargar_transacciones()

    transacciones = df.to_dict(orient="records")

    mostrar_reporte(transacciones)
    mostrar_analisis_tabular(transacciones)
    mostrar_graficas_financieras(transacciones)


if __name__ == "__main__":
    main()
