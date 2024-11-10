import random
def generarTablero(size):
    
    table = []
    for _ in range(size):
        row = random.randint(0,size-1)
        table.append(row)
    return table

def checkRows(column , table):

    queens = 0
    row = table[column]
    for i in range(0,len(table)):
        if i == column:
            continue
        if row == table[i]:
            queens += 1
    return queens

def checkDiagonals(column , table):
    
    queens = 0
    row = table[column]
    # Si esta en la diagonal verifica que abs(columna2-columna1) == abs(fila2 - fila1)
    for i in range(0,len(table)):
        if i == column:
            continue
        if (abs(column-i) == abs(row - table[i])):
            queens += 1

    return queens

def checkConflicts(table):

    queens = []
    size = len(table)
    for i in range(0,size):
        queens.append(checkRows(i,table) + checkDiagonals(i,table))
    return queens

def printTablero(table):
    size = len(table)
    
    # Recorre cada fila
    for row in range(size):
        line = ""
        # Recorre cada columna
        for col in range(size):
            if table[col] == row:
                line += "Q "  # Representa una reina
            else:
                line += ". "  # Representa un espacio vacío
        print(line)
    print("\n")