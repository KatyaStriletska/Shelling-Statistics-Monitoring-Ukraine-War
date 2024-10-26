from data_processing import load_and_process_data, merge_two_datas_by_model, get_categories_for_year
from visualization import plot_total_launched_and_destroyed_per_year, plot_total_launched_and_destroyed_per_category_and_year


# from visualization import plot_total_launched_and_destroyed_per_year_itaractive
from visualization import chart_most_common_weapons_per_year

def main():
    file_path = "/Users/admin/Documents/Shelling-Statistics-Monitoring-Ukraine-War/data/missile_attacks_daily.csv"

    # Завантажуємо та обробляємо дані
    df_massive_attacks = load_and_process_data(file_path)

    df_merged_with_categories = merge_two_datas_by_model(df_massive_attacks)

    # print(df_massive_attacks.head(10))

    # Створюємо графіки
    # plot_launch_places_distribution(df_massive_attacks, )
    # plot_time_series(df_massive_attacks)
    # chart_most_common_weapons_per_year(df_massive_attacks, 2023)

    # plot_total_launched_and_destroyed_per_year_itaractive(df_massive_attacks, 2024)


    # plot_total_launched_and_destroyed_per_year(df_massive_attacks, 2024)

    plot_total_launched_and_destroyed_per_category_and_year(2024, "UAV", df_merged_with_categories)

if __name__ == "__main__":
    main()
