## **Resultados de la Evaluación en `tennis.csv`**

Los resultados obtenidos de la evaluación se resumen en el siguiente diccionario:

```python
{
  'outlook': {
    'overcast': 'yes',
    'rainy': {
      'windy': {np.False*: 'yes', np.True*: 'no'}
    },
    'sunny': {
      'humidity': {'high': 'no', 'normal': 'yes'}
    }
  }
}
```

Expresado como reglas, esto se traduce en lo siguiente:

- **Si `outlook = overcast`**, entonces **play = yes**.
- **Si `outlook = rainy`** y `windy = False`, entonces **play = yes**.
- **Si `outlook = rainy`** y `windy = True`, entonces **play = no**.
- **Si `outlook = sunny`** y `humidity = high`, entonces **play = no**.
- **Si `outlook = sunny`** y `humidity = normal`, entonces **play = yes**.

Este conjunto de reglas muestra cómo el árbol de decisión evalúa los diferentes valores de los atributos para predecir si se jugará al tenis o no.

---

## **Estrategias para Manejar Datos Continuos en Árboles de Decisión**

Cuando los datos contienen **atributos numéricos o continuos** (por ejemplo, edad, peso, temperatura), los árboles de decisión adoptan estrategias especiales para manejar estos valores y realizar particiones adecuadas en los nodos. A continuación se describen las técnicas y estrategias más comunes:

### **1. Divisiones Binarias con Umbral Óptimo**

Para los atributos continuos, el árbol de decisión busca un **umbral de división óptimo** que separe los datos en dos grupos. El objetivo es maximizar alguna métrica de pureza (como la **Ganancia de Información** o el **Índice Gini**) para encontrar el punto de corte más adecuado.

- **Ejemplo:** Si el atributo "peso" tiene valores continuos, el árbol podría considerar si el peso es menor o igual a un valor específico, como 70 kg, y crear dos ramas:
  - Rama izquierda: individuos con peso ≤ 70 kg.
  - Rama derecha: individuos con peso > 70 kg.

Este umbral se determina evaluando diferentes puntos y eligiendo el que maximiza la pureza de las particiones resultantes.

### **2. Estrategias Recursivas de Partición**

Una vez que el árbol selecciona el primer umbral para dividir los datos, cada subconjunto resultante se analiza de nuevo. Este proceso se repite recursivamente en cada rama del árbol, dividiendo cada subconjunto hasta que se cumplan los criterios de detención, tales como:

- Alcanzar una **profundidad máxima** del árbol.
- Todos los elementos dentro de un nodo sean del mismo tipo o clase (es decir, no haya más incertidumbre).

Esto genera un árbol de decisión profundo, donde cada nodo representa una partición de los datos basada en una o más características.

### **3. Utilización de la Ganancia de Información y el Índice Gini**

Los árboles de decisión emplean dos métricas principales para decidir cómo dividir los datos en cada nodo:

- **Ganancia de Información**: Mide la reducción de la **incertidumbre** o **impureza** después de una división. Un valor alto de ganancia de información indica que la división ha hecho que los datos sean más homogéneos, lo que lleva a una predicción más precisa.
- **Índice Gini**: Calcula la "impureza" de un nodo, es decir, la probabilidad de que un elemento se clasifique erróneamente si se selecciona al azar. Un valor bajo de Gini indica que los datos en un nodo son relativamente homogéneos.

El algoritmo utiliza estas métricas para seleccionar el atributo y el punto de división que maximizan la pureza de las ramas resultantes, favoreciendo divisiones que generen nodos más puros.

### **4. Manejo de Overfitting**

Uno de los mayores desafíos al trabajar con atributos continuos es el **overfitting** o sobreajuste. Dado que los árboles pueden generar muchas divisiones finas, especialmente con datos continuos, existe el riesgo de que el árbol se ajuste demasiado a las particularidades de los datos de entrenamiento y no generalice bien a nuevos datos.

Para mitigar el overfitting, se implementan varias técnicas:

- **Poda de árboles** (pruning): Después de que el árbol se construye completamente, se eliminan algunas ramas que contribuyen poco a la mejora de la predicción. Esto reduce la complejidad del modelo.
- **Limitación de la profundidad del árbol**: Establecer un límite en la profundidad máxima del árbol asegura que el modelo no se vuelva demasiado complejo, lo que ayuda a evitar el sobreajuste.
