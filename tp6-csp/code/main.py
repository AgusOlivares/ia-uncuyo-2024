from backtracking import *
from csp import *
import time
import csv

def test_algoritmos(n, r):
    resultados = []

    for algoritmo in ['vuelta_atras', 'ac_3']:
        tiempos = []
        total_evaluaciones = 0

        for _ in range(r):
            if algoritmo == 'vuelta_atras':
                start_time = time.time()
                resultado, evaluaciones = busqueda_vuelta_atras(n)
                tiempos.append(time.time() - start_time)
                total_evaluaciones += evaluaciones
            else:  # ac_3
                board = Board(n)
                start_time = time.time()
                resultado, evaluaciones = ac_3(board)
                tiempos.append(time.time() - start_time)
                total_evaluaciones += evaluaciones

        # Calcular el promedio de evaluaciones
        promedio_evaluaciones = total_evaluaciones // r  # División entera para evitar decimales

        resultados.append((algoritmo, tiempos, promedio_evaluaciones))

    return resultados

# Tamaños de tablero a probar
tamaños = [4, 8, 10, 12]
r = 30  # Número de repeticiones para cada prueba

# Guardar resultados en un archivo CSV
with open('resultados_algoritmos.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Tamaño', 'Algoritmo', 'Tiempos', 'Evaluaciones'])

    # Ejecutar pruebas
    for n in tamaños:
        print(f"\nResultados para n = {n}:")
        resultados = test_algoritmos(n, r)
        for algoritmo, tiempos, promedio_evaluaciones in resultados:
            # Mostrar tiempos con 10 decimales
            tiempos_str = ', '.join(f"{tiempo:.10f}" for tiempo in tiempos)
            print(f"{algoritmo} -> Tiempos: {tiempos_str}, Evaluaciones: {promedio_evaluaciones}")
            writer.writerow([n, algoritmo, tiempos_str, promedio_evaluaciones])