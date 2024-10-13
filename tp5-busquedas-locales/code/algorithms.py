from tablero import Tablero
import copy
import random
import math

def hill_climbing(n: int) -> Tablero:  # Tengo mi objeto tablero, que inicia con reinas aleatorias y una función que calcula el heurístico.
    env1 = Tablero(n)  # Inicia el tablero con tamaño n

    print('tablero inicial:')
    env1.map_print()

    max_states = 25  # Máximo número de iteraciones permitidas
    count = 0  # Contador de iteraciones

    while count < max_states:
        current_heuristic = env1.calculate_heuristic()

        #  0 es el valor óptimo
        if current_heuristic == 0:
            print("Solución encontrada.")
            return env1

        neighbor = copy.deepcopy(env1)

        best_heuristic = current_heuristic
        best_neighbor = neighbor

        # Recorremos las columnas
        for col in range(n):
            for row in range(n):

                future_state = calculate_future(copy.deepcopy(neighbor), col, row) # Cambio la reina en la col actual, ACA esta el error
                future_heuristic = future_state.calculate_heuristic()

                
                if future_heuristic < best_heuristic:
                    best_neighbor = future_state
                    best_heuristic = future_heuristic
                    env1 = copy.deepcopy(best_neighbor)
                    break
                    
        count += 1

    return env1.map_print(), env1.calculate_heuristic()


def calculate_future(env: Tablero, col: int, target_row: int):  

    current_row = next(i for i in range(env.size) if env.grid[i][col]['state'] == 1)

    
    if target_row != current_row:
        env.grid[current_row][col]['state'] = 0  
        env.grid[target_row][col]['state'] = 1

    return env


# , schedule
def simulated_annealing(n: int) -> Tablero:
    env1 = Tablero(n)  # Inicializa el tablero con reinas aleatorias

    print('tablero inicial:')
    env1.map_print()

    count = 0  # Contador de iteraciones
    current_heuristic = env1.calculate_heuristic()

    while True:
        temperature = schedule(count)  # Obtenemos la temperatura del schedule
        if temperature == 0 or current_heuristic == 0:  # Termina si temperatura es 0 o si alcanzamos la solución óptima
            print("Fin del algoritmo.")
            return env1.map_print(), env1.calculate_heuristic()

        # vecino aleatorio
        col = random.randint(0, n - 1)
        row = random.randint(0, n - 1)
        neighbor = calculate_future(copy.deepcopy(env1), col, row)

        future_heuristic = neighbor.calculate_heuristic()

        delta_e = current_heuristic - future_heuristic
        if delta_e > 0:
            env1 = copy.deepcopy(neighbor)
            current_heuristic = future_heuristic
        else:
            # Si no es mejor, lo aceptamos con cierta probabilidad
            probability = math.exp(delta_e / temperature)  # Probabilidad de aceptar un peor estado
            if random.random() < probability:
                env1 = copy.deepcopy(neighbor)
                current_heuristic = future_heuristic

        count += 1

def schedule(t: int) -> float:

    initial_temp = 100
    cooling_rate = 0.01 
    return initial_temp * math.exp(-cooling_rate * t)