## Reporte TP3 y TP4

### Introducción:
Se implementaron y evaluaron diversos algoritmos de búsqueda, tanto no informada como informada. Los algoritmos no informados utilizados fueron:

- **BFS** (Búsqueda en Anchura).
- **DFS** (Búsqueda en Profundidad).
- **DLS** (Búsqueda en Profundidad Limitada).
- **UCS** (Búsqueda de Costo Uniforme).

Para la búsqueda informada, se empleó el algoritmo A* , utilizando como heurística la distancia Manhattan.

Todos los algoritmos fueron evaluados en el entorno FrozenLake, considerando dos escenarios de costos:

1. Costo fijo por cada acción: 1.
2. Costo variable por acción, es decir, cada acción tiene un costo distinto.

### Marco teórico:
El entorno seleccionado para la ejecución de los algoritmos fue FrozenLake-v1 de la librería Gymnasium en Python. Este entorno simula un lago congelado representado por una cuadrícula de tamaño N x N. En la superficie del lago hay agujeros que actúan como obstáculos para el agente. El agente y el objetivo son colocados aleatoriamente en la cuadrícula, además se deshabilitó la opción "is_slippery" en el entorno para su correcta comparación.

El agente tiene la capacidad de moverse en cuatro direcciones: izquierda, abajo, derecha y arriba, las cuales se representan numéricamente de 0 a 3, respectivamente. El objetivo principal del agente es encontrar un camino que lo lleve desde su posición inicial hasta el objetivo.

En cuanto a los escenarios de costos:

En el primer escenario, todas las acciones tienen un costo uniforme de 1.
En el segundo escenario, el costo de cada movimiento depende de la dirección tomada:
- Izquierda: costo 1.
- Abajo: costo 2.
- Derecha: costo 3.
- Arriba: costo 4.

### Diseño experimental:
Para evaluar el rendimiento de los algoritmos, se diseñó un conjunto de 30 entornos simulados, cada uno con un tamaño de 100x100 celdas y un 8% de obstáculos distribuidos aleatoriamente. En estos escenarios controlados, se ejecutaron repetidamente los algoritmos BFS, DFS, DLS (con un límite de profundidad de 10), UCS (con costos fijos y variables) y A* (utilizando la heurística de Manhattan). Al someter a todos los algoritmos a las mismas condiciones, se garantizó una comparación justa y se pudo analizar su comportamiento ante desafíos idénticos.

## Análisis y discusión de resultados

#### Análisis del numero de estados
Comenzamos el análisis comparando la cantidad de estados que explora cada algoritmo.

![Imagen 1](./imagenes/Numero_de_estados.png)

En el gráfico podemos observar que el algoritmo A* destaca por visitar significativamente menos estados en comparación con los demás y que el algoritmo DLS también explora pocos estados, lo que se debe a la limitación impuesta por la profundidad máxima de 10. sin embargo a la desventaja que presenta es que no nos asegura que siempre logre encontrar la solución.

#### Análisis con respecto a los costos
A continuación, analizamos el costo de los movimientos en los dos entornos, enfocándonos solo en los casos donde se haya encontrado una solución en un máximo de 1000 acciones.

![Imagen 2](./imagenes/Comparacion_costo_e1.png)
![Imagen 3](./imagenes/Comparacion_costo_e2.png)

Se observa que a comparacion de losalgoritmos BFS, UCS y A* logran encontrar la solución óptima, el algoritmo DFS muestra el peor rendimiento independientemente del costo de sus acciones, ya que la solución que encontrada no sera optima. El algoritmo DLS tendra un costo casi nulo debido a que solo puede realizar un máximo de 10 movimientos para hallar el camino.

#### Análisis de tiempos de cada algoritmo
![Imagen 4](./imagenes/Comparacion_tiempo_ejecucion.png)

En el gráfico, se destaca que el algoritmo A* demora significativamente menos tiempo que los demás en encontrar la solucion optima. Esto se debe a que, al ser un algoritmo de búsqueda informada, explora una menor cantidad de estados.

#### Análisis de las soluciones encontradas
![Imagen 5](./imagenes/Cantidad_soluciones.png)

A partir de este gráfico, podemos concluir que aunque el algoritmo DLS explora menos estados y consume menos tiempo que otros, esto no lo convierte en el mejor, ya que encuentra la solución en muy pocas ocasiones debido a su limitación de profundidad de 10. Algo similar ocurre con el algoritmo DFS, que consume mucho más tiempo y presenta un mayor costo de acciones. Además, DFS encuentra la solución en un número reducido de veces, ya que está limitado a un máximo de 1000 acciones para hallarla.

### Conclusiones

En este trabajo se implementaron y evaluaron varios algoritmos de búsqueda, tanto informada como no informada, en el entorno FrozenLake. Los algoritmos BFS, DFS, DLS, UCS y A* fueron analizados en términos de la cantidad de estados explorados, el costo de las soluciones encontradas, el tiempo de ejecución y la cantidad de veces que lograron encontrar una solución.

En este estudio comparativo, el algoritmo A* se destacó significativamente como la estrategia de búsqueda más eficiente para resolver el problema del FrozenLake. Su superioridad se atribuye principalmente a la incorporación de una función heurística que estima la distancia al nodo objetivo. permitiendo al agente explorar el espacio de búsqueda de manera más focalizada, evitando expandir nodos innecesarios.

Sin embargo, es importante destacar que la eficiencia de A* depende en gran medida de la calidad de la heurística utilizada. Una heurística admisible (que nunca sobreestima el costo real al objetivo) garantiza que A* encuentre siempre una solución óptima, pero una heurística más informativa puede acelerar aún más la búsqueda.

A* será mejor opción cuando se busque un balance entre tiempo de ejecución y calidad de la solución, mientras que los algoritmos como DFS y DLS resultan menos efectivos en escenarios con grandes limitaciones de recursos o profundidad.
