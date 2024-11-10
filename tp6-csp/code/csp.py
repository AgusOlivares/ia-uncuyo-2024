import copy

class Board:
    def __init__(self, long):
        self.long = long
        self.dominio = [list(range(long)) for _ in range(long)]  # Listas de posibles valores (columnas) para cada fila
        self.solution = [None for _ in range(long)]  # Solución actual (una reina por fila)

    def check(self, row, value):
        # Verificar si la solución es válida hasta la fila `row`
        for i in range(self.long):
            if self.solution[i] is not None:
                # Comprobar si están en la misma columna o diagonal
                if self.solution[i] == value or abs(value - self.solution[i]) == abs(row - i):
                    return False
        return True

    def finished(self):
        # Comprobar si todas las posiciones de la solución están llenas (es decir, todas las reinas están ubicadas)
        return all(elemento is not None for elemento in self.solution)

    def choose_index(self):
        # Elegir la fila con el menor número de posibles valores en el dominio (heurística de mínima cantidad de opciones)
        low_index = None
        low_amount = float("inf")

        for index, element in enumerate(self.dominio):
            if self.solution[index] is None and len(element) < low_amount:
                low_amount = len(element)
                low_index = index

        return low_index

    def print_solution(self):
        for i in range(self.long):
            linea = ['.'] * self.long
            if self.solution[i] is not None:
                linea[self.solution[i]] = 'Q'  # Usar 'Q' para representar la posición de la reina
            print(' '.join(linea))


def forward_checking(board, row, value):
    # Actualizar el dominio eliminando los valores que no se pueden utilizar (basado en la nueva asignación)
    aux = 1
    for i in range(row + 1, board.long):
        # Remover el valor de la columna actual en filas posteriores
        if value in board.dominio[i]:
            board.dominio[i].remove(value)

        # Calcular las diagonales hacia adelante y hacia atrás
        back_diagonal = value - aux
        forward_diagonal = value + aux

        # Remover valores de la diagonal hacia atrás si está dentro del rango
        if 0 <= back_diagonal < board.long:
            if back_diagonal in board.dominio[i]:
                board.dominio[i].remove(back_diagonal)

        # Remover valores de la diagonal hacia adelante si está dentro del rango
        if 0 <= forward_diagonal < board.long:
            if forward_diagonal in board.dominio[i]:
                board.dominio[i].remove(forward_diagonal)

        aux += 1
    return board


def ac_3(board, contador_evaluaciones=0):
    # Si ya se colocaron todas las reinas, terminar la búsqueda
    if board.finished():
        return True, contador_evaluaciones

    # Elegir la fila con el menor número de posibles valores
    index = board.choose_index()

    # Probar cada valor posible en la fila elegida
    for value in board.dominio[index]:
        # Contar la evaluación de cada valor
        contador_evaluaciones += 1

        if board.check(index, value):
            # Guardar el estado actual del dominio antes de asignar un valor (deepcopy para copiar toda la estructura)
            possible_values = copy.deepcopy(board.dominio)

            # Aplicar forward checking para actualizar el dominio
            forward_checking(board, index, value)

            # Asignar el valor actual a la solución
            board.solution[index] = value

            # Llamar a la recursión con la nueva asignación
            condition, contador_evaluaciones = ac_3(board, contador_evaluaciones)

            # Si encontramos una solución válida, regresar True
            if condition:
                return True, contador_evaluaciones

            # Restaurar el dominio si la asignación no lleva a una solución
            board.dominio = possible_values

    # Deshacer la asignación si no se encuentra solución en esta rama
    board.solution[index] = None
    return False, contador_evaluaciones


# Ejemplo de uso con un tablero de 8x8
board = Board(4)
resultado, contador_evaluaciones = ac_3(board)
print("Solución encontrada:", board.solution)
print(f"Evaluaciones realizadas: {contador_evaluaciones}")  # Mostrar el conteo de evaluaciones
board.print_solution()