import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_total_launched_and_destroyed_per_year(df: pd.DataFrame, year: int):
    df_year = df[df['time_start'].dt.year == year]
    df_year['month'] = df_year['time_start'].dt.month
    monthly_stats = df_year.groupby('month').size().reset_index(name='count')
    plt.figure(figsize=(8, 6)) # Width and Height of the chart
sns.lineplot(x='x',
             y='y',
             data=df,
             marker='o', # Style used to mark the join between 2 points
            )
plt.xlabel('X-axis') # x-axis name
plt.ylabel('Y-axis') # y-axis name
plt.title('Simple Connected Scatter Plot') # Add a title
plt.show() # Display the graph
    # print(monthly_stats)