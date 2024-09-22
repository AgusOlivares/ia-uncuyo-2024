import random


class Environment:
    def __init__(self, sizeX, sizeY, dirt_rate: float):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.dirt_rate = dirt_rate
        self.grid = self.create_grid(sizeX, sizeY)
        self.dirty_cells = round(sizeX * sizeY * dirt_rate)
        self.random_dirty(self.dirty_cells)

    def create_grid(self, sizeX: int, sizeY: int):
        return [[0 for _ in range(sizeY)] for _ in range(sizeX)]

    def random_dirty(self, dirty_cells: int): # genero casillas sucias aleatoriamente
        for _ in range(self.dirty_cells):
            pos_x = random.randint(0, self.sizeX - 1)
            pos_y = random.randint(0, self.sizeY - 1)
            self.grid[pos_x][pos_y] = 1  
        

    def acceptAction(self, action, Xpos: int, Ypos: int) -> bool:
        moves = {
            "Up": (1, 0),
            "Down": (-1, 0),
            "Right": (0, 1),
            "Left": (0, -1)
        }

        if action in moves:
            movX, movY = moves[action] 
            new_x, new_y = Xpos + movX, Ypos + movY
            
            # Verifico que no me salga de la matriz
            return (0 <= new_x < self.sizeX) and (0 <= new_y < self.sizeY)
        
        elif action == "Clean":
            if self.is_dirty(Xpos, Ypos):
                self.grid[Xpos][Ypos] = 0
                self.dirty_cells -= 1
                return True
            return False
        
        return False   

    def is_dirty(self, Xpos: int, Ypos: int):
        return (self.grid[Xpos][Ypos] == 1)

    def get_dirty(self):
        return self.dirty_cells

    def print_environment(self):
        print(f'{[[self.grid[x][y] for y in range(self.sizeY)] for x in range(self.sizeX)]}')