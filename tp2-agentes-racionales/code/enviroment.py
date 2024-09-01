import random


_CLEAN_CELL = 0
_DIRTY_CELL = 1
_CLEANED = 2

class Environment:
    def __init__(self,sizeX,sizeY,dirt_rate: float) -> None:

        self.sizeX = sizeX
        self.sizeY = sizeY
        self.dirt_rate = dirt_rate
        self.grid = create_grid(sizeX, sizeY)
        self.dirty_cells = round(sizeX * sizeY * dirt_rate)
        self.random_dirty(self.dirty_cells)


    def create_grid(sizeX: int, sizeY: int) -> grid:
        return [[_CLEAN_CELL for _ in range(sizeY)] for _ in range(sizeX)] # Creo una matriz de un tamaño especifico marcando como limpio cada espacio
        
    
    def random_dirty(self, dirty_cells: int) -> None: # Randomizo las posiciones sucias iniciales, si la casilla ya esta sucia entonces se intenta con otra

        grid = self.grid
        count = 0
        while count < dirty_cells:

            Xpos = random(0, (self.sizeX - 1))
            Ypos = random(0, (self.sizeY - 1))

            if not is_dirty(grid):  
                grid[Xpos][Ypos] = _DIRTY_CELL
                count += 1
            


    def accept_action(self, action: String, Xpos: int, Ypos: int) -> bool:

        # Movimientos posibles
        moves = {
            "Up": (1, 0),
            "Down": (-1, 0),
            "Right": (0, 1),
            "Left": (0, -1)
        }

        if action in moves:
            x, y = moves[action]
            movX, movY = Xpos + x, Ypos + y

            return (0<= movX < self.sizeX) and (0 <= movY < self.sizeY)
        
        if action == "Suck":
            if self.is_dirty(Xpos, Ypos):
                self.grid[Xpos][Ypos] = _CLEANED
                self.dirty_cells -= 1
                return True

    
    def is_dirty(self, Xpos: int, Ypos: int) -> bool:
        return self.grid[Xpos][Ypos] == _DIRTY_CELL
    
    def get_dirty(self):
        return self.dirty

    def print_environment(self) -> None:
        print(f'{[[self.grid[x][y] for y in range(self.sizeY)] for x in range(self.sizeX)]}')

