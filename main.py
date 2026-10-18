# Financial Data Analysis Project
# Proyecto de análisis de datos financieros

from datos import transacciones
from reportes import mostrar_reporte


def main():
    """Coordina la ejecución del programa."""
    mostrar_reporte(transacciones)


if __name__ == "__main__":
    main()
