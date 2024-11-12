# Ejercicio 1

## a) La muestra es extremadamente grande (n) y el número de predictores (p) es pequeño.

En este caso, un método flexible tendrá un mejor rendimiento que uno inflexible, ya que el gran tamaño de la muestra le permite aprender patrones complejos y sutiles, y ajustarse a relaciones no lineales. En contraste, un método inflexible puede sufrir de sobreajuste con una muestra tan grande, lo cual podría afectar negativamente su desempeño.

## b) El número de predictores (p) es muy grande y el número de observaciones (n) es pequeño.

Aquí se espera que un método flexible tenga un rendimiento menor, ya que con pocas observaciones en comparación con los predictores, no puede explotar su capacidad de aprendizaje sin riesgo de sobreajuste. En esta situación, un método inflexible puede ser más adecuado, ya que es menos propenso al sobreajuste y suele manejar mejor la alta dimensionalidad de los datos.

## c) La relación entre los predictores y la respuesta es altamente no lineal.

Se espera que un método flexible funcione mejor, pues los métodos inflexibles suelen asumir relaciones lineales y podrían pasar por alto patrones importantes, limitando su capacidad de ajuste a la complejidad de los datos. Los métodos flexibles, en cambio, pueden adaptarse a relaciones no lineales.

## d) La varianza de los términos de error es extremadamente alta.

En este caso, los métodos flexibles pueden sufrir de sobreajuste al intentar capturar la alta variabilidad en los datos. Por otro lado, los métodos inflexibles, al ser más simples y menos sensibles a la complejidad de los datos, pueden lograr un mejor desempeño en condiciones de alta varianza de error.

# Ejercicio 2

## a)

Es un caso de regresión, ya que se busca estimar la correlación entre varios factores y una variable continua (salario), lo cual corresponde a un problema de inferencia.  
`p` = 500, `n` = 4.

## b)

Este es un problema de predicción que se aborda mediante un método de clasificación, ya que el objetivo es prever si un producto será exitoso o no.  
`p` = 20, `n` = 14.

## c)

Es un caso de predicción que emplea un método de regresión para estimar un valor continuo.  
`p` = 52, `n` = 4.

# Ejercicio 5

Al usar métodos de regresión o clasificación, un método flexible puede ser útil para detectar patrones complejos o relaciones no lineales que los métodos inflexibles podrían no capturar, lo que en general mejora el ajuste a los datos de entrenamiento y la precisión en la predicción.  
Sin embargo, la principal desventaja de los métodos flexibles es que son susceptibles al sobreajuste, lo cual puede afectar su desempeño en datos reales.  
Por otro lado, un enfoque inflexible es más adecuado cuando se necesita interpretar el modelo para comprender los resultados, ya que estos métodos tienden a ser más fáciles de entender y menos propensos al sobreajuste, promoviendo una mejor generalización. La limitación de los métodos inflexibles es su falta de adaptabilidad ante datos complejos y relaciones intrincadas.

# Ejercicio 6

El enfoque paramétrico implica hacer suposiciones específicas sobre la forma de la relación entre las variables y emplea un número fijo de parámetros que caracterizan dicha relación. Modelos como la regresión lineal son más simples y fáciles de interpretar, pero su eficacia depende de que las suposiciones sean correctas, lo cual puede limitar su capacidad para capturar patrones complejos.  
El enfoque no paramétrico, en cambio, no impone suposiciones sobre la forma de la relación, permitiendo que la complejidad del modelo se adapte a los datos. Este tipo de modelos es más flexible y puede manejar relaciones no lineales y estructuras de datos complejas. Aunque pueden ser más robustos en algunos casos, la falta de suposiciones explícitas puede dificultar su interpretación y requiere conjuntos de datos más grandes para lograr estimaciones precisas.

# Ejercicio 7

## a) Cálculo de la distancia euclidiana

1.  \(\sqrt{0^2 + 3^2 + 0^2} = 3\)
2.  \(\sqrt{2^2 + 0^2 + 0^2} = 2\)
3.  \(\sqrt{0^2 + 1^2 + 3^2} = \sqrt{10}\)
4.  \(\sqrt{0^2 + 1^2 + 2^2} = \sqrt{10}\)
5.  \(\sqrt{(-1)^2 + 0^2 + 1^2} = \sqrt{2}\)
6.  \(\sqrt{1^2 + 1^2 + 1^2} = \sqrt{3}\)

## b)

El vecino más cercano es la observación 5, con una distancia euclidiana de \(\sqrt{2}\) y un valor de la variable Y = Green. Por lo tanto, la predicción es Y = Green.

## c)

Los tres vecinos más cercanos son 5, 6 y 2. Dos de ellos tienen Y = Red y uno tiene Y = Green, por lo tanto, dado que hay más probabilidad de pertenecer a la clase Red, el valor predicho es Y = Red.

## d)

Si la frontera de decisión de Bayes es altamente no lineal, el mejor valor para \(K\) será pequeño, ya que esto permite que el modelo sea más flexible y pueda captar características complejas.
