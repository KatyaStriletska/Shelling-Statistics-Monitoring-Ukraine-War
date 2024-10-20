import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.graph_objects as go
   
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
        line=dict(color='blue'),  
    ))

    fig.add_trace(go.Scatter(
        x=monthly_stats['month'],  
        y=monthly_stats['destroyed'],
        mode='lines+markers',  
        name='Destroyed',  
        line=dict(color='red'), 
    ))
    
    fig.update_layout(
    title=f'Total launched and destroyed per month in {year}',  
    xaxis_title='Month',  
    yaxis_title='Count',  
    xaxis_tickmode='array', 
    xaxis_tickvals=list(range(1, 13)), 
    xaxis_ticktext=[
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ],  
    showlegend=True,     
    )
    # fig.write_html("../../static/interactiveCharts/linechart-plotly-basic.html")
    fig.write_html("linechart-plotly-basic.html") 
    fig.show()
    