## 2.10 Considera una versión modificada del entorno de la aspiradora en el Ejercicio 2.8, en la cual al agente se le penaliza con un punto por cada movimiento.

### A. ¿Puede un agente reflexivo simple ser perfectamente racional en este entorno?

No es posible que sea racional ya que no maximizaria su medida de desempeño. El agente no puede percibir el estado de su alrededor, solamente el del casillero en el que se encuentra, por lo que seguiria moviendose de forma innecesaria aplicandole en consecuencia una penalizacion 

### B. ¿Qué pasa con un agente reflexivo con estado?

Dado el caso en que el agente guarde estados, por ejemplo las casillas en las que ha estado, este no se podria considerar perfectamente racional ya que no puede conocer cuales debe limpiar hasta explorarlas, pero tendria un desempeño mas alto

### C. ¿Cómo cambian tus respuestas a las partes a y b si las percepciones del agente le dan el estado limpio/sucio de cada casilla en el entorno?

En este caso considero que el agente si seria racional, debido a que podria evitar movimientos y penalizaciones innecesarias

## 2.11 Considera una versión modificada del entorno de la aspiradora en el Ejercicio 2.8, en la cual la geografía del entorno—su extensión, límites y obstáculos—es desconocida, al igual que la configuración inicial de suciedad. (El agente puede moverse hacia arriba y hacia abajo, así como a la izquierda y a la derecha.)

### A. ¿Puede un agente reflexivo simple ser perfectamente racional en este entorno? Explica.

No, no podria serlo, los agentes reflexivos simples solo conocen su estado actual y toman decisiones basados en este. Al no conocer su entorno no podria optimizar sus movimientos ni minimizar penalizaciones 

### B. ¿Puede un agente reflexivo simple con una función de agente aleatorizada superar a un agente reflexivo simple? Diseña tal agente y mide su rendimiento en varios entornos.

En terminos generales y debido a evidencia empirica podemos concluir que eso no seria posible, si bien en algunos entornos el agente aleatorio parece superar al racional, la realidad es que esto no es constante y en entornos de mayor tamaño el rendimiento del agente aleatorio decaera en comparacion.

### C. ¿Puedes diseñar un entorno en el que tu agente aleatorizado tenga un mal rendimiento? Muestra tus resultados.

Basta con hacer un entorno de gran tamaño con un porcentaje de suciedad bajo para que el rendimiento de este decaiga en comparacion al agente reflexivo simple

### D. ¿Puede un agente reflexivo con estado superar a un agente reflexivo simple? Diseña tal agente y mide su rendimiento en varios entornos. ¿Puedes diseñar un agente racional de este tipo?

Si, seria posible superarlo, ya que en el agente reflexivo con estados se podria implementar un algoritmo para optimizar los movimientos evitando el paso por casillas ya exploradas, pero de todas maneras no se podria consederar como racional ya que no conoce su entorno hasta que lo explore