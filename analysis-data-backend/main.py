from data_processing import load_and_process_data
from visualization import plot_total_launched_and_destroyed_per_year
def main():
    file_path = "data/missile_attacks_daily.csv"

    df_massive_attacks = load_and_process_data(file_path)
    

    plot_total_launched_and_destroyed_per_year(df_massive_attacks, 2024)
    
if __name__ == "__main__":
    main()
