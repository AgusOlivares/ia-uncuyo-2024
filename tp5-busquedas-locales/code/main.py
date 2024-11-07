from algorithms import hill_climbing, simulated_annealing, genetic_algorithm
from results import *

def main():
    n_queens_values = [4, 8, 10]  # Tamaños de tablero
    algorithms = {
        # "Hill Climbing": hill_climbing,
        # "Simulated Annealing": simulated_annealing,
        "Genetic Algorithm": genetic_algorithm
    }
    
    all_results = {}

    for algo_name, algorithm in algorithms.items():
        for n_queens in n_queens_values:
            print(f"Ejecutando {algo_name} para {n_queens} reinas...")
            
            # Corre los experimentos y obtiene resultados
            results = run_experiment(algorithm, n_queens)
            all_results[f"{algo_name}_{n_queens}"] = results

            # Guarda resultados en CSV
            filename = f"{algo_name}_{n_queens}_results.csv"
            save_results_to_csv(results, filename)

            # Calcula estadísticas y guarda
            stats = calculate_statistics(results)
            print(f"Estadísticas para {algo_name} ({n_queens} reinas): {stats}")

            # Genera gráficos de caja y bigotes para tiempos y estados visitados
            generate_boxplot(results["time_taken"], f"{algo_name} - Tiempo de Ejecución ({n_queens} reinas)", 
                             "Tiempo (s)", f"{algo_name}_{n_queens}_boxplot_time.png")
            generate_boxplot(results["states_visited"], f"{algo_name} - Estados Visitados ({n_queens} reinas)", 
                             "Estados Visitados", f"{algo_name}_{n_queens}_boxplot_states.png")

            # Graficar variación de heurística en una ejecución representativa
            h_values = results["heuristic_variation"][0]  # Toma la primera ejecución como representativa
            plot_heuristic_variation(h_values, f"{algo_name} ({n_queens} reinas)")

if __name__ == "__main__":
    main()
