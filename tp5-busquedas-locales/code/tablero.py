import random

class Tablero:
    def __init__(self, size: int) -> None:
        self.size = size
        self.grid = self.map_creation(size)
        self.place_queens()
        self.visited_states = []

    def map_creation(self, N: int):
        grid = [[{'state': 0} for _ in range(N)] for _ in range(N)]
        return grid

    def place_queens(self):
        # Coloca una reina en cada columna
        for i in range(self.size):
            self.grid[0][i]['state'] = 1

    def calculate_heuristic(self):
        conflicts = 0
        # reviso reinas en conflicto
        for row in range(self.size):
            for col in range(self.size):
                if self.grid[row][col]['state'] == 1:
                    conflicts += self.count_conflicts(row, col)

        # Dividimos entre 2 para no contar conflictos ya calculados
        return conflicts // 2

    def count_conflicts(self, row, col):
        conflicts = 0
        
        # Verificar misma fila
        for i in range(self.size):
            if i != col and self.grid[row][i]['state'] == 1:
                conflicts += 1

        # Verificar diagonal principal (i - j == row - col)
        for i in range(self.size):
            diag_col = col + (i - row)
            if 0 <= diag_col < self.size and i != row and self.grid[i][diag_col]['state'] == 1:
                conflicts += 1

        # Verificar diagonal secundaria (i + j == row + col)
        for i in range(self.size):
            diag_col = col - (i - row)
            if 0 <= diag_col < self.size and i != row and self.grid[i][diag_col]['state'] == 1:
                conflicts += 1

        return conflicts
    
    def record_state(self):
        # Registra el estado actual como una lista de posiciones de reinas en cada columna
        state = [next(row for row in range(self.size) if self.grid[row][col]['state'] == 1) for col in range(self.size)]
        self.visited_states.append(state)


    def map_print(self):
        for row in self.grid:
            print(' | '.join([str(cell['state']) for cell in row]))
        print(' ')

class Solution:
    def __init__(self, solution, visited_states):
        self.solution = solution
        self.visited_states = visited_states

