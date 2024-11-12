# Cargar el paquete necesario
library(dplyr)
library(ggplot2)
library(readr)
library(rpart)
library(caret)

######## Creacion de archivos de entramiento ########

# Leer el archivo CSV desde la carpeta de datos usando la ruta relativa correcta
dataset <- read.csv("tp7-ml/data/arbolado-mza-dataset.csv", stringsAsFactors = FALSE)

# Definir el porcentaje de muestra para la validación
set.seed(123)  # Semilla para reproducibilidad
sample_size <- floor(0.2 * nrow(dataset))  # 20% de los datos

# Seleccionar aleatoriamente el 20% de los datos para el conjunto de validación
validation_indices <- sample(seq_len(nrow(dataset)), size = sample_size)
dataset_validation <- dataset[validation_indices, ]
dataset_train <- dataset[-validation_indices, ]

# Guardar los datasets en archivos CSV en la misma carpeta de datos
write.csv(dataset_validation, "tp7-ml/data/arbolado-mendoza-dataset-validation.csv", row.names = FALSE)
write.csv(dataset_train, "tp7-ml/data/arbolado-mendoza-dataset-train.csv", row.names = FALSE)

######## Creacion de visualizacion de inclinacion_peligrosa ########
# Cargar el dataset de entrenamiento
dataset_train <- read.csv("tp7-ml/data/arbolado-mendoza-dataset-train.csv", stringsAsFactors = FALSE)

# Convertir la columna inclinacion_peligrosa a factor para facilitar el análisis
dataset_train$inclinacion_peligrosa <- as.factor(dataset_train$inclinacion_peligrosa)

# Pregunta a: Distribución de la clase inclinacion_peligrosa
ggplot(dataset_train, aes(x = inclinacion_peligrosa)) +
  geom_bar(fill = "skyblue", color = "black") +
  labs(title = "Distribución de Inclinación Peligrosa", x = "Inclinación Peligrosa", y = "Frecuencia") +
  theme_minimal()

# Pregunta b: Secciones con mayor riesgo de inclinación peligrosa
ggplot(dataset_train, aes(x = seccion, fill = inclinacion_peligrosa)) +
  geom_bar(position = "fill") +
  labs(title = "Distribución de Inclinación Peligrosa por Sección", x = "Sección", y = "Proporción", fill = "Inclinación Peligrosa") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

# Pregunta c: Especies con mayor riesgo de inclinación peligrosa
ggplot(dataset_train, aes(x = especie, fill = inclinacion_peligrosa)) +
  geom_bar(position = "fill") +
  labs(title = "Distribución de Inclinación Peligrosa por Especie", x = "Especie", y = "Proporción", fill = "Inclinación Peligrosa") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

######## Creacion de visualizacion de circ_tronco_cm ########
# Pregunta b: Generar histogramas de circ_tronco_cm con diferentes números de bins
par(mfrow = c(2, 2))  # Crear una cuadrícula 2x2 para mostrar varios histogramas

hist(dataset_train$circ_tronco_cm, main = "Histograma (5 bins)", xlab = "circ_tronco_cm", breaks = 5)
hist(dataset_train$circ_tronco_cm, main = "Histograma (10 bins)", xlab = "circ_tronco_cm", breaks = 10)
hist(dataset_train$circ_tronco_cm, main = "Histograma (20 bins)", xlab = "circ_tronco_cm", breaks = 20)
hist(dataset_train$circ_tronco_cm, main = "Histograma (30 bins)", xlab = "circ_tronco_cm", breaks = 30)

# Restaurar la configuración de gráficos a una sola ventana
par(mfrow = c(1, 1))

# Pregunta c: Histograma de circ_tronco_cm separado por inclinacion_peligrosa
ggplot(dataset_train, aes(x = circ_tronco_cm, fill = inclinacion_peligrosa)) +
  geom_histogram(binwidth = 10, position = "identity", alpha = 0.6) +
  labs(title = "Histograma de circ_tronco_cm separado por inclinacion_peligrosa", 
       x = "circ_tronco_cm",
       y = "Frecuencia") +
  scale_fill_manual(values = c("1" = "red", "0" = "green"), name = "Inclinación Peligrosa") +
  theme_minimal()

# Pregunta d: Crear una nueva variable categórica circ_tronco_cm_cat
dataset_train <- dataset_train %>% 
  mutate(circ_tronco_cm_cat = cut(circ_tronco_cm, 
                                  breaks = c(0, 60, 180, 250, Inf),
                                  labels = c("bajo", "medio", "alto", "muy alto"),
                                  include.lowest = TRUE))

# Guardar el nuevo dataframe con la columna circ_tronco_cm_cat en un archivo CSV
write_csv(dataset_train, "tp7-ml/data/arbolado-mendoza-dataset-circ_tronco_cm-train.csv")


######## Clasificador Aleatorio ########
generar_prediction_prob <- function(data) {
  data$prediction_prob <- runif(nrow(data), min = 0, max = 1)
  return(data)
}

random_classifier <- function(data) {
  data <- generar_prediction_prob(data)  # Llamada a la función para añadir `prediction_prob`
  data$prediction_class <- ifelse(data$prediction_prob > 0.5, 1, 0)
  return(data)
}

# Cargar el archivo de validación
dataset_validation <- read.csv("tp7-ml/data/arbolado-mendoza-dataset-validation.csv", stringsAsFactors = FALSE)

# Aplicar el clasificador aleatorio
dataset_validation <- random_classifier(dataset_validation)


# Convertir `inclinacion_peligrosa` a factor si no lo está
dataset_validation$inclinacion_peligrosa <- as.factor(dataset_validation$inclinacion_peligrosa)

# Calcular TP, TN, FP, FN
tp <- nrow(filter(dataset_validation, inclinacion_peligrosa == 1 & prediction_class == 1))
tn <- nrow(filter(dataset_validation, inclinacion_peligrosa == 0 & prediction_class == 0))
fp <- nrow(filter(dataset_validation, inclinacion_peligrosa == 0 & prediction_class == 1))
fn <- nrow(filter(dataset_validation, inclinacion_peligrosa == 1 & prediction_class == 0))

# Crear la tabla de la matriz de confusión
matriz_confusion <- data.frame(
  "Predicción Positiva" = c(tp, fp),
  "Predicción Negativa" = c(fn, tn),
  row.names = c("Real Positivo", "Real Negativo")
)

print(matriz_confusion)


######## Clasificador Mayoritario ########
biggerclass_classifier <- function(data) {
  # Asegurarse de que `inclinacion_peligrosa` es numérico
  data$inclinacion_peligrosa <- as.numeric(as.character(data$inclinacion_peligrosa))
  
  # Calcular la clase mayoritaria (asumimos que 1 es mayoritaria si la media es mayor que 0.5)
  clase_mayoritaria <- ifelse(mean(data$inclinacion_peligrosa, na.rm = TRUE) > 0.5, 1, 0)
  
  # Asignar la clase mayoritaria a `prediction_class`
  data$prediction_class <- clase_mayoritaria
  return(data)
}


# Aplicar el clasificador por clase mayoritaria
dataset_validation_biggerclass <- biggerclass_classifier(dataset_validation)

# Calcular TP, TN, FP, FN para el clasificador por clase mayoritaria
tp_biggerclass <- nrow(filter(dataset_validation_biggerclass, inclinacion_peligrosa == 1 & prediction_class == 1))
tn_biggerclass <- nrow(filter(dataset_validation_biggerclass, inclinacion_peligrosa == 0 & prediction_class == 0))
fp_biggerclass <- nrow(filter(dataset_validation_biggerclass, inclinacion_peligrosa == 0 & prediction_class == 1))
fn_biggerclass <- nrow(filter(dataset_validation_biggerclass, inclinacion_peligrosa == 1 & prediction_class == 0))

# Crear la matriz de confusión para el clasificador por clase mayoritaria
matriz_confusion_biggerclass <- data.frame(
  "Predicción Positiva" = c(tp_biggerclass, fp_biggerclass),
  "Predicción Negativa" = c(fn_biggerclass, tn_biggerclass),
  row.names = c("Real Positivo", "Real Negativo")
)

print(matriz_confusion_biggerclass)



######## Calcular métricas de rendimiento ########
# Función para calcular Accuracy
calcular_accuracy <- function(TP, TN, FP, FN) {
  (TP + TN) / (TP + TN + FP + FN)
}
# Función para calcular Precision
calcular_precision <- function(TP, FP) {
  if ((TP + FP) == 0) {
    return(NA) # O retorna 0 si prefieres manejar como 0 cuando no hay positivos predichos
  }
  TP / (TP + FP)
}
# Función para calcular Sensitivity (Recall)
calcular_sensitivity <- function(TP, FN) {
  if ((TP + FN) == 0) {
    return(NA)
  }
  TP / (TP + FN)
}

# Función para calcular Specificity
calcular_specificity <- function(TN, FP) {
  if ((TN + FP) == 0) {
    return(NA)
  }
  TN / (TN + FP)
}

# Metricas clasificador Aleatorio
accuracy_random <- calcular_accuracy(tp, tn, fp, fn)
precision_random <- calcular_precision(tp, fp)
sensitivity_random <- calcular_sensitivity(tp, fn)
specificity_random <- calcular_specificity(tn, fp)

cat("Métricas para el clasificador aleatorio:\n")
cat("Accuracy:", accuracy_random, "\n")
cat("Precision:", precision_random, "\n")
cat("Sensitivity:", sensitivity_random, "\n")
cat("Specificity:", specificity_random, "\n")

# Metricas clasificador clase mayoritaria
accuracy_biggerclass <- calcular_accuracy(tp_biggerclass, tn_biggerclass, fp_biggerclass, fn_biggerclass)
precision_biggerclass <- calcular_precision(tp_biggerclass, fp_biggerclass)
sensitivity_biggerclass <- calcular_sensitivity(tp_biggerclass, fn_biggerclass)
specificity_biggerclass <- calcular_specificity(tn_biggerclass, fp_biggerclass)

cat("\nMétricas para el clasificador por clase mayoritaria:\n")
cat("Accuracy:", accuracy_biggerclass, "\n")
cat("Precision:", precision_biggerclass, "\n")
cat("Sensitivity:", sensitivity_biggerclass, "\n")
cat("Specificity:", specificity_biggerclass, "\n")


### Creacion de los folds ###
library(dplyr)
library(ROSE)
library(rpart)

# Función para crear la matriz de confusión
new_confusion_matrix <- function(inclinacion, predict) {
  truePos <- sum((inclinacion == 1) & (predict == 1))
  trueNeg <- sum((inclinacion == 0) & (predict == 0))
  falsePos <- sum((inclinacion == 0) & (predict == 1))
  falseNeg <- sum((inclinacion == 1) & (predict == 0))
  return(data.frame(True_Positive = truePos, True_Negative = trueNeg, False_Positive = falsePos, False_Negative = falseNeg))
} 

# Funciones para calcular las métricas
newAccuracy <- function(dataFrame) {
  (dataFrame$True_Positive + dataFrame$True_Negative) / (dataFrame$True_Negative + dataFrame$False_Positive + dataFrame$False_Negative + dataFrame$True_Positive)
}

newPrecision <- function(dataFrame) {
  dataFrame$True_Positive / (dataFrame$True_Positive + dataFrame$False_Positive)
}

newSensitivity <- function(dataFrame) {
  dataFrame$True_Positive / (dataFrame$True_Positive + dataFrame$False_Negative)
}

newSpecificity <- function(dataFrame) {
  dataFrame$True_Negative / (dataFrame$True_Negative + dataFrame$False_Positive)
}

newCalculateMetrics <- function(data) {
  data.frame(
    Accuracy = newAccuracy(data),
    Precision = newPrecision(data),
    Sensitivity = newSensitivity(data),
    Specificity = newSpecificity(data)
  )
}

# Función para crear folds
create_folds <- function(dataFrame, num) {
  indexes <- sample(1: nrow(dataFrame))
  split(indexes, cut(seq_along(indexes), breaks = num, labels = FALSE))
}

# Función para realizar validación cruzada
cross_validation <- function(dataFrame, num_folds) {
  dataFrame$inclinacion_peligrosa <- as.factor(dataFrame$inclinacion_peligrosa)
  train_formula <- formula(inclinacion_peligrosa ~ altura + diametro_tronco + seccion)

  folds <- create_folds(dataFrame, num_folds)
  predicList <- list()
  matrixList <- list()

  for (i in seq_along(folds)) {
    trainData <- dataFrame[-folds[[i]], ]
    valData <- dataFrame[folds[[i]], ]
    
    tree_model <- rpart(train_formula, data = trainData)
    p <- predict(tree_model, valData, type = 'class') 
    maAux <- new_confusion_matrix(valData$inclinacion_peligrosa, p)
    
    matrixList[[i]] <- maAux
    predicList[[paste0("Fold", i)]] <- p
  }
  return(list(predictions = predicList, matrices = matrixList))
}

# Cargar y preparar datos
dataFrame <- read.csv("tp7-ml/data/arbolado-mendoza-dataset-validation.csv", header = TRUE, sep = ",")
dataFrame <- dataFrame %>%
  group_by(especie) %>%
  filter(n() > 1) %>%
  ungroup()

# Configurar sobremuestreo
maj <- dataFrame[dataFrame$inclinacion_peligrosa == 0, ]
min <- dataFrame[dataFrame$inclinacion_peligrosa == 1, ]
dataOverSample <- ovun.sample(inclinacion_peligrosa ~ ., data = dataFrame, method = "over", N = nrow(maj) * 2)$data

# Validación cruzada con sobremuestreo
res_over <- cross_validation(dataOverSample, 10)
met_over <- lapply(res_over$matrices, newCalculateMetrics)
final_over <- do.call(rbind, met_over)
write.csv(final_over, file = "tp7-ml/data/metricsDataOverSample.csv")

# Métricas promedio y desviación estándar para sobremuestreo
metrics_over <- data.frame(
  Metrica = c("Accuracy", "Precision", "Sensitivity", "Specificity"),
  Media = sapply(final_over, mean, na.rm = TRUE),
  Desviacion = sapply(final_over, sd, na.rm = TRUE)
)
write.csv(metrics_over, file = "tp7-ml/data/metricsOverSample.csv")

# Configurar submuestreo
n <- nrow(min) * 2
dataUnderSample <- ovun.sample(inclinacion_peligrosa ~ ., data = dataFrame, method = "under", N = n)$data

# Validación cruzada con submuestreo
res_under <- cross_validation(dataUnderSample, 10)
met_under <- lapply(res_under$matrices, newCalculateMetrics)
final_under <- do.call(rbind, met_under)
write.csv(final_under, file = "tp7-ml/data/metricsDataUnderSample.csv")

# Métricas promedio y desviación estándar para submuestreo
metrics_under <- data.frame(
  Metrica = c("Accuracy", "Precision", "Sensitivity", "Specificity"),
  Media = sapply(final_under, mean, na.rm = TRUE),
  Desviacion = sapply(final_under, sd, na.rm = TRUE)
)
write.csv(metrics_under, file = "tp7-ml/data/metricsUnderSample.csv")
