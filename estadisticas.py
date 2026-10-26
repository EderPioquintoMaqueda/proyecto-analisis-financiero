
# Statistical analysis
# Análisis estadístico

import numpy as np


def calcular_promedio(importes):
    """Calcula el promedio de una colección de importes."""
    valores = np.array(importes, dtype=float)
    return np.mean(valores)


def calcular_desviacion_estandar(importes):
    """Calcula la desviación estándar poblacional."""
    valores = np.array(importes, dtype=float)
    return np.std(valores)
