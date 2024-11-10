import tablero
import random
import math
def generateNeighBors(column , table , neighbors):
    # Genero los vecinos para una columna en particular
    current_row = table[column]
    for row in range(len(table)):
        if (row != current_row):
            new_table = table.copy()
            new_table[column] = row
            neighbors.append(new_table)
    return neighbors

def generateAllNeighbors(table):
    # Genero los vecinos para todas las columnas
    size = len(table)
    neighbors = []
    for column in range(size):
        generateNeighBors(column,table,neighbors)
    return neighbors


def findBestNeighbord(table):

    neighbors = generateAllNeighbors(table)
    min_conflicts = sum(tablero.checkConflicts(table))
    best_neighbors = [table]

    for neighbor in neighbors:
        conflicts = sum(tablero.checkConflicts(neighbor))
        if conflicts < min_conflicts:
            best_neighbors = [neighbor]
            min_conflicts = conflicts
        elif conflicts == min_conflicts:
            best_neighbors.append(neighbor)

    # Elijo el vecino de manera aleatoria entre los mejores
    best_neighbor = random.choice(best_neighbors)
    return best_neighbor, min_conflicts

def hillClimbing(table):

    current_table = table
    current_conflicts = sum(tablero.checkConflicts(current_table))
    moves = 0
    h_e_list = []

    while current_conflicts > 0 and moves < 1000:
        best_neighbor, min_conflicts = findBestNeighbord(current_table)
        h_e_list.append(min_conflicts)
        
        if min_conflicts < current_conflicts:
            current_table = best_neighbor
            current_conflicts = min_conflicts
        else:
            break  # No hay mejor vecino, salimos del bucle

        moves += 1
    
    return best_neighbor , min_conflicts , moves , h_e_list



def simulatedAnnealing(initial_table, initial_temp=1000, cooling_rate=0.90, max_iter=1000):
    current_table = initial_table
    current_conflicts = sum(tablero.checkConflicts(current_table))
    temp = initial_temp
    best_table = current_table
    best_conflicts = current_conflicts

    # Almaceno el historial de la cantidad de reinas atacadas hasta encontrar la solucion
    h_e_list = []
    h_e_list.append(best_conflicts)

    moves = 1
    for _ in range(max_iter-1):
        neighbors = generateAllNeighbors(current_table)
        next_table = random.choice(neighbors)
        next_conflicts = sum(tablero.checkConflicts(next_table))
        
        if next_conflicts < best_conflicts:
            best_table = next_table
            best_conflicts = next_conflicts
        
        # Decide si aceptamos el siguiente estado basado en la probabilidad
        if next_conflicts < current_conflicts or random.uniform(0, 1) < math.exp((current_conflicts - next_conflicts) / temp):
            current_table = next_table
            current_conflicts = next_conflicts
        
        # Reduzco la temperatura
        temp *= cooling_rate
        moves += 1
        h_e_list.append(current_conflicts)

        if current_conflicts == 0:
            break

    return best_table,best_conflicts , moves, h_e_list

def setNumPopulation(size):
    # El primer valor es la poblacion y el segundo es la particion para la seleccion por torneo
    if size == 4:
        return 20 , 4
    elif size == 8:
        return 100 , 10
    elif size == 10:
        return 150 , 15 
    elif size == 12:
        return 200 , 20
    else:
        return 250 , 25

def generatePopulation(size):
    # Genero la poblacion inicial
    population = []
    num_population, partition = setNumPopulation(size)

    for i in range(num_population):
        population.append(tablero.generarTablero(size))
    
    return population , partition

def fitness(table):
    total_conflicts = sum(tablero.checkConflicts(table)) // 2 # Par de reinas atacandose entre si
    n = len(table)
    total_pairs = (n * (n-1) ) // 2 # Numero total de pares de reinas posibles
    return total_pairs - total_conflicts # Numero de pares de reinas que no se atacan.

def tournament(population_list):

    best_parent , best_fitness = population_list[0]

    for (parent,fitness) in population_list:
        if fitness > best_fitness:
            best_parent = parent
            best_fitness = fitness
    
    return best_parent , best_fitness



def selectParents(population_fitness , partition):
    
    size = len(population_fitness)
    step = size // partition
    parents = []
    for i in range(0 , partition):
        if (i == step-1):
            end = size
        else: 
            end = (i+1) * step

        start = i * step
        new_list = population_fitness[start:end]
        best_parent , best_fitness = tournament(new_list)
        parents.append((best_parent,best_fitness))

    return parents

def crossover(parent1 , parent2 , crossing_point , size):
    children1 = []
    children2 = []
    for i in range(size):
        if i < crossing_point:
            children1.append(parent1[i])
            children2.append(parent2[i])
        else:
            children1.append(parent2[i])
            children2.append(parent1[i])
    return children1 , children2

def totalFitness(parents):
    sum = 0
    for (_,fitness) in parents:
        sum += fitness
    return sum

def selectionProbability(fitness , total_fitness):
    return (fitness/total_fitness) 

def calculateProbabilities(parents, total_fitness):
    probabilities = []
    for (_ , fitness) in parents:
        probabilities.append(selectionProbability(fitness,total_fitness))
    
    return probabilities # Devuelvo los padres con su probabilidad de ser seleccionado

def mutation(children):
    probability = 0.05
    mutation = random.choices([True,False], weights=[probability, 1 - probability],k=1)[0]
    if (mutation):
        random_column = random.randint(0,len(children)-1)
        random_row = random.randint(0,len(children)-1)
        children[random_column] = random_row
    return children

def parentsCrossover(parents, total_population, size):
    childrens = []
    total_fitness = totalFitness(parents)
    probabilidades = calculateProbabilities(parents, total_fitness)

    while len(childrens) < total_population:
        parent1 = random.choices(parents, weights =probabilidades, k=1)[0]
        parent2 = random.choices(parents, weights =probabilidades, k=1)[0]
        crossing_point = random.randint(1,size-1) # Minimo un elemento de un padre
        children1 , children2 = crossover(parent1[0], parent2[0], crossing_point, size)
        # Muteacion a los hijos con cierta probabilidad
        children1 = mutation(children1)
        children2 = mutation(children2)
        childrens.append(children1)
        if len(childrens) < total_population:
            childrens.append(children2)

    return childrens

def fitnessList(list):
    return [fitness(table) for table in list]

def populationFitness(population , fitness_list): # Devuelvo la tupla (individuo,fitness)
    return list(zip(population,fitness_list))

def geneticAlgorithm(size):

    # Devuelvo la cantidad de poblacion y el tamaño de la particion
    population , partition = generatePopulation(size) 
    
    # Calculo el fitness a cada individuo de la poblacion
    fitness_list = fitnessList(population)

    # Lista que almacena el par de reinas amenazadas hasta encontrar o no la solución
    h_e_list = []

    # Devuelvo una tupla con (individuo,fitness)
    population_fitness = populationFitness(population,fitness_list)
    #print(f"Poblacion total: {population_fitness}")

    # Calculo los padres para la siguiente generacion con su fitness
    parents = selectParents(population_fitness,partition)
    #print(f"Mejores padres: {parents}")
    generation = 1000
    max_possible_fitness = (size * (size - 1)) // 2 # Maximo de reinas sin atacarse

    while generation > 0:
        childrens = parentsCrossover(parents , len(population), size) # Obtengo los hijos
        fitness_list = fitnessList(childrens) # Calculo el fitness a los hijos

        max_fitness = max(fitness_list)
        if (max_fitness == max_possible_fitness):
            h_e_list.append(max_possible_fitness - max_fitness)
            index = fitness_list.index(max_fitness) # Indice del hijo con mayor fitness
            #print(f"Encontramos el mejor hijo: {childrens[index]} , {fitness_list[index]}")
            return childrens[index] , (max_possible_fitness - fitness_list[index]) , 1001 - generation , h_e_list

        h_e_list.append(max_possible_fitness - max_fitness)
        population_fitness = populationFitness(childrens,fitness_list) # Uno en una tupla
        parents = selectParents(population_fitness,partition) # Torneo para la seleccion de padres
        generation -= 1

    index = max(fitness_list)
    # Le tomo 1000 generaciones y no encontró la solución
    return childrens[index] , (max_possible_fitness - fitness_list[index]) , 1000 , h_e_list