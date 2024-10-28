import pandas as pd
import numpy as np


def load_and_process_data() -> pd.DataFrame:
    df_massive_attacks = pd.read_csv("data/missile_attacks_daily.csv")

    # preprocessing data for missile_attacks_daily.csv

    # transform in correct type
    # print(f"Data types before: \n {df_massive_attacks.dtypes} \nShape: {df_massive_attacks.shape}")

    def parse_datetime(val):
        val = val.strip() 
        try:
            return pd.to_datetime(val, format='%Y-%m-%d %H:%M', errors='raise')
        except ValueError:
            return pd.to_datetime(val, format='%Y-%m-%d') + pd.Timedelta(hours=0)
        
    df_massive_attacks["time_start"] = df_massive_attacks["time_start"].apply(parse_datetime)
    df_massive_attacks["time_end"] = df_massive_attacks["time_end"].apply(parse_datetime)

    # print(f"\nData types after: \n {df_massive_attacks.dtypes} \nShape: {df_massive_attacks.shape}")

    # Checking for null/missing values
    # print("\nSum of null/missing values: \n", df_massive_attacks.isnull().sum())
    df_massive_attacks = df_massive_attacks.drop(["launched_details", "launch_place_details", "still_attacking", "cross_border_belarus"],  axis=1)
    # print("\nSum of null/missing values after dropping: \n", df_massive_attacks.isnull().sum())

# Checking for duplicate values
# print(f"Duplicate values: {df_massive_attacks.duplicated().sum()}")
# print(f"Shape after drpopping: {df_massive_attacks.shape}")

# print(df_massive_attacks.describe())

    # Transform empty 'launch_place' values 
    df_massive_attacks['launch_place'] = df_massive_attacks['launch_place'].str.split(' and ')
    df_massive_attacks = df_massive_attacks.explode('launch_place')
    mode_launch_place = df_massive_attacks['launch_place'].mode()[0]

    df_massive_attacks['launch_place'] = df_massive_attacks['launch_place'].fillna(mode_launch_place)
    most_common_places = df_massive_attacks['launch_place'].value_counts()
    
    df_massive_attacks['model'] = df_massive_attacks['model'].str.split(' and ')    
    df_massive_attacks = df_massive_attacks.explode('model')
    df_massive_attacks['model'] = df_massive_attacks['model'].replace(['C-300', 'C-400'], 'C-300/C-400')
    df_massive_attacks['model'] = df_massive_attacks['model'].replace(['Iskander-M', 'KN-23'], 'Iskander-M/KN-23')
    df_massive_attacks['model'] = df_massive_attacks['model'].replace(['X-59', 'X-69', 'X-59/X-69\t'], 'X-59/X-69')
    

# Transform 'back_russia' column with replacing Nan value
# if the value is zero, it means that nothing was returned back to russia
    df_massive_attacks["back_russia"] = df_massive_attacks["back_russia"].fillna(0.0)


# Transform 'not_reach_goal' column with replacing Nan value
# if the value is zero, it means that nothing was reach 
    df_massive_attacks["not_reach_goal"] = df_massive_attacks["not_reach_goal"].fillna(0.0)

    print("\nSum of null/missing values: \n", df_massive_attacks.isnull().sum())
    print(f"Shape after drpopping: {df_massive_attacks.shape}")

    print(df_massive_attacks[0::100])
    return df_massive_attacks

def merge_two_data(df_missiles_daily: pd.DataFrame):
    df_missiles_description = pd.read_csv("data/missiles_and_uav.csv")
    df_missiles_description['model'] = df_missiles_description['model'].str.split(' and ')

    df_missiles_description = df_missiles_description.explode('model')
    
    df_missiles_description['model'] = df_missiles_description['model'].replace(['C-300', 'C-400'], 'C-300/C-400')
    df_missiles_description['model'] = df_missiles_description['model'].replace(['Iskander-M', 'KN-23'], 'Iskander-M/KN-23')
    df_missiles_description['model'] = df_missiles_description['model'].replace(['X-59', 'X-69', 'X-59/X-69\t'], 'X-59/X-69')
    df_missiles_description['model'] = df_missiles_description['model'].replace(['X-555', 'X-101'], 'X-101/X-555')
    df_missiles_daily["year"] = df_missiles_daily["time_start"].dt.year

    df_missiles = df_missiles_daily.merge(df_missiles_description, how='left', on=['model'])
    
    return df_missiles

def get_data_of_weapon_by_year(df_missiles: pd.DataFrame):
    df_missiles = df_missiles.groupby(['year', 'category','model'], dropna=True)[['launched', 'destroyed']].sum()
    df_missiles['reached_goal'] = df_missiles['launched'] - df_missiles['destroyed']
    return df_missiles

def get_category_of_weapon(df: pd.DataFrame):
    df_missiles = df.groupby('category')['model'].unique().reset_index()
    df_missiles['model'] = df_missiles['model'].apply(list)
    return df_missiles 

#df_missiles it is merged daily and uav dataset
#func fir getting all of the categories if weapons per year
def get_categories_for_year(df_missiles: pd.DataFrame, year: int):
    filtered_df = df_missiles.xs(year, level='year')
    unique_categories = filtered_df.index.get_level_values('category').unique()
    return unique_categories.tolist()
