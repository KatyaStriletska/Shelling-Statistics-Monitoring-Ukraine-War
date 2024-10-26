import pandas as pd
from collections import Counter
import plotly.graph_objects as go
import json
import plotly.utils 
import matplotlib.pyplot as plt
import plotly.offline as pyo


def plot_destroyed_vs_not_destroyed_by_model_and_month(df: pd.DataFrame):
    # Додавання колонок для року та місяця
    df['year'] = df['time_start'].dt.year
    df['month'] = df['time_start'].dt.month
    df['not_destroyed'] = df['launched'] - df['destroyed']
    
    # Групування по моделям, рокам і місяцям
    model_month_stats = df.groupby(['model', 'year', 'month']).agg({
        'destroyed': 'sum',
        'not_destroyed': 'sum'
    }).reset_index()

    # Фільтруємо дані для конкретного року (наприклад, 2023)
    year_data = model_month_stats[model_month_stats['year'] == 2023]
    
    # Побудова графіка
    fig = px.bar(
        year_data, 
        x='month', 
        y=['destroyed', 'not_destroyed'], 
        color='model', 
        title='Destroyed vs Not Destroyed Missiles by Model and Month (2023)',
        labels={'value': 'Count', 'month': 'Month'},
        barmode='stack'  # Stack для збитих/не збитих
    )
    
    # Оновлення підписів місяців
    fig.update_layout(
        xaxis=dict(
            tickmode='array',
            tickvals=list(range(1, 13)),
            ticktext=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        )
    )
    
    pyo.plot(fig, filename='missile_stats_offline.html')

# Виклик функції для DataFrame
# plot_destroyed_vs_not_destroyed_by_model_and_month(df)

def plot_launched_vs_destroyed_by_model_and_month(df: pd.DataFrame):
    # Додавання колонок для року та місяця
    df['year'] = df['time_start'].dt.year
    df['month'] = df['time_start'].dt.month
    df['not_destroyed'] = df['launched'] - df['destroyed']
    
    # Групування по моделям, рокам і місяцям
    model_month_stats = df.groupby(['model', 'year', 'month']).agg({
        'launched': 'sum',
        'destroyed': 'sum',
        'not_destroyed': 'sum'
    }).reset_index()
    
    years = model_month_stats['year'].unique()
    
    for year in years:
        fig = go.Figure()
        year_data = model_month_stats[model_month_stats['year'] == year]
        
        for model in year_data['model'].unique():
            model_data = year_data[year_data['model'] == model]
            
            # Додавання стовпців для запущених
            fig.add_trace(go.Bar(
                x=model_data['month'],
                y=model_data['launched'],
                name=f'Launched - {model}',
                marker_color='blue'
            ))
            
            # Додавання стовпців для збитих
            fig.add_trace(go.Bar(
                x=model_data['month'],
                y=model_data['destroyed'],
                name=f'Destroyed - {model}',
                marker_color='red'
            ))
            
            # Додавання стовпців для не збитих
            fig.add_trace(go.Bar(
                x=model_data['month'],
                y=model_data['not_destroyed'],
                name=f'Not Destroyed - {model}',
                marker_color='orange'
            ))
        
        # Налаштування вигляду графіка
        fig.update_layout(
            barmode='stack',
            title=f'Missiles Launched vs Destroyed by Model in {year}',
            xaxis_title='Month',
            yaxis_title='Count',
            showlegend=True,
            xaxis=dict(
                tickmode='array',
                tickvals=list(range(1, 13)),
                ticktext=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            )
        )
        pyo.plot(fig, filename='missile_stats_offline.html')
  
        # fig.show()

# Виклик функції для DataFrame
# plot_launched_vs_destroyed_by_model_and_month(df)


def plot_launched_vs_destroyed_by_model(df: pd.DataFrame):
    
    df = df[df['time_start'].dt.year == 2022 and dt.month ]
    df['not_destroyed'] = df['launched'] - df['destroyed']
    
    model_stats = df.groupby('model').agg({
        'launched': 'sum',
        'destroyed': 'sum',
        'not_destroyed': 'sum'
    }).reset_index()
    
    fig = go.Figure()
    
    # Додати стовпці для запущених
    fig.add_trace(go.Bar(
        x=model_stats['model'],
        y=model_stats['launched'],
        name='Launched',
        marker_color='blue'
    ))
    
    # Додати стовпці для збитих
    fig.add_trace(go.Bar(
        x=model_stats['model'],
        y=model_stats['destroyed'],
        name='Destroyed',
        marker_color='red'
    ))
    
    # Додати стовпці для не збитих
    fig.add_trace(go.Bar(
        x=model_stats['model'],
        y=model_stats['not_destroyed'],
        name='Not Destroyed',
        marker_color='orange'
    ))
    
    fig.update_layout(
        barmode='stack',
        title='Launched vs Destroyed Missiles by Model',
        xaxis_title='Missile Model',
        yaxis_title='Count',
        showlegend=True
    )
    pyo.plot(fig, filename='missile_stats_offline.html')

    # fig.show()

# Виклик функції
# plot_launched_vs_destroyed_by_model(df)

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

    # fig.show()

def chart_most_common_weapons_per_year(data: pd.DataFrame, year: int):
    data_by_years = data[data["time_start"].dt.year == year]
    # print(data_by_years.groupby(["model"]).count())

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

    print(models)
    print(percentages)

    colors = ["#2b472f", "#3e5334", "#4a6047", "#556a48", "#6d8162", "#718970",
              "#889a80", "#9fb29e", "#a6b899", "#c0cfc0", "#d8e8d1"]

    fig = go.Figure(data=[go.Pie(labels=models, values=percentages,
                                 hoverinfo="none",
                                 textinfo="none",
                                 marker=dict(colors=colors),
                                 hovertemplate="Model: %{label}<br>Percentage: %{percent}<extra></extra>",
                                 hole=0.5)])

    fig.update_layout(title_text="Most common models of weapons")
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    # fig.show()


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
    title=f'Total launched and destroyed per month in {year}',  
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


def plot_total_reached_and_destroyed_by_category(df: pd.DataFrame):
    # df['reached_goal'] = df['launched'] - df['destroyed']
    df = df.reset_index()

    fig = go.Figure()
    
    # Додати стовпці для запущених
    fig.add_trace(go.Bar(
        x=df['destroyed'],  # Змінено на x
        y=df['category'],  # Змінено на y
        name='Destroyed',
        orientation='h',
        marker_color='red'
    ))

    
    # Додати стовпці для досягнутого
    fig.add_trace(go.Bar(
        x=df['reached_goal'],  # Змінено на x
        y=df['category'],  # Змінено на y
        name='Reached Goal',
        marker_color='blue',
        orientation='h',
    ))
    
    fig.update_layout(
        barmode='stack',  # Можна залишити 'group' якщо потрібно
        title='Launched vs Destroyed Missiles by Category',
        xaxis_title='Count',
        yaxis_title='Category',
        showlegend=True
        
    )
    
    pyo.plot(fig, filename='missile_stats_offline.html')
