# Trabajo Práctico 6: Satisfacción de restricciones 

### 1) Describir en detalle una formulación CSP para el Sudoku

En una formulación CSP para Sudoku, las variables corresponden a cada celda del tablero. El dominio de cada variable es el conjunto {1, 2, ..., 9}. Las restricciones imponen la unicidad de los valores en cada fila, columna y subcuadrícula, asegurando así la solución única del puzzle.

### 2) Utilizar el algoritmo AC-3 para demostrar que la arco consistencia puede detectar la inconsistencia de la asignación parcial WA=red, V=blue para el problema de colorear el mapa de Australia.

Utilizaremos el algoritmo AC-3 para detectar la inconsistencia con la asignación parcial WA = Red , V = Blue. Es decir que cuando lleguemos a un punto en el que tengamos una variable X<sub>i</sub> con dominio vacío, no tendremos solución para esta asignación parcial.

*Nota*: Se asignará R = Red , G = Green y B = Blue.

Dominio inicial del problema:
- D(WA) = {R}
- D(NT) = {R,B,G}
- D(SA) = {R,B,G}
- D(Q) = {R,B,G}
- D(NSW) = {R,B,G}
- D(V) = {B}
Una posible ordenación de los arcos para este ejemplo es:
Q = {(SA->WA), (SA->V), (NT->SA), (NSW->V), (NSW->SA), (Q->NSW), (Q->SA), (NT->Q), (NT->WA)}

Algoritmo:
1. SA->WA : Elimino R del dominio SA, D(SA) = {B,G}
2. SA->V : Elimino B del dominio SA, D(SA) = {G}
3. NT->SA : Elimino G de NT, D(NT) = {R,B}
4. NSW->V : Elimino B de NSW, D(NSW) = {R,G}
5. NSW->SA : Elimino G de NSW, D(NSW) = {R}
6. Q->NSW : Elimino R de Q, D(Q) = {B,G}
7. Q->SA : Elimino G de Q, D(Q) = {B}
8. NT->Q : Elimino B de NT, D(NT) = {R}
9. NT->WA : Elimino R de NT, D(NT) = { }

Como NT no tiene mas valores en su dominio, podemos concluir que para esta asignación parcial no tenemos solución.
### 3) ¿Cuál es la complejidad en el peor caso cuando se ejecuta AC-3 en un árbol estructurado CSP? (i.e. cuando el grafo de restricciones forma un árbol: cualquiera dos variables están relacionadas por a lo sumo un camino).

En un árbol, las conexiones entre los nodos son claras y directas. Esto significa que el algoritmo AC-3 solo necesita revisar cada conexión una vez, lo que resulta en una eficiencia de O(ED), donde E es el número de conexiones y D el número máximo de posibles valores para cada nodo.

### 4) AC-3 coloca de nuevo en la cola todo arco (Xk, Xi) cuando cualquier valor es removido del dominio de Xi incluso si cada valor de Xk es consistente con los valores restantes de Xi. Supongamos que por cada arco (Xk, Xi) se puede llevar la cuenta del número de valores restantes de  Xi que sean consistentes con cada valor de Xk. Explicar cómo actualizar ese número de manera  eficiente y demostrar que la arco consistencia puede lograrse en un tiempo total O(n^2d^2).

La idea básica es preprocesar las restricciones de modo que, para cada valor de Xi, realicemos un seguimiento de aquellas variables Xk para las cuales ese valor particular de Xi satisface un arco de Xk a Xi. Esta estructura de datos se puede calcular en un tiempo proporcional al tamaño de la representación del problema. Luego, cuando se elimina un valor de Xi, reducimos en 1 el recuento de valores permitidos para cada arco (Xk, Xi) registrado bajo ese valor.

### 5) Demostrar la correctitud del algoritmo CSP para árboles estructurados (sección 6.5, AIMA 3ra edición). Para ello, demostrar:

a) Para un CSP cuyo grafo de restricciones es un árbol, la 2-consistencia (consistencia de arco) implica n−consistencia, siendo n el número total de variables.

b) Argumentar por qué lo demostrado en 5a es suficiente.

**Demostracion**

Supongamos que tenemos un CSP cuyo grafo de restricciones es un árbol y hemos logrado la 2-consistencia. Esto significa que para cada par de variables (Xi, Xj) en el CSP, cualquier valor en el dominio de Xi es consistente con al menos un valor en el dominio de Xj, y viceversa.

Para demostrar la n-consistencia, consideremos cualquier variable Xi en el CSP. Dado que el grafo de restricciones es un árbol, Xi está relacionada con el resto de las variables a través de un único camino en el árbol. Denotemos las variables en este camino como X1, X2, ..., Xn, donde X1 = Xi.

Dado que hemos logrado la 2-consistencia, sabemos que para cualquier variable Xk en el camino (donde k > 1), hay al menos un valor en el dominio de Xk que es consistente con algún valor en el dominio de Xk-1. Esto es cierto para todas las variables en el camino.

Por lo tanto, hemos demostrado que para cualquier variable Xi en el CSP, cualquier valor en su dominio es consistente con al menos un valor en el dominio de cada otra variable en el CSP, siguiendo el único camino en el árbol de restricciones.

Este resultado es suficiente porque, en un CSP, el objetivo es encontrar una asignación que cumpla con todas las restricciones. Si hemos logrado que todas las variables sean consistentes entre sí, hemos eliminado cualquier conflicto y hemos asegurado que existe una solución que satisface todas las restricciones. Esto es fundamental para la correctitud del algoritmo CSP en árboles estructurados, ya que garantiza que si una solución existe, el algoritmo la encontrará.

# Informe sobre el Desempeño de Algoritmos

Para la demostración de los ejercicios, se optó por realizar gráficos de caja y bigote que muestran los tiempos de ejecución de ambos algoritmos en función de diferentes tamaños, permitiendo así una comparación clara de su desempeño. Además, se analizará la evolución de cada algoritmo a través de los distintos tamaños, considerando la cantidad de estados evaluados.

## Gráficos de Caja y Bigote

Para facilitar la comprensión, se presentarán dos gráficos que representan la eficiencia de los algoritmos para resolver los problemas de las 10 y 12 reinas.

![Imagen 1](images/grafico_tiempos_n_10.png)

![Imagen 2](images/grafico_tiempos_n_12.png)

A su vez, se realizará un análisis más profundo mediante la evaluación de un gráfico que muestra la cantidad de evaluaciones por algoritmo y tamaño.

![Imagen 3](images/grafico_evaluaciones.png)

Los gráficos muestran que el desempeño de los algoritmos AC-3 y backtracking es sensible a las características del problema. Aunque en algunos casos el algoritmo AC-3 supera al algoritmo de backtracking, en general se observa una tendencia clara hacia una baja de su rendimiento a medida que aumenta el tamaño de la instancia, llegando a veces a triplicar el número de estados explorados.
