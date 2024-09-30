import random
import numpy as np
from collections import deque
import heapq



def dfs(grid, start, goal):

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # Arriba, Abajo, Izquierda, Derecha

    
    stack = [(start, [start])] # Pila para DFS: (current, path) donde path lleva una lista del camino recorrido
    
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



def bfs(self, start, goal):
    
    directions = [(0, 1), (0, -1), (1, 0),(-1, 0)] # Arriba, Abajo, Izquierda, Derecha

    queue = deque([(start, [start])])

    visited = set([start])

    states_v = 0

    while queue:
        (current, path) = queue.popleft()
        states_visited += 1  # Incrementar el contador al visitar un estado
        
        if current == goal:
            return path, len(visited)    # Devuelvo el camino y el número de estados visitados
        
        # Exploro los vecinos
        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            
            if (0 <= neighbor[0] < len(grid)) and (0 <= neighbor[1] < len(grid[0])):  # Verificar límites
                # Me fijo que no sea un agujero y que no haya pasado por este camino
                if neighbor not in visited and grid[neighbor[0]][neighbor[1]] in ('F', 'G'): 
                    queue.append((neighbor, path + [neighbor]))
                    visited.add(neighbor)
    
    return None, len(visited)  

def dfs_limited(grid, start, goal, limit):

    directions = [(0, 1), (0, -1), (1, 0),(-1, 0)] # Arriba, Abajo, Izquierda, Derecha

    # Pila para DFS: (current, path, depth) donde depth lleva el nivel de profundidad actual
    stack = [(start, [start], 0)]
    
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
                
                if (0 <= neighbor[0] < len(grid)) and (0 <= neighbor[1] < len(grid[0])):  # Verifico limites
                    # Me fijo que no sea un agujero y que no haya pasado por este camino
                    if neighbor not in visited and grid[neighbor[0]][neighbor[1]] in ('F', 'G'):
                        # Agrego el vecino al stack con la profundidad incrementada
                        stack.append((neighbor, path + [neighbor], depth + 1))
                        visited.add(neighbor)
    
    return None , len(visited)


def ucs_costo1(grid, start, goal):

    directions = [(0, 1), (0, -1), (1, 0),(-1, 0)] # Arriba, Abajo, Izquierda, Derecha
    
    priority_queue = [(0, start, [start])]
    
    visited = set()
    
    states_visited = 0
    
    while priority_queue:
        
        cost, current, path = heapq.heappop(priority_queue)
        
        if current in visited:
            continue
        
        visited.add(current)
        states_visited += 1 
        
        if current == goal:
            return path, states_visited  
        
        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            
            if (0 <= neighbor[0] < len(grid)) and (0 <= neighbor[1] < len(grid[0])):  

                if neighbor not in visited and grid[neighbor[0]][neighbor[1]] in ('F', 'G'):
                    
                    new_cost = cost + 1
                    
                    heapq.heappush(priority_queue, (new_cost, neighbor, path + [neighbor]))
    
    return None, states_visited  


def ucs(grid, start, goal):


    directions = [((0, 1), 3), ((0, -1), 2), ((1, 0), 1),((-1, 0), 4)] # Arriba, Abajo, Izquierda, Derecha con costos asociados
    
    priority_queue = [(0, start, [start])] # Cola de prioridad para la búsqueda de costo uniforme: (cost, current, path)
    
    visited = set()

    states_visited = 0 # Contador 
    
    while priority_queue:

        cost, current, path = heapq.heappop(priority_queue) # Extraigo nodo de menor costo acumulado
        
        
        if current in visited:
            continue
        
        visited.add(current) #Agrego el nodo actual a los nodos visitados
        
        states_visited += 1
        
        if current == goal:
            return path, states_visited  # Devuelvo el camino y los estados visitados
        
        # Explorar los vecinos
        for direction, move_cost in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            
            if (0 <= neighbor[0] < len(grid)) and (0 <= neighbor[1] < len(grid[0])):  # Verificar límites
                # Si el vecino es transitable ('F' o 'G') y no ha sido visitado
                if neighbor not in visited and grid[neighbor[0]][neighbor[1]] in ('F', 'G'):
                    # Ajusto el costo segun la direccion
                    new_cost = cost + move_cost
                    # Agrego el vecino a la cola de prioridad con su nuevo costo acumulado
                    heapq.heappush(priority_queue, (new_cost, neighbor, path + [neighbor]))
    
    return None, states_visited  # Devuelvo caminos visitados aunque no se haya alcanzado el objetivo

