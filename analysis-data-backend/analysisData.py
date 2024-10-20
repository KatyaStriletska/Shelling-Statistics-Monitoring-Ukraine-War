import pandas as pd
import numpy as np

df_massive_attacks = pd.read_csv("data\missile_attacks_daily.csv")

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
# df_massive_attacks['launch_place'] = df_massive_attacks['launch_place'].astype('category')
# print(most_common_places)



# Transform 'back_russia' column with replacing Nan value
# if the value is zero, it means that nothing was returned back to russia
df_massive_attacks["back_russia"] = df_massive_attacks["back_russia"].fillna(0.0)


# Transform 'not_reach_goal' column with replacing Nan value
# if the value is zero, it means that nothing was reach 
df_massive_attacks["not_reach_goal"] = df_massive_attacks["not_reach_goal"].fillna(0.0)

print("\nSum of null/missing values: \n", df_massive_attacks.isnull().sum())
print(f"Shape after drpopping: {df_massive_attacks.shape}")
df_year = df_massive_attacks[df_massive_attacks['time_start'].dt.year == 2024]
# Assuming df_year is a slice of another DataFrame
df_year.loc[:, 'month'] = df_year['time_start'].dt.month
monthly_stats = df_year.groupby('month').agg({
        'launched': 'sum',
        'destroyed': 'sum'
    }).reset_index()
print(monthly_stats)