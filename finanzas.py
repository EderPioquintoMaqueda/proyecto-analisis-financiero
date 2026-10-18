
# Financial calculations
# Cálculos financieros

def calcular_total(transacciones, tipo):
    """Calcula el total de ingresos o gastos."""
    return sum(
        transaccion["importe"]
        for transaccion in transacciones
        if transaccion["tipo"] == tipo
    )


def calcular_balance(ingresos, gastos):
    """Calcula la diferencia entre ingresos y gastos."""
    return ingresos - gastos


def contar_transacciones(transacciones):
    """Devuelve el número de transacciones registradas."""
    return len(transacciones)
