import agent as a
import enviroment as e
import pandas as pd
import random
import matplotlib.pyplot as plt
import agentsResults as ar



# Definimos los tamaños y los porcentajes de suciedad
sizes = [2, 4, 8, 16, 32, 64, 128]
dirty_rates = [0.1, 0.2, 0.4, 0.8]
"""

# Para generar nuevos resultados descomentar las siguientes lineas:

# Convierto los resultados a DataFrames de pandas
results = ar.resultados_agentes(sizes, dirty_rates)
df_reflexivo = pd.DataFrame(results[0])
df_random = pd.DataFrame(results[1])

# Guardo los resultados en archivos Excel separados
df_reflexivo.to_excel('./tp2-agentes-racionales/code/agente_reflexivo_resultados.xlsx', index=False)
df_random.to_excel('./tp2-agentes-racionales/code/agente_random_resultados.xlsx', index=False)

print("Los archivos Excel han sido generados")
"""



# Cargar los datos desde los archivos Excel
df_reflexivo = pd.read_excel('/home/agus3112/Documents/Facu/IA1/ia-uncuyo-2024/tp2-agentes-racionales/code/agente_reflexivo_resultados.xlsx')
df_random = pd.read_excel('/home/agus3112/Documents/Facu/IA1/ia-uncuyo-2024/tp2-agentes-racionales/code/agente_random_resultados.xlsx')

ar.graficos_performance_entorno(df_reflexivo, df_random, dirty_rates, sizes)
ar.graficos_performance_dirtyRate(df_reflexivo, df_random, dirty_rates, sizes)
ar.graficos_moves_entorno(df_reflexivo, df_random, dirty_rates, sizes)
ar.grafico_caja_extensiones(df_reflexivo, df_random, dirty_rates)

