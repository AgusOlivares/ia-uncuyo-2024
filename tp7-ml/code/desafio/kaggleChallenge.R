# Librerías necesarias
suppressMessages(library(readr))
suppressMessages(library(randomForest))
suppressMessages(library(dplyr))

# Set de semilla para reproducibilidad
set.seed(2024)

# Cargar datos de entrenamiento
data_train <- readr::read_csv("tp7-ml/code/desafio/arbolado-mza-dataset.csv",
                              col_types = cols(
                                especie = col_character(),
                                altura = col_character(),
                                circ_tronco_cm = col_double(),
                                diametro_tronco = col_character(),
                                long = col_double(),
                                lat = col_double(),
                                nombre_seccion = col_character(),
                                seccion = col_integer(),
                                area_seccion = col_double(),
                                inclinacion_peligrosa = col_integer()
                              ))

# Cargar datos de prueba
data_test <- readr::read_csv("tp7-ml/code/desafio/arbolado-mza-dataset-test.csv",
                              col_types = cols(
                                especie = col_character(),
                                id = col_integer(),
                                altura = col_character(),
                                circ_tronco_cm = col_double(),
                                diametro_tronco = col_character(),
                                long = col_double(),
                                lat = col_double(),
                                nombre_seccion = col_character(),
                                seccion = col_integer(),
                                area_seccion = col_double()
                              ))

# Conversión y limpieza de datos
data_train$altura <- as.numeric(gsub("[^0-9.]", "", data_train$altura))
data_test$altura <- as.numeric(gsub("[^0-9.]", "", data_test$altura))
data_train <- na.omit(data_train)

# Selección de datos balanceados
muestra_inclinacion_peligrosa <- data_train[data_train$inclinacion_peligrosa == 1, ]
muestra_inclinacion_no_peligrosa <- data_train %>% filter(inclinacion_peligrosa == 0) %>% sample_n(3500)
data_filtrado <- rbind(muestra_inclinacion_peligrosa, muestra_inclinacion_no_peligrosa)

# Preparar predictores y variable de respuesta
predictores <- data_filtrado[, !(colnames(data_filtrado) %in% c("inclinacion_peligrosa", "id", "nombre_seccion", "area_seccion", "seccion", "ultima_modificacion", "circ_tronco_cm"))]
respuesta <- factor(data_filtrado$inclinacion_peligrosa)

# Entrenar modelo Random Forest
modelo <- randomForest(x = predictores, y = respuesta, ntree = 3900, mtry = 4)

# Realizar predicciones en el conjunto de prueba
predictions <- predict(modelo, newdata = data_test)

# Convertir predicciones a 1 y 0
predicciones_transformadas <- as.numeric(predictions) - 1  # Convierte 'No' a 0 y 'Sí' a 1

# Crear un DataFrame para enviar a Kaggle
submission <- data.frame(id = data_test$id, inclinacion_peligrosa = predicciones_transformadas)

# Guardar el resultado en un archivo CSV
write.csv(submission, file = "tp7-ml/code/desafio/arbolado-mza-dataset-envio.csv", row.names = FALSE)

# Imprimir el modelo para ver su desempeño
print(modelo)
