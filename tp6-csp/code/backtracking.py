def crear_matriz(n):
    """Crear una matriz de tamaño n, donde cada posición contiene una lista con los valores de 0 a n-1."""
    return [list(range(n)) for _ in range(n)]


def remover_valor_excepto_fila(matriz, valor_a_remover, fila_excluida):
    """Eliminar el valor en todas las filas excepto en la fila excluida."""
    for index, fila in enumerate(matriz):
        if index == fila_excluida or isinstance(fila, int):
            continue
        if valor_a_remover in fila:
            fila.remove(valor_a_remover)
    return matriz


def estan_en_diagonal(vector, n):
    """Verificar si hay elementos en diagonal conflictiva."""
    for fila1 in range(n):
        if vector[fila1] is None or isinstance(vector[fila1], list):
            continue
        for fila2 in range(fila1 + 1, n):
            if vector[fila2] is None or isinstance(vector[fila2], list):
                continue
            if abs(fila1 - fila2) == abs(vector[fila1] - vector[fila2]):
                return True
    return False


def posicion_con_menos_valores(vector):
    """Encontrar el índice de la fila con la menor cantidad de opciones."""
    min_valores = float('inf')  # Inicializamos con infinito
    indice_menor = None

    for index, valor in enumerate(vector):
        if isinstance(valor, list) and len(valor) > 1:
            if len(valor) < min_valores:  # Buscar la lista con menos elementos
                min_valores = len(valor)
                indice_menor = index

    return indice_menor


def vuelta_atras_recursiva(asignacion, n, contador_evaluaciones=0):
    """Implementar la búsqueda con vuelta atrás para resolver el problema."""
    # Obtener el índice con menos opciones de asignación
    index = posicion_con_menos_valores(asignacion)

    # Si no hay ninguna posición con más de un valor, se ha encontrado una solución
    if index is None:
        return asignacion, contador_evaluaciones

    # Obtener las opciones en esa posición (lista de valores posibles)
    opciones = asignacion[index]

    # Crear una copia de la asignación para restaurar en caso de errores
    copia_asignacion = [list(fila) if isinstance(fila, list) else fila for fila in asignacion]

    for valor in opciones:
        # Incrementar el contador por cada evaluación de valor
        contador_evaluaciones += 1

        # Asignar el valor actual y removerlo de las demás filas
        asignacion[index] = valor
        remover_valor_excepto_fila(asignacion, valor, index)

        # Si no hay valores en diagonal, continuar con la recursión
        if not estan_en_diagonal(asignacion, n):
            resultado, contador_evaluaciones = vuelta_atras_recursiva(asignacion, n, contador_evaluaciones)
            if resultado is not None:
                return resultado, contador_evaluaciones  # Solución encontrada

        # Revertir la asignación en esta posición
        asignacion = [list(fila) if isinstance(fila, list) else fila for fila in copia_asignacion]

    return None, contador_evaluaciones  # No se encontró solución
    return None  # No se encontró solución




def mostrar_tablero(asignacion, n):
    """Función para mostrar el resultado como un tablero."""
    print("\nSolución encontrada:")
    for fila in range(n):
        # Si la asignación de la fila es un entero, lo mostramos
        if isinstance(asignacion[fila], int):
            tablero = ['.'] * n
            tablero[asignacion[fila]] = 'Q'  # Colocar la reina en la columna correspondiente
            print(" ".join(tablero))
        elif isinstance(asignacion[fila], list) and len(asignacion[fila]) == 1:
            tablero = ['.'] * n
            tablero[asignacion[fila][0]] = 'Q'
            print(" ".join(tablero))
        else:
            print("[Error] La fila no tiene un valor asignado correctamente.")  # Esto no debería ocurrir si la solución es válida

def busqueda_vuelta_atras(n):
    """Función principal para buscar la solución con vuelta atrás."""
    asignacion_inicial = crear_matriz(n)
    return vuelta_atras_recursiva(asignacion_inicial, n)


# Prueba del código y visualización
n = 4  # Tamaño del tablero
resultado, contador_evaluaciones = busqueda_vuelta_atras(n)
print(f"Evaluaciones realizadas: {contador_evaluaciones}")  # Mostrar el conteo de evaluaciones

if resultado:
    mostrar_tablero(resultado, n)
else:
    print("No se encontró una solución.")