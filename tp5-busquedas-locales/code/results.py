import matplotlib.pyplot as plt
import seaborn as sns
import tablero 
import time
import algorithms as algo
import pandas as pd
import ast
import random
class PlotUtils:

    @staticmethod
    def generateResults(tableros, algorithm):
        # Crear una lista para almacenar los resultados
        resultados = []

        for tablero in tableros:
            print(f"Tamaño del tablero: {len(tablero)}")
            # Medir tiempo de ejecución
            start_time = time.time()
            
            # Aplicar Algoritmo
            if (algorithm is not algo.geneticAlgorithm):
                solucion, conflictos, moves , h_e_list = algorithm(tablero)
            else:
                solucion, conflictos, moves , h_e_list = algorithm(len(tablero))
                
            
            # Medir tiempo final de ejecución
            end_time = time.time()
            tiempo_ejecucion = end_time - start_time
            
            # Almacenar resultados en la lista
            resultados.append({
                "Tablero inicial": tablero,
                "Tamaño del tablero": len(tablero),
                "Tablero solución": solucion,
                "Número de conflicos": conflictos,
                "Cantidad de Movimientos": moves,
                "Tiempo (segundos)": tiempo_ejecucion,
                "Historial de reinas amenazadas": h_e_list
            })

        return resultados
    
    @staticmethod
    def generarTableros(sizes, iterations):
        
        tableros = []
        for size in sizes:
            for _ in range(iterations):
                tablero_inicial = tablero.generarTablero(size)
                tableros.append(tablero_inicial)
        return tableros
        

    @staticmethod 
    def lineChart(ejeX, ejeY, labelX:str, labelY:str, legend_str:str, title:str):
        
        plt.plot(ejeX, ejeY, label=legend_str, marker='o', linestyle='--')
        
        plt.title(title)
        plt.xlabel(labelX)
        plt.ylabel(labelY)
        plt.legend()
        plt.grid(True)
        plt.ylim(-1,30)
        # Muestra el gráfico para el tamaño actual
        plt.show()


    @staticmethod
    def boxplot(dataframe, ejeX:str, ejeY:str, title:str,):
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=ejeX, y=ejeY, data=dataframe)
        plt.title(title)
        plt.xlabel(ejeX)
        plt.ylabel(ejeY)
        plt.show()

    @staticmethod
    def filtrarTableroSinConflictos(dataframe, size, index):

        # Filtrar por tamaño del tablero 
        filtro = (dataframe["Tamaño del tablero"] == size) 
        filtered_df = dataframe[filtro]

        return filtered_df.iloc[index]
        
    @staticmethod
    def h_function(dataframe , size , nombre_algoritmo , index):
        filtered_df = PlotUtils.filtrarTableroSinConflictos(dataframe, size, index)
        print(f"Tablero inicial: {filtered_df["Tablero inicial"]}")
        print(f"Cantidad de Movimientos: {filtered_df["Cantidad de Movimientos"]}")
        print(f"Historial: {filtered_df["Historial de reinas amenazadas"]}")
        print(f"Numero de conflictos: {filtered_df["Número de conflicos"]}")
        print(f"Tablero solución: {filtered_df["Tablero solución"]}")

        historial_reinas_amenazadas = ast.literal_eval(filtered_df["Historial de reinas amenazadas"]) # Convierto la lista en forma de string en lista
        ejeX = []
        for i in range(len(historial_reinas_amenazadas)):
            ejeX.append(i)

        titulo = "Historial de reinas amenazadas" + " "+ nombre_algoritmo
        PlotUtils.lineChart(ejeX , historial_reinas_amenazadas ,"Iteraciones", 
                            "Par de reinas atacadas", nombre_algoritmo , titulo)
        print("--"*20)

    @staticmethod
    def percentage(dataframe, iterations):
        return (len(dataframe) / iterations) * 100

    @staticmethod
    def calculate_solution_percentage_by_size(dataframe , sizes ,iterations):
        
        percentage_list = []
        for size in sizes:
            filter = (dataframe["Tamaño del tablero"] == size) & (dataframe["Número de conflicos"] == 0)
            filtered_df = dataframe[filter]
            percentage_list.append(PlotUtils.percentage(filtered_df, iterations))
        return percentage_list

    @staticmethod
    def plot_percentage_by_sizes(sizes, percentages: list, algoritmo: str):
        plt.figure(figsize=(10, 6))
        sizes_str = [str(size) for size in sizes]
        plt.bar(sizes_str, percentages, color='skyblue')
        
        # Añadir etiquetas a cada barra
        for i, percentage in enumerate(percentages):
            plt.text(i, percentage + 1, f"{percentage:.3f}%", ha='center', va='bottom', fontsize=10)
        
        plt.xlabel("Tamaño del tablero")
        plt.ylabel("Porcentaje de soluciones")
        plt.title(f"Porcentaje de veces que se encontró solución: {algoritmo}")
        
        # Establecer los límites del eje Y de 0 a 100
        plt.ylim(0, 110)
        
        plt.show()