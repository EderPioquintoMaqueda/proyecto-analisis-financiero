
# Financial Data Analysis Project
# Proyecto de análisis de datos financieros

from datos import transacciones
from reportes import mostrar_reporte
from graficas import mostrar_grafica_gastos


def main():
    """Coordina la ejecución del programa."""

    mostrar_reporte(transacciones)
    mostrar_grafica_gastos(transacciones)


if __name__ == "__main__":
    main()
