import gymnasium as gym
import map as map
import matplotlib.pyplot as plt
import seaborn as sns
import random
import algorithms as algo
import analisis as la
import pandas as pd
import time


def iniciarEnv(env, steps):

    if steps is None:
        return 
    
    # Diccionario para traducir movimientos a acciones en el entorno
    direction_to_action = {
        (0, -1): 0,  # Izquierda
        (1, 0): 1,   # Abajo
        (0, 1): 2,   # Derecha
        (-1, 0): 3  # Arriba
    }

    # Simulación usando steps
    done = truncated = False
    step_count = 0

    for i in range(len(steps) - 1):

        if i == 1000:
            print(f"¿Frenó? (alcanzó el máximo de pasos posible): {truncated}\n")
            break

        current_pos = steps[i]
        next_pos = steps[i + 1]
        # Calcular la dirección del movimiento (Izq,Abajo,Derecha,Arriba)
        move = (next_pos[0] - current_pos[0], next_pos[1] - current_pos[1])
        # Obtener la acción correspondiente
        action = direction_to_action.get(move)
        
        if action is not None:
            next_state, reward, done, truncated, _ = env.step(action)
            print(f"Paso {step_count}: Acción: {action}, Nuevo estado: {next_state}, Recompensa: {reward}")
            print(f"¿Ganó? (encontró el objetivo): {done}")
            step_count += 1
            
        if done:
            break

    # Cerrar el entorno al finalizar
    env.close()

def calculate_cost(path):
    """
    Calcula el costo del camino según las especificaciones dadas.

    path: Lista de tuplas que representan el camino desde el inicio al objetivo.

    return: 
        - Costo con todas las direcciones con valor 1.
        - Costo con izquierda = 1, abajo = 2, derecha = 3 y arriba = 4.
    """

    if path is None or len(path) > 1000: 
        return 0,0
    
    # Direcciones de movimiento con su respectivo costo
    direction_to_cost = {
        (0, -1): 1,  # Izquierda
        (1, 0): 2,   # Abajo
        (0, 1): 3,   # Derecha
        (-1, 0): 4   # Arriba
    }

    cost_uniform = len(path)-1  # Costo donde todas las direcciones valen 1
    cost_weighted = 0  # Costo según el valor de la dirección

    for i in range(len(path) - 1):
        current_pos = path[i]
        next_pos = path[i + 1]
        # Calcular la dirección del movimiento
        move = (next_pos[0] - current_pos[0], next_pos[1] - current_pos[1])

        # Sumar el costo para el movimiento actual
        cost_weighted += direction_to_cost.get(move, 0)  # Costo específico de la dirección

    return cost_uniform, cost_weighted

def init_algorithms():
    # Inicializar listas para almacenar resultados
    results = []

    # Realizar 30 simulaciones
    for simulation in range(30):
        # Generar seed aleatoria
        seed = random.randint(0, 1_000_000_000)
        print(f"Simulación {simulation + 1}, Seed: {seed}")
        random.seed(seed)

        # Crear el entorno, la posición inicial del agente y el objetivo
        size = 100
        p_hole = 0.08
        start = (random.randint(0, size - 1), random.randint(0, size - 1))
        end = (random.randint(0, size - 1), random.randint(0, size - 1))
        e = map.Map(size, p_hole, start, end)

        # Diccionario para almacenar resultados por simulación
        simul_result = {
            "seed": seed
        }

        # Aplicar los algoritmos
        for algo_name, algorithm in {
            "BFS": algo.bfs,
            "DFS": algo.dfs,
            "DLS": lambda g, s, e: algo.dfs_limited(g, s, e, 10),
            "UCS E1": algo.ucs_c1,
            "UCS E2": algo.ucs_c2,
            "A star": algo.a_star,
        }.items():
            # Medir el tiempo de ejecución
            start_time = time.time()
            # Ejecutar el algoritmo
            steps, num_states = algorithm(e.grid, e.start, e.end)
            
            # Medir el tiempo final
            end_time = time.time()
            
            # Calcular el tiempo de ejecución
            execution_time = end_time - start_time

            # Calcular el costo
            cost_1, cost_2 = la.calculate_cost(steps)
            
            # Comprobar si se encontró la solución
            if steps is None or len(steps) >= 1000:
                found_solution = False
            else:
                found_solution = True
                
            # Guardar resultados
            simul_result["Algoritmo"] = algo_name
            simul_result["numero_estados"] = num_states
            simul_result["cost_e1"] = cost_1
            simul_result["cost_e2"] = cost_2
            simul_result["solucion_encontrada"] = found_solution
            simul_result["tiempo_ejecicion"] = execution_time  # Agregar el tiempo de ejecución

            # Agregar el resultado de esta simulación a la lista
            results.append(simul_result.copy())

    return results

def box_states(results):

    # Crear el gráfico de cajas
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Algoritmo', y='numero_estados', data=results)

    # Configurar el gráfico
    plt.title('Comparación de número de estados visitados por algoritmo')
    plt.xlabel('Algoritmo')
    plt.ylabel('Número de estados')
    plt.xticks(rotation=45)
    
    # Mostrar el gráfico
    plt.tight_layout()
    plt.show()


def box_cost_e1(results):

    # Filtrar los resultados para excluir los valores de 'cost_e1' que sean 0
    filtered_results = results[results["solucion_encontrada"] == True]
    
    # Crear el gráfico de cajas
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Algoritmo', y='cost_e1', data=filtered_results)

    # Configurar el gráfico
    plt.title('Comparación de cost_e1 por algoritmo (sin valores de cost_e1 = 0)')
    plt.xlabel('Algoritmo')
    plt.ylabel('Cost E1')
    plt.xticks(rotation=45)
    
    # Mostrar el gráfico
    plt.tight_layout()
    plt.show()


def box_cost_e2(results):

    filtered_results = results[results["solucion_encontrada"] == True]
    # Crear el gráfico de cajas
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Algoritmo', y='cost_e2', data=filtered_results)

    # Configurar el gráfico
    plt.title('Comparación de cost_e2 por algoritmo')
    plt.xlabel('Algoritmo')
    plt.ylabel('Cost E2')
    plt.xticks(rotation=45)
    
    # Mostrar el gráfico
    plt.tight_layout()
    plt.show()

def box_times(results):

    # Crear el gráfico de cajas
    filtered_results = results[results["solucion_encontrada"] == True]
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Algoritmo', y='tiempo_ejecicion', data=filtered_results)

    # Configurar el gráfico
    plt.title('Comparación de execution_time por Algoritmo')
    plt.xlabel('Algoritmo')
    plt.ylabel('execution_time')
    plt.xticks(rotation=45)
    
    # Mostrar el gráfico
    plt.tight_layout()
    plt.show()

def plot_solution_counts(results):

    # Filtrar las filas donde se encontró la solución
    solution_counts = results[results["solucion_encontrada"] == True].groupby("Algoritmo").size()

    # Crear un gráfico de barras
    plt.figure(figsize=(10, 6))
    solution_counts.plot(kind='bar', color='skyblue')

    # Configurar el gráfico
    plt.title('Cantidad de soluciones encontradas por cada algoritmo')
    plt.xlabel('Algoritmo')
    plt.ylabel('Cantidad de soluciones')
    plt.xticks(rotation=45)
    
    # Mostrar el gráfico
    plt.tight_layout()
    plt.show()