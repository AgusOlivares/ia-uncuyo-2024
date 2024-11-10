import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leer el archivo CSV
datos = pd.read_csv('resultados_algoritmos.csv', encoding='utf-8')

# Configurar el estilo de los gráficos
sns.set(style="whitegrid")

# Crear gráficos de caja y bigotes para cada tamaño de n (tiempos de ejecución)
tamaños = datos['Tamaño'].unique()
for n in tamaños:
    plt.figure(figsize=(10, 6))
    subset = datos[datos['Tamaño'] == n]
    
    # Extraer y expandir los tiempos
    tiempos = []
    algoritmos = []
    for _, row in subset.iterrows():
        tiempos_str = row['Tiempos'].split(', ')
        tiempos.extend(map(float, tiempos_str))  # Convertir cada tiempo a float
        algoritmos.extend([row['Algoritmo']] * len(tiempos_str))  # Repetir el algoritmo según la cantidad de tiempos

    # Crear un nuevo DataFrame para los tiempos expandidos
    tiempos_df = pd.DataFrame({'Algoritmo': algoritmos, 'Tiempos': tiempos})
    
    # Graficar
    sns.boxplot(x='Algoritmo', y='Tiempos', data=tiempos_df)
    plt.title(f'Distribución de Tiempos de Ejecución para n = {n}')
    plt.xlabel('Algoritmo')
    plt.ylabel('Tiempo de Ejecución')
    plt.savefig(f'grafico_tiempos_n_{n}.png')  # Guardar el gráfico de tiempos
    plt.close()

print("Gráficos de tiempos guardados para cada tamaño de n.")

# Crear gráfico de comparación de evaluaciones
plt.figure(figsize=(10, 6))
evaluaciones = []
for n in tamaños:
    subset = datos[datos['Tamaño'] == n]
    for _, row in subset.iterrows():
        evaluaciones.append({'Tamaño': n, 'Algoritmo': row['Algoritmo'], 'Evaluaciones': row['Evaluaciones']})

evaluaciones_df = pd.DataFrame(evaluaciones)

# Graficar como gráfico de líneas
plt.figure(figsize=(10, 6))
for algoritmo in evaluaciones_df['Algoritmo'].unique():
    subset_alg = evaluaciones_df[evaluaciones_df['Algoritmo'] == algoritmo]
    plt.plot(subset_alg['Tamaño'], subset_alg['Evaluaciones'], marker='o', label=algoritmo)
    
    # Agregar etiquetas en cada punto
    for i in range(len(subset_alg)):
        plt.text(subset_alg['Tamaño'].iloc[i], subset_alg['Evaluaciones'].iloc[i],
                 str(subset_alg['Evaluaciones'].iloc[i]), fontsize=10, ha='center', va='bottom')

plt.title('Evaluaciones por Algoritmo y Tamaño')
plt.xlabel('Tamaño')
plt.ylabel('Número de Evaluaciones')
plt.xticks(tamaños)  # Asegurar que todos los tamaños sean mostrados en el eje x
plt.legend(title='Algoritmo')
plt.grid()
plt.savefig('grafico_evaluaciones.png')  # Guardar gráfico de evaluaciones
plt.close()

print("Gráfico de evaluaciones guardado.")