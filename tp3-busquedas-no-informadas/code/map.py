import gymnasium as gym
import random


class Map():
    def __init__(self, size: int, h_ratio: float, start, end):
    
        self.size = size
        self.h_ratio = h_ratio
        self.start = start
        self.end = end

        self.grid_holes = round(size * size * h_ratio)

        (custom_map,self.grid) = self.generate_random_map_custom(size, start, end)
        self.env = gym.make('FrozenLake-v1', desc=custom_map, is_slippery=False, render_mode='human')
        self.env = gym.wrappers.TimeLimit(self.env, max_episode_steps=1000) # Máximo 1000 acciones


    def generate_random_map_custom(self, size, start, end):

        mapa = [['F' for _ in range(size)] for _ in range(size)]

        for _ in range(self.grid_holes):
            posX = random.randint(0, size - 1)
            posY = random.randint(0, size - 1)
            mapa[posX][posY] = 'H'  # Marco la casilla como Agujero 

        # De esta manera me aseguro que 'start' y 'end' no son agujeros

        mapa[start[0]][start[1]] = 'S'
        mapa[end[0]][end[1]] = 'G'
        return [''.join(row) for row in mapa] , mapa  #formateo la salida a la requerida por frozen lake
        
        
    
        



        
