# Informe TP 7 - B

#### Descripción del proceso de preprocesamiento

El proceso de preprocesamiento de los datos incluyó varias etapas clave. En primer lugar, se abordó la limpieza de datos, especialmente la variable `altura`, que contenía caracteres no numéricos. Esta columna fue transformada a formato numérico, eliminando los caracteres no relevantes mediante una expresión regular.

Posteriormente, se eliminaron las filas con valores faltantes (`NA`) utilizando la función `na.omit()`, asegurando que solo los registros completos fueran incluidos en el conjunto de entrenamiento. Este paso fue crucial para evitar que los valores faltantes afectaran el rendimiento del modelo.

Se identificó un desbalance en las clases de la variable de respuesta `inclinacion_peligrosa`, con muchas más observaciones de la clase `0` (sin inclinación peligrosa) que de la clase `1` (con inclinación peligrosa). Para mitigar este problema, se implementó un procedimiento de undersampling en la clase mayoritaria, reduciendo el número de muestras de la clase `0` a 3500 y combinándolas con todas las muestras de la clase minoritaria. Esto resultó en un conjunto de datos balanceado, lo que ayudó a mejorar el desempeño del modelo.

En cuanto a la selección de variables, se eliminaron varias columnas que no aportaban valor para la predicción, tales como `id`, `nombre_seccion`, `area_seccion`, `seccion` y `circ_tronco_cm`. Esto permitió que el modelo se centrara en las variables más relevantes, como `especie`, `altura`, `diametro_tronco`, `long`, y `lat`. Además, la variable de respuesta `inclinacion_peligrosa` fue convertida a un factor, lo que facilitó su tratamiento como variable categórica en el modelo.

#### Resultados obtenidos sobre el conjunto de validación

El modelo no utilizó un conjunto de validación independiente, ya que se optó por entrenar el modelo con todo el conjunto de datos disponible. A pesar de esto, el proceso de balanceo de clases y la eliminación de valores faltantes contribuyeron a la mejora del rendimiento general del modelo. Aunque no se aplicó una validación cruzada explícita, se puede decir que el modelo fue entrenado de forma exhaustiva con los datos balanceados y procesados.

#### Resultados obtenidos en Kaggle

El modelo fue evaluado en Kaggle, donde obtuvo un puntaje de **0.70653** en la tabla pública. Este valor refleja la precisión del modelo al predecir la variable `inclinacion_peligrosa` en un conjunto de datos diferente al utilizado para el entrenamiento.

#### Descripción detallada del algoritmo propuesto

El modelo utilizado para la clasificación fue **Random Forest**, un algoritmo de ensamble basado en árboles de decisión. Este enfoque es robusto y es conocido por su capacidad para manejar grandes cantidades de datos y reducir el sobreajuste al combinar múltiples árboles de decisión.

El modelo fue entrenado con las variables `especie`, `altura`, `diametro_tronco`, `long` y `lat`, y se utilizó un total de 3900 árboles (`ntree = 3900`). Este número elevado de árboles se eligió para mejorar la precisión y estabilidad del modelo, reduciendo la varianza y aumentando la capacidad de generalización.

Se empleó un valor de `mtry = 4`, que determina cuántas variables se consideran en cada división del árbol. Este parámetro fue ajustado para balancear la exploración de las características del modelo y optimizar su desempeño.

El balanceo de clases se logró a través de un undersampling de la clase mayoritaria, lo que permitió al modelo aprender mejor las características de la clase minoritaria (aquellos con `inclinacion_peligrosa = 1`).

Para garantizar la reproducibilidad de los resultados, se fijó la semilla de aleatoriedad con `set.seed(2024)`. Esto asegura que los experimentos puedan ser replicados con los mismos resultados.
