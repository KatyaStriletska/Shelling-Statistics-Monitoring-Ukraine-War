import pandas as pd
from collections import Counter
import plotly.graph_objects as go
import json
import plotly.utils 
import matplotlib.pyplot as plt
import plotly.offline as pyo

def plot_launched_by_model_per_month(df: pd.DataFrame):
    # Додавання місяця
    df['month'] = df['time_start'].dt.to_period('M')
    
    # Групування по моделям і місяцям
    model_month_stats = df.groupby(['month', 'model']).agg({
        'launched': 'sum'
    }).reset_index()
    
    fig = go.Figure()
    
    # Додавання ліній для кожної моделі
    for model in model_month_stats['model'].unique():
        model_data = model_month_stats[model_month_stats['model'] == model]
        fig.add_trace(go.Scatter(
            x=model_data['month'].astype(str), 
            y=model_data['launched'], 
            mode='lines+markers',
            name=model
        ))
    
    fig.update_layout(
        title='Launched Missiles per Month by Model',
        xaxis_title='Month',
        yaxis_title='Launched',
        showlegend=True,
        xaxis_tickmode='array',
        xaxis_tickvals=model_month_stats['month'].astype(str).unique(),
    )
    pyo.plot(fig, filename='missile_stats_offline.html')

def chart_most_common_weapons_per_year(data: pd.DataFrame, year: int):
    data_by_years = data[data["time_start"].dt.year == year]
    counter = Counter(data_by_years["model"])
    top_10 = counter.most_common(10)
    total_count = len(data_by_years["model"])

    models = []
    percentages = []

    for value, count in top_10:
        models.append(value)
        percentages.append((count / total_count) * 100)

    models.append("Other")
    percentages.append(100 - sum(percentages))

    colors = ["#2b472f", "#3e5334", "#4a6047", "#556a48", "#6d8162", "#718970",
              "#889a80", "#9fb29e", "#a6b899", "#c0cfc0", "#d8e8d1"]

    fig = go.Figure(data=[go.Pie(labels=models, values=percentages,
                                 hoverinfo="none",
                                 textinfo="none",
                                 marker=dict(colors=colors),
                                 hovertemplate="Model: %{label}<br>Percentage: %{percent}<extra></extra>",
                                 hole=0.5)])
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

def chart_most_common_category_per_year(df: pd.DataFrame, year:int):
    data_by_years = df.xs(year, level='year')
    category_sums = data_by_years.groupby('category')['launched'].sum().reset_index()
    
    labels = category_sums['category']
    values = category_sums['launched']

    colors = ["#2b472f", "#d8e8d1", "#556a48", "#6d8162", "#718970",
              "#889a80", "#9fb29e", "#a6b899", "#c0cfc0", "#d8e8d1"]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values,
                                 hoverinfo="label+percent",
                                 textinfo="none",
                                 marker=dict(colors=colors),
                                 hovertemplate="Category: %{label}<br>Percentage: %{percent}<extra></extra>",
                                 hole=0.5)])
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)


def plot_total_launched_and_destroyed_per_launch_place(df: pd.DataFrame):
    df_launch_place = df.groupby('launch_place').agg({
        'launched': 'sum',
        'destroyed': 'sum'
    }).reset_index()
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_launch_place['launch_place'],
        y=df_launch_place['launched'],
        mode='lines+markers',
        name='Launched',  
        line=dict(color='#3e5334'),  
    ))

    fig.add_trace(go.Scatter(
        x=df_launch_place['launch_place'],
        y=df_launch_place['destroyed'],
        mode='lines+markers',  
        name='Destroyed',  
        line=dict(color='#889a80'), 
    ))

    fig.update_layout(
    xaxis_title='Month',  
    yaxis_title='Count',  
    plot_bgcolor='rgba(240, 240, 240, 0.8)',   
    paper_bgcolor='rgba(255, 255, 255, 1)', 
    xaxis_tickangle=-45,
    hoverlabel=dict(
        font_size=12,       
        font_family="Arial" 
    ),
    showlegend=True,     
    )
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)


def plot_total_launched_and_destroyed_per_year(df: pd.DataFrame, year: int):
    df_year = df[df['time_start'].dt.year == year].copy()
    df_year.loc[:, 'month'] = df_year['time_start'].dt.month

    monthly_stats = df_year.groupby('month').agg({
        'launched': 'sum',
        'destroyed': 'sum'
    }).reset_index()
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=monthly_stats['month'],
        y=monthly_stats['launched'],
        mode='lines+markers',
        name='Launched',  
        line=dict(color='#3e5334'),  
    ))

    fig.add_trace(go.Scatter(
        x=monthly_stats['month'],
        y=monthly_stats['destroyed'],
        mode='lines+markers',  
        name='Destroyed',  
        line=dict(color='#889a80'), 
    ))

    fig.update_layout(
    xaxis_title='Month',  
    yaxis_title='Count',  
    xaxis_tickmode='array', 
    xaxis_tickvals=list(range(1, 13)), 
    plot_bgcolor='rgba(240, 240, 240, 0.8)',   
    paper_bgcolor='rgba(255, 255, 255, 1)', 
    xaxis_ticktext=[
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ],  
    hoverlabel=dict(
        font_size=12,       
        font_family="Arial" 
    ),
    showlegend=True,     
    )
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

def plot_total_launched_and_destroyed_per_category_and_year(year: int, category: str, df: pd.DataFrame):
    grouped_data = df.xs((year, category), level=('year', 'category'))
    if grouped_data.empty:
        print(f'No data available for {year} in category "{category}".')
        return

    models = grouped_data.index.tolist()
    launched = grouped_data['launched'].tolist()
    destroyed = grouped_data['destroyed'].tolist()
    reached_goal = grouped_data['reached_goal'].tolist()

    fig = go.Figure()

    fig.add_trace(go.Bar(x=models, y=launched, name='Launched', 
                         hovertemplate='Launched<br>%{x}: %{y}<extra></extra>', 
                         marker_color="#3e5334"))

    fig.add_trace(go.Bar(x=models, y=destroyed, name='Destroyed', 
                         hovertemplate='Destroyed<br>%{x}: %{y}<extra></extra>', 
                         marker_color="#6d8162"))

    fig.add_trace(go.Bar(x=models, y=reached_goal, name='Reached Goal', 
                         hovertemplate='Reached Goal<br>%{x}: %{y}<extra></extra>', 
                         marker_color="#c0cfc0"))

    fig.update_layout(xaxis_title='Models',
                      yaxis_title='Amount',
                      xaxis_tickangle=-45,
                      plot_bgcolor='#f1f1ec' ,
                      barmode='group')
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)