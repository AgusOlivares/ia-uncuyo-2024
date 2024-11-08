import gymnasium as gym
import random

class Map():
    def __init__(self, size , p_hole,start,end):
        self.size = size 
        self.p_hole = p_hole
        self.start = start
        self.end = end
        self.grid_holes = round(size * size * p_hole)

        (custom_map,self.grid) = self.generate_custom_map(size, start, end)
        self.env = gym.make('FrozenLake-v1', desc=custom_map, is_slippery=False, render_mode='human')
        self.env = gym.wrappers.TimeLimit(self.env, max_episode_steps=1000) # Máximo 1000 acciones

    def generate_custom_map(self, size, start, end):
        """
        size: Tamaño del mapa (por ejemplo, 100 para un mapa de 100x100)
        p_hole: Probabilidad de que una celda sea un agujero (valor entre 0 y 1)
        
        return: Lista de cadenas que representan al mapa para el formato de FrozenLake y el Mapa como matriz
        """
        map_array = [['F' for _ in range(size)] for _ in range(size)]
        map_array = self.holes_grid(size ,map_array)

        # Asegurar que la posición inicial y la meta no sean agujeros
        map_array[start[0]][start[1]] = 'S'
        map_array[end[0]][end[1]] = 'G'
        
        # Convierto el mapa a la lista de cadenas que requiere FrozenLake
        return [''.join(row) for row in map_array] , map_array
    
    def holes_grid(self,size, map_array):
        
        for _ in range(self.grid_holes):
            pos_x = random.randint(0, size - 1)
            pos_y = random.randint(0, size - 1)
            map_array[pos_x][pos_y] = 'H'  # Marco la casilla como Agujero 
        return map_array