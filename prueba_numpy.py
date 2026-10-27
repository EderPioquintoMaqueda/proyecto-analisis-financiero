import numpy as np
from datos import transacciones

importes = [
    transaccion["importe"]
    for transaccion in transacciones
]

arreglo_importes = np.array(importes)

print("Importes:", arreglo_importes)
print("Cantidad de importes:", arreglo_importes.size)
print("Suma:", np.sum(arreglo_importes))
print("Promedio:", np.mean(arreglo_importes))
