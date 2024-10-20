from data_processing import load_and_process_data
# from visualization import plot_launch_places_distribution, plot_time_series

def main():
    # Шлях до вашого CSV файлу
    file_path = "data/missile_attacks_daily.csv"

    # Завантажуємо та обробляємо дані
    df_massive_attacks = load_and_process_data(file_path)
    
    # Створюємо графіки
    # plot_launch_places_distribution(df_massive_attacks, )
    # plot_time_series(df_massive_attacks)

if __name__ == "__main__":
    main()
