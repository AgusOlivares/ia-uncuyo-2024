import gymnasium as gym
import map as map
import random
import algorithms as algo
import analisis as la
import pandas as pd

"""
seed = 308289337
size = 10
p_hole = 0.08
start = (random.randint(0, size - 1), random.randint(0, size - 1))
end = (random.randint(0, size - 1), random.randint(0, size - 1))
e = map.Map(size, p_hole, start, end)
env = e.env  # Me quedo con el entorno
path , states = algo.dfs(e.grid , start,end)
env.reset()
print(f"{la.calculate_cost(path)} , cantidad de estados: {states}" )
la.iniciarEnv(env,path)
"""

#Crear un DataFrame de los resultados
df = pd.DataFrame(la.init_algorithms())

#Guardar los resultados en un archivo Excel
df.to_excel("Resultados_Simulacion.xlsx", index=False)

df = pd.read_excel("Resultados_Simulacion.xlsx")
la.plot_solution_counts(df)
la.box_states(df)
la.box_cost_e1(df)
la.box_cost_e2(df)
la.box_times(df)
print("Simulaciones completadas y resultados guardados en Resultados_Simulacion.xlsx")