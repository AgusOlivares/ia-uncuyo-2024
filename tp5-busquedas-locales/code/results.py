import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tablero import Tablero  # Archivo donde se define la estructura del tablero
from algorithms import hill_climbing, simulated_annealing, genetic_algorithm  # Importa algoritmos

def run_experiment(algorithm, n_queens, runs=30):
    results = {
        "time_taken": [],
        "optimal_solution": 0,
        "states_visited": [],
        "heuristic_variation": []  # Almacena la variación de la heurística
    }
    
    for _ in range(runs):
        start_time = time.time()
        solution, heuristic_path = algorithm(n_queens)  # Ajusta para capturar `heuristic_path`
        end_time = time.time()
        
        elapsed_time = end_time - start_time
        results["time_taken"].append(elapsed_time)
        results["states_visited"].append(len(solution.visited_states))
        results["heuristic_variation"].append(heuristic_path)  # Guarda la variación de la heurística
        
        if solution.calculate_heuristic() == 0:
            results["optimal_solution"] += 1
            
    return results


def save_results_to_csv(results, filename="results.csv"):
    df = pd.DataFrame(results)
    df.to_csv(filename, index=False)

def calculate_statistics(results):
    optimal_percentage = (results["optimal_solution"] / len(results["time_taken"])) * 100
    avg_time = np.mean(results["time_taken"])
    std_time = np.std(results["time_taken"])
    avg_states = np.mean(results["states_visited"])
    std_states = np.std(results["states_visited"])
    
    return {
        "Optimal Percentage": optimal_percentage,
        "Average Time": avg_time,
        "Std Dev Time": std_time,
        "Average States": avg_states,
        "Std Dev States": std_states
    }

def generate_boxplot(data, title, y_label, filename):
    sns.boxplot(data=data)
    plt.title(title)
    plt.ylabel(y_label)
    plt.savefig(filename)
    plt.close()

def plot_heuristic_variation(heuristic_values, algorithm_name):
    plt.plot(heuristic_values, marker='o')
    plt.title(f'Variación de H para {algorithm_name}')
    plt.xlabel('Iteración')
    plt.ylabel('Valor de H')
    plt.show()
