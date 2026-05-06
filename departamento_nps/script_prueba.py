# script_prueba.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Librerías importadas correctamente")

# Crear datos con numpy
datos = np.array([10, 20, 30, 40, 50])
print("Datos numpy:", datos)

# Crear DataFrame con pandas
df = pd.DataFrame(datos, columns=["Valores"])
print("\nDataFrame:")
print(df)

# Crear gráfica con matplotlib
plt.plot(df["Valores"])
plt.title("Gráfica de prueba")
plt.xlabel("Índice")
plt.ylabel("Valores")

print("\nMostrando gráfica...")
plt.show()