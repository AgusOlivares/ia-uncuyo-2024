## Ejercicio 2

#### ¿Cual es la distribucion de la clase inclinacion_peligrosa?

La distribución de las clases es la siguiente:
![DistribucionClasesInclinacionPeligrosa](/tp7-ml/images/DistribucionInclinacionPeligrosa.png)
Se observa que la clase nos indica que mayoritariamente los árboles no tienen una inclinación peligrosa.

### ¿Se puede considerar alguna sección mas peligrosa que otra?

El siguiente gráfico nos muestra que, si hay secciones que posee una mayor proporcion de árboles con inclinacion peligrosa. Tanto la seccion 2 y 3 son las que lidera en esta restrospectiva:
![DistribucionClasesInclinacionPeligrosa](/tp7-ml/images/DistribucionInclinacionPeligrosaSeccion.png)

### ¿ Se puede considerar alguna especie más peligrosa que otra?

Si, en base a los que podemos observar en el siguiente gráfico podemos ver que hay ciertas especie que son mucho más peligrosas que otras. Sin embargo, es notable como los algarrobos lideran con casi un 50%:
![DistribucionClasesInclinacionEspecie](/tp7-ml/images/DistribucionInclinacionPeligrosaEspecie.png)

## Ejercicio 3

### 3. A partir del archivo arbolado-mendoza-dataset-train.csv,

#### b. Histograma de frecuencia para la variable circ_tronco_cm.

![HistrogramaCircunferenciaTronco](/tp7-ml/images/HistogramasCircTronco.png)

#### c. Histograma de frecuencia para la variable circ_tronco_cm pero separando por la clase de la variable inclinación_peligrosa.

![HistrogramaCircunferenciaTroncoInclinacionPeligrosa](/tp7-ml/images/HistogramaCircTroncoSeparadoInclinacion.png)

### d. Crear una nueva variable categórica de nombre circ_tronco_cm_cat a partir circ_tronco_cm, en donde puedan asignarse solo 4 posibles valores [ muy alto, alto, medio, bajo ].

Se tomaron los cortes de la siguiente manera: (0, 60, 180, 250, Inf).

Se encuentra en [TP7-ML/data](/tp7-ml/data/arbolado-mendoza-dataset-circ_tronco_cm-train.csv)
