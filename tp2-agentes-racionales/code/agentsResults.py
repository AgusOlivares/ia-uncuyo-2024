import agent as a
import reflexiveAgent as rag
import randomAgent as rage
import enviroment as e
import pandas as pd
import seaborn as sns
import random
import matplotlib.pyplot as plt

def resultados_agentes(sizes,dirty_rates):
    # Listas para almacenar los resultados de los agentes
    results_reflexivo = []

    results_random = []

    # Bucle para cada combinación de tamaño y porcentaje de suciedad
    for size in sizes:
        for rate in dirty_rates:
            for _ in range(10):  
                # Generar y guardar una semilla aleatoria
                seed = random.randint(0, 1000000)
                
                # Usar la semilla
                random.seed(seed)
                entorno_reflexivo = e.Environment(size, size, rate)
                agenteReflexivo = rag.reflexiveAgent(entorno_reflexivo)
                result_reflexivo = agenteReflexivo.think()  
                results_reflexivo.append({
                    'Size': f'{size}x{size}',
                    'Dirty Rate': rate,
                    'Performance': result_reflexivo[0],
                    'Necessary Moves': result_reflexivo[1]
                })
                
                # Usar la misma semilla para el agente random
                random.seed(seed)  # Reseteo la semilla para asegurar el mismo entorno
                entorno_random = e.Environment(size, size, rate)
                agenteRandom = rage.randomAgent(entorno_random)
                result_random = agenteRandom.think()  # Tupla con (performance , necessaryMoves)
                results_random.append({
                    'Size': f'{size}x{size}',
                    'Dirty Rate': rate,
                    'Performance': result_random[0],
                    'Necessary Moves': result_random[1]
                })
    return results_reflexivo,results_random


def performance_promedio_suciedad(df_1 , df_2 , dirty_rates , size ):
    # Promedio de los 10 intentos
    promedios_1 = []
    promedios_2 = []

    # Promedio para todos los porcentajes de suciedad
    for rate in dirty_rates:
        df_1_filtered = df_1[(df_1['Size'] == size) & (df_1['Dirty Rate'] == rate)]
        df_2_filtered = df_2[(df_2['Size'] == size) & (df_2['Dirty Rate'] == rate)]

        promedio_1 = promedio(df_1_filtered,'Performance')
        promedio_2 = promedio(df_2_filtered,'Performance')

        promedios_1.append(promedio_1)
        promedios_2.append(promedio_2)
    
    return promedios_1,promedios_2


def performance_promedio_entorno(df_1 , df_2 , rate , sizes ):
    # Guardan el promedio de los 10 intentos
    promedios_1 = []
    promedios_2 = []

    # Guardamos el promedio para todos los entornos
    for size in sizes:
        df_1_filtered = df_1[(df_1['Size'] == f'{size}x{size}') & (df_1['Dirty Rate'] == rate)]
        df_2_filtered = df_2[(df_2['Size'] == f'{size}x{size}') & (df_2['Dirty Rate'] == rate)]

        promedio_1 = promedio(df_1_filtered,'Performance')
        promedio_2 = promedio(df_2_filtered,'Performance')

        promedios_1.append(promedio_1)
        promedios_2.append(promedio_2)
    
    return promedios_1,promedios_2

def necessary_moves_promedio_entorno(df_1 , df_2 , rate , sizes):

    # Promedio de los movimientos necesarios para llegar a su maxima performance
    promedios_1 = []
    promedios_2 = []

    # Promedio para todos los entornos
    for size in sizes:
        df_1_filtered = df_1[(df_1['Size'] == f'{size}x{size}') & (df_1['Dirty Rate'] == rate)]
        df_2_filtered = df_2[(df_2['Size'] == f'{size}x{size}') & (df_2['Dirty Rate'] == rate)]

        promedio_1 = promedio(df_1_filtered,'Necessary Moves')
        promedio_2 = promedio(df_2_filtered,'Necessary Moves')

        promedios_1.append(promedio_1)
        promedios_2.append(promedio_2)
    
    return promedios_1,promedios_2


def promedio(df_filtered,columna):
    return sum(df_filtered[columna])/len(df_filtered[columna])


def graficos_performance_dirtyRate(df_reflexivo, df_random, dirty_rates,sizes):

    for size in sizes:
        resultados = performance_promedio_suciedad(df_reflexivo, df_random,dirty_rates, f'{size}x{size}')
        
        plt.plot(dirty_rates, resultados[0], label='Agente Reflexivo', marker='o', linestyle='--')
        plt.plot(dirty_rates, resultados[1], label='Agente Random', marker='o', linestyle='--')
        
        plt.title(f'Comparación de Performance para entorno {size}x{size}')
        plt.xlabel('Porcentaje de suciedad')
        plt.ylabel('Performance promedio')
        plt.legend()
        plt.grid(True)
        

        plt.show()

def graficos_performance_entorno(df_reflexivo, df_random, dirty_rates, sizes):

    sizes_str = [f'{size}x{size}' for size in sizes]

    for rate in dirty_rates:
        resultados = performance_promedio_entorno(df_reflexivo, df_random, rate, sizes)
        
        plt.plot(sizes_str, resultados[0], label='Agente Reflexivo', marker='o', linestyle='--')
        plt.plot(sizes_str, resultados[1], label='Agente Random', marker='o', linestyle='--')
        
        plt.title(f'Comparación de Performance con {rate*100}% de suciedad')
        plt.xlabel('Entornos')
        plt.ylabel('Performance promedio')
        plt.legend()
        plt.grid(True)
        
        # Muestra el gráfico para el tamaño actual
        plt.show()

def graficos_moves_entorno(df_reflexivo, df_random, dirty_rates, sizes):

    sizes_str = [f'{size}x{size}' for size in sizes]


    for rate in dirty_rates:
        resultados = necessary_moves_promedio_entorno(df_reflexivo, df_random, rate, sizes)
        
        plt.plot(sizes_str, resultados[0], label='Agente Reflexivo', marker='o', linestyle='--')
        plt.plot(sizes_str, resultados[1], label='Agente Random', marker='o', linestyle='--')
        
        plt.title(f'Comparación de Performance con {rate*100}% de suciedad')
        plt.xlabel('Entornos')
        plt.ylabel('Promedio de movimientos necesarios')
        plt.legend()
        plt.grid(True)
        
        # Muestra el gráfico para el tamaño actual
        plt.show()

def grafico_caja_extensiones(df_reflexivo,df_random,dirty_rates):
    # Crear gráficos de performance en función del tamaño del entorno
    # Añadir columna para identificar al agente
    df_reflexivo['Agent'] = 'Reflexivo'
    df_random['Agent'] = 'Random'

    # Combinar los DataFrames
    df_combined = pd.concat([df_reflexivo, df_random])
    for rate in dirty_rates:
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='Size', y='Performance', hue='Agent', data=df_combined[df_combined['Dirty Rate'] == rate])
        plt.title(f'Comparación de Performance entre Agentes con {rate*100}% de suciedad')
        plt.xlabel('Tamaño del Entorno')
        plt.ylabel('Performance')
        plt.grid(True)
        plt.show()