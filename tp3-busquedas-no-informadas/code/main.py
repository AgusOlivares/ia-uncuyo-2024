import gymnasium as gym
import map as map
import random
import algorithms as algo
import analisis as la
import pandas as pd


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