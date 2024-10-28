from data_processing import load_and_process_data, get_data_of_weapon_by_year, get_categories_for_year, get_category_of_weapon, merge_two_data
from visualization import plot_total_launched_and_destroyed_per_year, plot_total_launched_and_destroyed_per_category_and_year, chart_most_common_category_per_year


# from visualization import plot_total_launched_and_destroyed_per_year_itaractive
from visualization import chart_most_common_weapons_per_year

def main():
    main_df = load_and_process_data()
    merged_df = merge_two_data(main_df)
    df_category_of_weapon = get_category_of_weapon(merged_df)
    df_weapon_by_year = get_data_of_weapon_by_year(merged_df)
    print("Sum ", main_df['launched'].sum())

    print(main_df.head(10))
    print(df_weapon_by_year.head(10))
if __name__ == "__main__":
    main()
