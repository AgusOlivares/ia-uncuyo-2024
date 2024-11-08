import gymnasium as gym
import numpy as np
from collections import deque
import random
import heapq


def bfs(grid, start, goal):
    """ 
    grid: La matriz del entorno (custom_map)
    start: Tupla (x, y) de la posición inicial ('S')
    goal: Tupla (x, y) de la posición del objetivo ('G')
    
    return: Lista de tuplas que representan el camino desde el inicio al objetivo 
            y el número de estados visitados, o None si no hay camino.
    """
    # Direcciones de movimiento: izquierda, abajo, derecha, arriba
    directions = [(0,-1), (1,0), (0,1), (-1,0)]

    # Cola de la forma: (current , path) donde path lleva una lista del camino recorrido
    queue = deque([(start, [start])])
    
    # Posiciones visitadas
    visited = set([start])
    
    # Contador de estados visitados
    states_visited = 0
    
    while queue:
        (current, path) = queue.popleft()
        states_visited += 1  # Incrementar el contador al visitar un estado
        
        if current == goal:
            return path, len(visited)    # Devuelvo el camino y el número de estados visitados
        
        # Exploro los vecinos moviéndome en las 4 direcciones
        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            
            if (0 <= neighbor[0] < len(grid)) and (0 <= neighbor[1] < len(grid[0])):  # Verificar límites
                # Me fijo que no sea un agujero y que no haya pasado por este camino
                if neighbor not in visited and grid[neighbor[0]][neighbor[1]] in ('F', 'G'): 
                    queue.append((neighbor, path + [neighbor]))
                    visited.add(neighbor)
    
    return None, len(visited)  


def dfs(grid, start, goal):
    """ 
    grid: La matriz del entorno (custom_map)
    start: Tupla (x, y) de la posición inicial ('S')
    goal: Tupla (x, y) de la posición del objetivo ('G')
    
    return: Lista de tuplas que representan el camino desde el inicio al objetivo o None si no hay camino.
    """
    # Direcciones de movimiento: izquierda, abajo, derecha, arriba
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    # Pila para DFS: (current, path) donde path lleva una lista del camino recorrido
    stack = [(start, [start])]
    
    # Posiciones visitadas
    visited = set([start])
    count = 0
    
    while stack:
        current, path = stack.pop()
        count += 1

        if current == goal:
            return path, count  # Devuelvo el camino desde S hasta G y la cantidad de estados visitados
        
        # Exploro los vecinos moviéndome en las 4 direcciones pero en orden inverso
        for direction in reversed(directions):
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            
            # Verificar límites
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]):
                # Verificar que el vecino no sea un obstáculo y no esté visitado
                if neighbor not in visited and grid[neighbor[0]][neighbor[1]] in ('F', 'G'):
                    # Agrego el vecino a la pila con su camino actualizado
                    stack.append((neighbor, path + [neighbor]))
                    visited.add(neighbor)

    return None, count  # Si no hay solución, devuelvo None


def dfs_limited(grid, start, goal, limit):
    """ 
    grid: La matriz del entorno (custom_map)
    start: Tupla (x, y) de la posición inicial ('S')
    goal: Tupla (x, y) de la posición del objetivo ('G')
    limit: Límite de profundidad para la búsqueda
    
    return: Lista de tuplas que representan el camino desde el inicio al objetivo
            o None si no hay camino dentro del límite de profundidad.
    """
    # Direcciones de movimiento: izquierda, abajo, derecha, arriba
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    # Pila para DFS: (current, path, depth) donde depth lleva el nivel de profundidad actual
    stack = [(start, [start], 0)]
    
    # Posiciones visitadas
    visited = set([start])
    
    while stack:
        current, path, depth = stack.pop()
        
        if current == goal:
            return path , len(visited)  # Devuelvo el camino desde S hasta G
        
        # Si la profundidad actual es menor que el límite, continúo explorando
        if depth < limit:
            # Exploro los vecinos moviéndome en las 4 direcciones, pero en orden inverso
            for direction in directions:
                neighbor = (current[0] + direction[0], current[1] + direction[1])
                
                if (0 <= neighbor[0] < len(grid)) and (0 <= neighbor[1] < len(grid[0])):  # Verificar límites
                    # Me fijo que no sea un agujero y que no haya pasado por este camino
                    if neighbor not in visited and grid[neighbor[0]][neighbor[1]] in ('F', 'G'):
                        # Agrego el vecino al stack con la profundidad incrementada
                        stack.append((neighbor, path + [neighbor], depth + 1))
                        visited.add(neighbor)
    
    return None , len(visited)

def ucs_c1(grid, start, goal):
    """ 
    grid: La matriz del entorno (custom_map)
    start: Tupla (x, y) de la posición inicial ('S')
    goal: Tupla (x, y) de la posición del objetivo ('G')
    
    return: Lista de tuplas que representan el camino desde el inicio al objetivo
            y la cantidad de estados visitados, o None si no hay camino.
    """
    # Direcciones de movimiento: izquierda, abajo, derecha, arriba
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    
    # Cola de prioridad para la búsqueda de costo uniforme: (cost, current, path)
    priority_queue = [(0, start, [start])]
    
    # Posiciones visitadas
    visited = set()
    
    # Contador de estados visitados
    states_visited = 0
    
    while priority_queue:
        # Extraer el nodo con el menor costo acumulado
        cost, current, path = heapq.heappop(priority_queue)
        
        if current in visited:
            continue
        
        # Marcar el nodo como visitado
        visited.add(current)
        states_visited += 1  # Incrementar el contador al visitar un estado
        
        if current == goal:
            return path, states_visited  # Devuelvo el camino y el número de estados visitados
        
        # Exploro los vecinos moviéndome en las 4 direcciones
        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            
            if (0 <= neighbor[0] < len(grid)) and (0 <= neighbor[1] < len(grid[0])):  # Verificar límites
                # Si el vecino es transitable ('F' o 'G') y no ha sido visitado
                if neighbor not in visited and grid[neighbor[0]][neighbor[1]] in ('F', 'G'):
                    # El costo del movimiento es 1
                    new_cost = cost + 1
                    # Agrego el vecino a la cola de prioridad con su nuevo costo acumulado
                    heapq.heappush(priority_queue, (new_cost, neighbor, path + [neighbor]))
    
    return None, states_visited  


def ucs_c2(grid, start, goal):
    """ 
    grid: La matriz del entorno (custom_map)
    start: Tupla (x, y) de la posición inicial ('S')
    goal: Tupla (x, y) de la posición del objetivo ('G')
    
    return: Lista de tuplas que representan el camino desde el inicio al objetivo
            y la cantidad de estados visitados, o None si no hay camino.
    """
    # Direcciones de movimiento con su respectivo costo: izquierda, abajo, derecha, arriba
    directions = [((0, -1), 1), ((1, 0), 2), ((0, 1), 3), ((-1, 0), 4)]
    
    # Cola de prioridad para la búsqueda de costo uniforme: (cost, current, path)
    priority_queue = [(0, start, [start])]
    
    # Posiciones visitadas
    visited = set()

    # Contador de estados visitados
    states_visited = 0
    
    while priority_queue:
        # Extraer el nodo con el menor costo acumulado
        cost, current, path = heapq.heappop(priority_queue)
        
        if current in visited:
            continue
        
        # Marcar el nodo como visitado
        visited.add(current)
        states_visited += 1
        
        if current == goal:
            return path, states_visited  # Devuelvo el camino y los estados visitados
        
        # Explorar los vecinos moviéndome en las 4 direcciones
        for direction, move_cost in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            
            if (0 <= neighbor[0] < len(grid)) and (0 <= neighbor[1] < len(grid[0])):  # Verificar límites
                # Si el vecino es transitable ('F' o 'G') y no ha sido visitado
                if neighbor not in visited and grid[neighbor[0]][neighbor[1]] in ('F', 'G'):
                    # El costo del movimiento se ajusta según la dirección
                    new_cost = cost + move_cost
                    # Agrego el vecino a la cola de prioridad con su nuevo costo acumulado
                    heapq.heappush(priority_queue, (new_cost, neighbor, path + [neighbor]))
    
    return None, states_visited  # Devuelvo los estados visitados aunque no se haya encontrado un camino


def randomMove(grid, start, goal):
    # Direcciones de movimiento: izquierda, abajo, derecha, arriba
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    current = start
    path = [current]  
    moves = 0  
    
    while moves < 1000:  # Limitar a 1000 movimientos válidos
        if current == goal:
            return path
        
        # Movimiento aleatorio
        move = random.choice(directions)
        neighbor = (current[0] + move[0], current[1] + move[1])
        
        # Verifico los límites
        if (0 <= neighbor[0] < len(grid)) and (0 <= neighbor[1] < len(grid[0])):
            if grid[neighbor[0]][neighbor[1]] in ('F', 'G'):
                path.append(neighbor)
                current = neighbor
                moves += 1  # Contar solo los movimientos válidos
    
    return None 

def heuristic(a, b):
    """ 
    Calcula la distancia de Manhattan entre dos puntos `a` y `b`.
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
    """ 
    grid: La matriz del entorno (custom_map)
    start: Tupla (x, y) de la posición inicial ('S')
    goal: Tupla (x, y) de la posición del objetivo ('G')
    
    return: Lista de tuplas que representan el camino desde el inicio al objetivo
            o None si no hay camino. También devuelve la cantidad de estados visitados.
    """
    # Direcciones de movimiento: izquierda, abajo, derecha, arriba
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    # Cola de prioridad: (costo estimado hasta el objetivo, costo real, current, path)
    priority_queue = [(0, 0, start, [start])]
    
    # Conjunto de posiciones visitadas
    visited = set()
    
    # Contador de estados visitados
    states_visited = 0

    while priority_queue:
        # Extraer el nodo con el menor costo estimado hasta el objetivo
        estimated_cost, actual_cost, current, path = heapq.heappop(priority_queue)
        
        if current in visited:
            continue
        
        # Marcar el nodo como visitado
        visited.add(current)
        states_visited += 1

        # Si hemos llegado al objetivo, devolvemos el camino y los estados visitados
        if current == goal:
            return path, states_visited

        # Explorar los vecinos moviéndome en las 4 direcciones
        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            
            # Verificar si el vecino está dentro de los límites del grid
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]):
                # Si el vecino es transitable ('F' o 'G') y no ha sido visitado
                if neighbor not in visited and grid[neighbor[0]][neighbor[1]] in ('F', 'G'):
                    # El costo real para moverse al vecino es el costo actual más 1
                    new_actual_cost = actual_cost + 1
                    # El costo estimado es el costo real más la heurística
                    new_estimated_cost = new_actual_cost + heuristic(neighbor, goal)
                    # Agregar el vecino a la cola de prioridad
                    heapq.heappush(priority_queue, (new_estimated_cost, new_actual_cost, neighbor, path + [neighbor]))

    # Si no hay camino, devolver None y la cantidad de estados visitados
    return None, states_visited