import pandas as pd
import folium
from folium.plugins import HeatMap, TimestampedGeoJson
import json
from datetime import datetime

def shelling_map_visualization(data: pd.DataFrame) -> folium.Map:
    ukraine_map = folium.Map(location=[48.3794, 31.1656], zoom_start=6)

    features = []
    for _, row in data.iterrows():
        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [row['longitude'], row['latitude']]
            },
            'properties': {
                'time': row['date_start'].strftime('%Y-%m-%d'),
                'popup': f"Date: {row['date_start']}<br>Deaths of civilians: {row['deaths_civilians']}<br>{row['source_headline']}",
                "icon": "circle",
                "iconstyle": {
                    "fillColor": "red",
                    "fillOpacity": 0.6,
                    "stroke": "false",
                    "radius": 15,
                },
                "style": {"weight": 0}
            }
        }
        features.append(feature)

    # Create TimestampedGeoJson
    timestamped_geojson = TimestampedGeoJson(
        {
            'type': 'FeatureCollection',
            'features': features,
        },
        period='P1D',
        duration='P1D',
        add_last_point=False,
        auto_play=False,
        loop=False,
        max_speed=1,
        loop_button=True,
        date_options='YYYY-MM-DD',
        time_slider_drag_update=True
    )

    timestamped_geojson.add_to(ukraine_map)

    # Save the map as an HTML file
    #ukraine_map.save("ukraine_shelling_map.html")

    return ukraine_map