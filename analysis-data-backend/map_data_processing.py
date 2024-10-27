import pandas as pd

def load_and_process_map_data() -> pd.DataFrame:
    url = "https://data.humdata.org/dataset/bb30eaae-306d-4d53-8978-998eb8b9a06e/resource/d4c483d4-e8dc-4246-9b6c-3aef8a7b16c6/download/conflict_data_ukr.csv"
    data = pd.read_csv(url, skiprows=[1])

    necessary_columns = {
        "#geo+lat": "latitude",
        "#geo+lon": "longitude",
        "#date+year": "year",
        "#date+start": "date_start",
        "#date+end": "date_end",
        "#affected+killed": "deaths_civilians",
        "#meta+source": "source_headline",
        "#date+end": "source_date"
    }
    data = data[data.get("where_prec") != 6]
    data = data.rename(columns=necessary_columns)
    data = data[list(necessary_columns.values())]

    data['latitude'] = pd.to_numeric(data['latitude'], errors='coerce')
    data['longitude'] = pd.to_numeric(data['longitude'], errors='coerce')
    data = data.dropna(subset=['latitude', 'longitude'])
    data = data[(data['latitude'] != 0) & (data['longitude'] != 0)]

    data['date_start'] = pd.to_datetime(data['date_start'], errors='coerce')
    data = data[(data['date_start'] >= '2022-02-24')]

    return data