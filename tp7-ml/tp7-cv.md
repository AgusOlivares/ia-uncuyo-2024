### Ejercicio 7

```r
create_folds <- function(dataFrame, num) {
  indexes <- sample(1: nrow(dataFrame))
  folds <- split(indexes, cut(seq_along(indexes), breaks = num, labels = FALSE))
  names(folds) <- paste0("Fold", 1:num)
  return(folds)
}

cross_validation <- function(dataFrame, num) {
  dataFrame$inclinacion_peligrosa <- as.factor(dataFrame$inclinacion_peligrosa)
  train_formula <- formula(inclinacion_peligrosa ~ altura + diametro_tronco + seccion)

  folds <- create_folds(dataFrame, num)
  predicList <- list()
  matrixList <- list()

  for (i in 1:num) {
    indexes <- folds[[i]]
    trainData <- dataFrame[-indexes, ]
    valData <- dataFrame[indexes, ]

    tree_model <- rpart(train_formula, data = trainData)
    p <- predict(tree_model, valData, type = 'class')
    maAux <- new_confusion_matrix(valData$inclinacion_peligrosa, p)
    matrixList[[i]] <- maAux
    predicList[[paste0("Fold", i)]] <- p
  }
  return(list(predictions = predicList, matrices = matrixList))
}
```

### Resultados

#### 1) Sin Balanceo de Clases

Inicialmente, entrenamos el modelo sin modificar el balance de clases. Esto generó resultados donde el modelo predecía "no" ya que, las clases tenían un notable desbalance entonces al sobre predecir "no" estaba correcto en lo casos. Para resolver el problema se implementaron dos tecnicas para reducir este desbalance con, oversamplin y undersampling.

#### 2) Balanceo con Oversampling

Para mejorar la detección de la clase minoritaria, se utilizó **oversampling** con la librería `ROSE`, generando datos sintéticos para igualar la cantidad de ambas clases. Tras varias pruebas, observamos que el modelo alcanzó su mejor rendimiento con **10 folds**.

| Métrica         | Media  | Desviación Estándar |
| --------------- | ------ | ------------------- |
| **Accuracy**    | 0.6459 | 0.0175              |
| **Precision**   | 0.6091 | 0.0186              |
| **Sensitivity** | 0.8153 | 0.0182              |
| **Specificity** | 0.4769 | 0.0185              |

La implementación de oversampling mejoró considerablemente la **sensibilidad** y **precisión**, lo cual es clave para el objetivo de este problema. Sin embargo, observamos una ligera disminución en **accuracy** y **specificity** debido al incremento de falsos positivos.

#### 3) Balanceo con Undersampling

También realizamos el mismo proceso utilizando **undersampling**, eliminando registros aleatorios de la clase mayoritaria para igualar las clases. Luego de probar distintas cantidades de folds, los mejores resultados se obtuvieron con **20 folds**.

| Métrica         | Media  | Desviación Estándar |
| --------------- | ------ | ------------------- |
| **Accuracy**    | 0.6232 | 0.0544              |
| **Precision**   | 0.5988 | 0.0766              |
| **Sensitivity** | 0.7654 | 0.0585              |
| **Specificity** | 0.4857 | 0.0901              |

Los resultados de undersampling son similares a los de oversampling, aunque presentan una mejora leve en **specificity** y **precision**, a costa de una pequeña reducción en **sensibilidad**.

**Comparación de Métodos (Oversampling vs. Undersampling):**

- **Oversampling**: Este método alcanza la **mejor sensibilidad** (0.8153), lo que lo hace ideal para detectar árboles peligrosos, aunque presenta un leve aumento en falsos positivos.
- **Undersampling**: Mejora la precisión y especificidad, pero sacrifica un poco de sensibilidad en comparación con el oversampling.

En conclusion, para la identificación de árboles peligrosos, es más optimo utilizar el metodo de **oversampling** al ofrece una sensibilidad superior, lo que responde al objetivo de este problema.
