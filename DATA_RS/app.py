# app.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
import io
import base64
from flask import Flask, render_template

# Inicializa la aplicación Flask
app = Flask(__name__)

@app.route('/')
def index():
    """
    Ruta principal que genera los datos, crea los gráficos y calcula las estadísticas,
    luego renderiza la plantilla HTML para mostrarlos.
    """
    # --- Tarea 2: Generar datos aleatorios para el experimento de redes sociales ---
    # Definir la lista de categorías
    categories = ['Comida', 'Viajes', 'Moda', 'Tecnología', 'Deportes', 'Música', 'Arte']

    # Generar un rango de fechas
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')

    # Crear una lista para almacenar los datos
    data = []
    for _ in range(500): # Generar 500 entradas de datos
        date = random.choice(dates)
        category = random.choice(categories)
        # Generar un número aleatorio de likes entre 10 y 1000
        likes = np.random.randint(10, 1001)
        data.append({'Date': date, 'Category': category, 'Likes': likes})

    # Crear el DataFrame de pandas
    df = pd.DataFrame(data)

    # --- Tarea 3: Limpiar los datos ---
    # Verificar si hay valores nulos
    # print("Valores nulos antes de la limpieza:")
    # print(df.isnull().sum())

    # Eliminar filas con valores nulos (si los hubiera)
    df.dropna(inplace=True)

    # Eliminar filas duplicadas (si las hubiera)
    df.drop_duplicates(inplace=True)

    # print("\nValores nulos después de la limpieza:")
    # print(df.isnull().sum())

    # --- Tarea 4: Visualizar los datos ---

    # Crear un buffer para almacenar las imágenes de los gráficos
    img_buffer = io.BytesIO()

    # Histograma de 'Likes'
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Likes'], bins=30, kde=True, color='skyblue')
    plt.title('Distribución de Likes')
    plt.xlabel('Número de Likes')
    plt.ylabel('Frecuencia')
    plt.grid(axis='y', alpha=0.75)
    plt.tight_layout()
    # Guardar el histograma en el buffer
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0) # Volver al inicio del buffer
    histogram_base64 = base64.b64encode(img_buffer.read()).decode('utf-8')
    plt.close() # Cerrar la figura para liberar memoria

    # Boxplot de 'Likes' por 'Category'
    img_buffer = io.BytesIO() # Resetear el buffer para el nuevo gráfico
    plt.figure(figsize=(12, 7))
    sns.boxplot(x='Category', y='Likes', data=df, palette='viridis')
    plt.title('Likes por Categoría')
    plt.xlabel('Categoría')
    plt.ylabel('Número de Likes')
    plt.grid(axis='y', alpha=0.75)
    plt.tight_layout()
    # Guardar el boxplot en el buffer
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0) # Volver al inicio del buffer
    boxplot_base64 = base64.b64encode(img_buffer.read()).decode('utf-8')
    plt.close() # Cerrar la figura para liberar memoria

    # --- Tarea 4: Realizar estadísticas sobre los datos ---
    # Media de la categoría 'Likes'
    mean_likes = df['Likes'].mean()

    # Media de 'Likes' por 'Category'
    grouped_mean_likes = df.groupby('Category')['Likes'].mean().reset_index()

    # Renderizar la plantilla HTML y pasar los datos de las imágenes y las estadísticas
    return render_template('index.html',
                           histogram_image=histogram_base64,
                           boxplot_image=boxplot_base64,
                           mean_likes=mean_likes,
                           grouped_mean_likes=grouped_mean_likes.to_html(classes='table table-striped', index=False))

# Ejecutar la aplicación Flask si este script es el principal
if __name__ == '__main__':
    app.run(debug=True)
