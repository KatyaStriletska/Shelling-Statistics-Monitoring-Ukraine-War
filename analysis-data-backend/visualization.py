import pandas as pd
from collections import Counter
import plotly.graph_objects as go


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

    fig.show()
