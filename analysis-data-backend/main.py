from data_processing import load_and_process_data
from visualization import plot_total_launched_and_destroyed_per_year


# from visualization import plot_total_launched_and_destroyed_per_year_itaractive
from visualization import chart_most_common_weapons_per_year

def main():
    file_path = "data/missile_attacks_daily.csv"

    # Завантажуємо та обробляємо дані
    df_massive_attacks = load_and_process_data(file_path)

    # Створюємо графіки
    # plot_launch_places_distribution(df_massive_attacks, )
    # plot_time_series(df_massive_attacks)
    chart_most_common_weapons_per_year(df_massive_attacks, 2023)

    # plot_total_launched_and_destroyed_per_year_itaractive(df_massive_attacks, 2024)


    plot_total_launched_and_destroyed_per_year(df_massive_attacks, 2024)

if __name__ == "__main__":
    main()
