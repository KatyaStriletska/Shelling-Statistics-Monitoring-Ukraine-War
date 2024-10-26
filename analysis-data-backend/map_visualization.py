import pandas as pd
import folium
from folium.plugins import HeatMap

def shelling_map_visualization(data: pd.DataFrame) -> folium.Map:
    ukraine_map = folium.Map(location=[48.3794, 31.1656], zoom_start=6)

    # Add a marker for each shelling incident
    for _, row in data.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"Date: {row['source_date']}<br>",
            icon=folium.Icon(color='red', icon='fire')
        ).add_to(ukraine_map)

    # Optional: Add heatmap layer for shelling intensity visualization
    heat_data = [[row['latitude'], row['longitude']] for _, row in data.iterrows()]
    HeatMap(heat_data, radius=8, max_zoom=13).add_to(ukraine_map)

    # Save the map as an HTML file
    # ukraine_map.save("ukraine_shelling_map.html")
    
    return ukraine_map