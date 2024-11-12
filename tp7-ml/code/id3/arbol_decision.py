import pandas as pd
from collections import Counter
import math
import pprint #pretty-print, imprime estructuras de datos complejas en un formato más legible y organizado


def entropia(ejemplos):
    total = len(ejemplos)
    conteo = Counter(ejemplos)
    entropia = -sum((count / total) * math.log2(count / total) for count in conteo.values())
    return entropia

def elegir_atributo(atributos, ejemplos, objetivo):
    entropia_inicial = entropia(ejemplos[objetivo])
    mejor_atributo = None
    mejor_ganancia = -1

    for atributo in atributos:
        valores = ejemplos[atributo].unique()
        entropia_condicional = sum(
            (len(subconjunto) / len(ejemplos)) * entropia(subconjunto[objetivo])
            for valor in valores
            if (subconjunto := ejemplos[ejemplos[atributo] == valor]).size > 0
        )

        ganancia = entropia_inicial - entropia_condicional
        if ganancia > mejor_ganancia:
            mejor_ganancia = ganancia
            mejor_atributo = atributo

    return mejor_atributo


def aprendizaje_arbol_decision(ejemplos, atributos, por_defecto):
    if ejemplos.empty:
        return por_defecto
    elif len(ejemplos[objetivo].unique()) == 1:
        return ejemplos[objetivo].iloc[0]
    elif not atributos:
        return valor_mayoria(ejemplos)

    mejor = elegir_atributo(atributos, ejemplos, objetivo)
    arbol = {mejor: {}}
    valor_may = valor_mayoria(ejemplos)

    for valor in ejemplos[mejor].unique():
        ejemplos_v = ejemplos[ejemplos[mejor] == valor]
        sub_arbol = aprendizaje_arbol_decision(
            ejemplos_v, [a for a in atributos if a != mejor], valor_may
        )
        arbol[mejor][valor] = sub_arbol

    return arbol


def valor_mayoria(ejemplos):
    return ejemplos[objetivo].mode()[0] #MODA: obtiene el valor más frecuente


df = pd.read_csv("tennis.csv")
objetivo = "play"  # se quiere predecir si se jugará o no.
atributos = list(df.columns) #convierte las columnas del data set en lista de nombres de atributos.
atributos.remove(objetivo) #eliminamos el nombre de la variable objetivo "play" de la lista ya q es la q queremos predecir


arbol = aprendizaje_arbol_decision(df, atributos, valor_mayoria(df))


pprint.pprint(arbol, width=40)
print(atributos)

"""
resultado: 
Si outlook = overcast, entonces play = yes.
Si outlook = rainy y windy = False, entonces play = yes.
Si outlook = rainy y windy = True, entonces play = no.
Si outlook = sunny y humidity = high, entonces play = no.
Si outlook = sunny y humidity = normal, entonces play = yes.
"""