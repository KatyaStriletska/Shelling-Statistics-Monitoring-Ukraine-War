from data_processing import load_and_process_data, merge_two_datas_by_model
from visualization import plot_total_reached_and_destroyed_by_category, plot_launched_vs_destroyed_by_model
def main():
    file_path = "data/missile_attacks_daily.csv"

    # Завантажуємо та обробляємо дані
    df_massive_attacks = load_and_process_data(file_path)
    plot_launched_vs_destroyed_by_model(df_massive_attacks)
if __name__ == "__main__":
    main()
