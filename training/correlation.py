import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carga los datos desde un archivo CSV
data = pd.read_csv("datasettif.csv", index_col="fecha")

# Elimina la columna "id"
data = data.drop("id", axis=1)

# Convierte la columna de fechas a numérica para calcular la correlación
data["fecha"] = pd.to_numeric(pd.to_datetime(data.index))

# Calcula la correlación entre las columnas restantes
correlation_matrix = data.corr()

# Imprime la matriz de correlación
print(correlation_matrix)

# Crea un mapa de calor para visualizar la correlación
plt.figure(figsize=(10, 8))
plt.imshow(correlation_matrix, cmap="coolwarm", interpolation="nearest")
plt.colorbar()
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=90)
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
plt.title("Matriz de Correlación")
plt.show()