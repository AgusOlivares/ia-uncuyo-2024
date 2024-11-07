from tablero import Tablero, Solution  
import copy
import random
import math

def hill_climbing(n: int):
    env1 = Tablero(n)
    max_states = 25
    count = 0
    heuristic_path = []  # Para almacenar los valores de la heurística en cada iteración
    
    while count < max_states:
        current_heuristic = env1.calculate_heuristic()
        heuristic_path.append(current_heuristic)  # Guarda el valor actual de la heurística
        
        if current_heuristic == 0:
            return env1, heuristic_path  # Devuelve también el historial de heurística

        neighbor = copy.deepcopy(env1)
        best_heuristic = current_heuristic
        best_neighbor = neighbor
        
        for col in range(n):
            for row in range(n):
                future_state = calculate_future(copy.deepcopy(neighbor), col, row)
                future_heuristic = future_state.calculate_heuristic()
                
                if future_heuristic < best_heuristic:
                    best_neighbor = future_state
                    best_heuristic = future_heuristic
                    env1 = copy.deepcopy(best_neighbor)
                    break
                    
        count += 1
    
    heuristic_path.append(env1.calculate_heuristic())  # Última medición de heurística
    return env1, heuristic_path  # Devuelve el historial de la heurística y el estado final


def calculate_future(env: Tablero, col: int, target_row: int) -> Tablero:
    current_row = next(i for i in range(env.size) if env.grid[i][col]['state'] == 1)
    if target_row != current_row:
        env.grid[current_row][col]['state'] = 0  
        env.grid[target_row][col]['state'] = 1
        env.record_state()  # Registra el cambio de estado después de mover una reina
    return env


def simulated_annealing(n: int):
    env1 = Tablero(n)  # Inicia el tablero con tamaño n
    heuristic_path = []  # Para almacenar los valores de la heurística

    print('tablero inicial:')
    env1.map_print()

    count = 0  # Contador de iteraciones
    current_heuristic = env1.calculate_heuristic()
    heuristic_path.append(current_heuristic)  # Agrega el valor inicial de heurística

    while True:
        temperature = schedule(count)  # Obtenemos la temperatura del schedule
        if temperature == 0 or current_heuristic == 0:  # Termina si temperatura es 0 o si alcanzamos la solución óptima
            print("Fin del algoritmo.")
            return env1, heuristic_path  # Retorna el tablero y el historial de la heurística

        # vecino aleatorio
        col = random.randint(0, n - 1)
        row = random.randint(0, n - 1)
        neighbor = calculate_future(copy.deepcopy(env1), col, row)
        future_heuristic = neighbor.calculate_heuristic()
        delta_e = current_heuristic - future_heuristic

        # Actualiza el estado actual o lo acepta con probabilidad
        if delta_e > 0 or random.random() < math.exp(delta_e / temperature):
            env1 = copy.deepcopy(neighbor)
            current_heuristic = future_heuristic
        
        heuristic_path.append(current_heuristic)  # Guarda la heurística después de cada movimiento
        count += 1

def schedule(t: int) -> float:

    initial_temp = 100 
    cooling_rate = 0.01 
    return initial_temp * math.exp(-cooling_rate * t) # Me muevo mas 'osadamente' al inicio y a medida que me voy equivocando acepto menos los tableros


def genetic_algorithm(n):
    population_size = 30  # Defino el tamaño de población
    generations = 100  # La cantidad de generaciones
    mutation_rate = 0.01  # El ratio de mutación

    # Generar población inicial
    population = [(generate_individual(n), None) for _ in range(population_size)]
    population = [(ind, calculate_heuristic(ind)) for ind, _ in population]  # Calcular heurístico inicial

    heuristic_path = []  # Lista para almacenar el mejor valor heurístico de cada generación

    for generation in range(generations):
        new_generation = []
        
        for _ in range(population_size // 2):
            # Selección de padres
            parent1 = selection(population)
            parent2 = selection(population)
            
            # Cruza y mutación
            child1, child2 = crossover(parent1[0], parent2[0])
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            
            # Calcular heurístico de los hijos y agregar a la nueva generación
            new_generation.append((child1, calculate_heuristic(child1)))
            new_generation.append((child2, calculate_heuristic(child2)))
        
        # Reemplazo de la población
        population = replacement(population, new_generation)

        # Encontrar el mejor individuo de la generación
        best_individual = min(population, key=lambda x: x[1])
        heuristic_path.append(best_individual[1])  # Almacena el valor de heurística mínimo en cada generación

        # Verificar si se ha encontrado la solución óptima
        if best_individual[1] == 0:
            print(f"Solución encontrada en la generación {generation + 1}: {best_individual[0]}")
            return Solution(best_individual[0], heuristic_path)  # Retorna un objeto Solution

    # Si no se encuentra solución óptima en el número de generaciones especificado
    print("No se encontró solución óptima.")
    return Solution(min(population, key=lambda x: x[1])[0], heuristic_path)  # Retorna un objeto Solution



def generate_individual(n):
    """Genera un individuo, que es un vector de tamaño n donde cada valor representa la fila de una reina en esa columna."""
    return [random.randint(0, n - 1) for _ in range(n)]

def calculate_heuristic(individual):
    """Calcula el número de conflictos en el tablero (peor heurístico)."""
    n = len(individual)
    conflicts = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            # Conflicto si están en la misma fila o en diagonal
            if individual[i] == individual[j] or abs(individual[i] - individual[j]) == j - i:
                conflicts += 1
    
    return conflicts

# 2. Selección: Torneo
def selection(population, tournament_size=3):
    """Selecciona el mejor individuo de un torneo aleatorio."""
    selected = random.sample(population, tournament_size)
    selected.sort(key=lambda x: x[1])  # Ordenar por heurístico (menos conflictos)
    return selected[0]

# 3. Operadores Genéticos
def crossover(parent1, parent2):
    """Cruza dos padres usando un corte de un punto."""
    point = random.randint(1, len(parent1) - 2)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(individual, mutation_rate=0.05):
    """Realiza una mutación en el individuo cambiando una reina aleatoriamente."""
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = random.randint(0, len(individual) - 1)
    return individual

# 4. Estrategia de reemplazo
def replacement(population, new_generation, elitism_size=1):
    """Reemplaza la población usando elitismo."""
    population.sort(key=lambda x: x[1])
    new_generation.sort(key=lambda x: x[1])
    
    # Mantener los mejores individuos
    return population[:elitism_size] + new_generation[:len(population) - elitism_size]