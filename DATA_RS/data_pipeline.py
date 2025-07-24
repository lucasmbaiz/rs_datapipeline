#TAREA 1 - Importar Librerías Requeridas

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random
import numpy as np

from datetime import datetime

def log_progress(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("code_log.txt", "a") as f:
        f.write(f"{timestamp} : {message} \n")

# Registro para la tarea 1       
log_progress("Bibliotecas requeridas importadas.")

print("Bibliotecas importadas correctamente")

#TAREA 2 - Generar datos aleatorios para los datos en redes sociales

categories = ['Food', 'Travel', 'Fashion', 'Fitness', 'Music', 'Culture', 'Family', 'Health']

# Entrada de datos
n = 500

# Generando un diccionario aleatorio de entrada de datos
data = {
    'Date': pd.date_range('2021-01-01', periods=n), # Rango de fechas desde el 01/01/2021
    'Category': [random.choice(categories) for _ in range (n)],
    'Likes': np.random.randint(0, 1001, size=n)# Enteros aleatorios entre 1 y 1000    
}

# Registro para la tarea 2
log_progress("Datos aleatorios de redes sociales generados")

print("Datos aleatorios generados correctamente:")
#Imprime las primeras 5 entradas para verificar

print(data['Date'][:5])
print(data['Category'][:5])
print(data['Likes'][:5])

# TAREA 3 - Cargar los datos en un Pandas DataFrame y explorar los Datos

df = pd.DataFrame(data)

print("DataFrame creado exitosamente")

# Imprimir las primeras 5 filas del DataFrame
print("\nPrimeras 5 lineas del DataFrame")
print(df.head())

# Imprimir la INFO del DataFrame
print("\nInformación del DataFrame")
df.info()

# Imprimir la descripción estadistica del DataFrame
print("\nDescripción estadistica del DataFrame")
print(df.describe())

# Imprimir el conteo de cada elemento de Category
print("\nConteo de Likes por categoria:")
print(df['Category'].value_counts())

# Registro para la tarea 3
log_progress("Datos cargados en DataFrame y explorados.")

# TAREA 4 - Limpiar los datos

print("Iniciando limpieza de datos...")

# 1. Verificar valores faltantes
print("\nVerificando valores faltantes en el DataFrame:")
print(df.isnull().sum()) # Suma de valores nulos por columna

if df.isnull().sum().sum() > 0:
    print("\nAdvertencia: Existen valores faltantes en el DataFrame. Considera eliminarlos o imputarlos.")
else:
    print("\nExcelente! No se encontraron valores faltantes.")

# 2. Verificar duplicados
print("\nVerificando filas duplicadas en el DataFrame:")
num_duplicates = df.duplicated().sum()
print(f"Número de filas duplicadas: {num_duplicates}")

# Si hay duplicados, eliminarlos
if num_duplicates > 0:  
    df = df.drop_duplicates(inplace=True)
    print(f"\nSe eliminaron {num_duplicates} filas duplicadas.")
    print(f"Nuevo número de filas en el DataFrame: {len(df)}")
else:
    print("\nExcelente! No se encontraron filas duplicadas.")

print("\nLimpieza de datos completada.")

# Registro para la tarea 4
log_progress("Datos limpiados y verificados.")

# TAREA 5 - Visualizar los datos y realizar estadisticas descriptivas

print("\nIniciando visualización de datos y cálculo de estadisticas...")

# 1. Crear un histograma de la columna 'Likes'
print("\nCreando histograma de Likes...")
plt.figure(figsize=(10, 6)) # Define el tamaño de la figura
sns.histplot(df['Likes'], kde=True, bins=20) # Crea el histograma con una curva de densidad
plt.title('Distribución de Likes') # Añade título al histograma
plt.xlabel('Likes') # Añade etiqueta al eje X
plt.ylabel('Frecuencia') # Añade etiqueta al eje Y
plt.grid(axis='y', alpha=0.75) # Añade una cuadrícula
plt.show() # Muestra el histograma

# 2. Crear un Bloxplot de 'Likes' por 'Category'
print("\nCreando boxplot de Likes por Category...")
plt.figure(figsize=(12, 7)) # Define el tamaño de la figura
sns.boxplot(x='Category', y='Likes', data=df) # Crea el boxplot
plt.title('Distribución de Likes por Categoria') # Añade título al boxplot
plt.xlabel('Categoria') # Añade etiqueta al eje X
plt.ylabel('Likes') # Añade etiqueta al eje Y
plt.xticks(rotation=45, ha='right') # Rota las etiquetas del eje X para mejor visibilidad
plt.tight_layout() # Ajusta el layout para evitar superposiciones
plt.show() # Muestra el boxplot

# 3. Calcular estadisticas descriptivas
print("\nRealizando cálculos estadisticos...")

# Imprimir la media de la categoria 'Likes'
mean_likes = df['Likes'].mean()
print(f"\nMedia de Likes: {mean_likes:.2f}")

# Usar el método groupby para calcular la media de Likes por categoria
mean_likes_by_category = df.groupby('Category')['Likes'].mean()
print("\nMedia de Likes por Categoria:")
print(mean_likes_by_category)

print("\nEstadisticas descriptivas completas:")

# Registro para la tarea 5
log_progress("Datos visualizados (histograma Boxplot) y estadisticas descriptivas calculadas.")