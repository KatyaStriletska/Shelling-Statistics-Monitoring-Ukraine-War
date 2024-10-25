import pandas as pd

def load_and_process_map_data() -> pd.DataFrame:
    url = "https://data.humdata.org/dataset/bb30eaae-306d-4d53-8978-998eb8b9a06e/resource/d4c483d4-e8dc-4246-9b6c-3aef8a7b16c6/download/conflict_data_ukr.csv"
    data = pd.read_csv(url, skiprows = [1])

    # Drop unnecessary columns
    unnecessary_columns = [col for col in data.columns if col not in ["latitude", "longitude", "year", "date_start", "date_end", "deaths_civilians", "source_headline", "source_date"]]
    data = data.drop(columns=unnecessary_columns)

    # Ensure latitude and longitude are numeric
    data['latitude'] = pd.to_numeric(data['latitude'], errors='coerce')
    data['longitude'] = pd.to_numeric(data['longitude'], errors='coerce')

    # Drop rows where latitude or longitude is 0 or missing
    data = data.dropna(subset=['latitude', 'longitude'])
    data = data[(data['latitude'] != 0) & (data['longitude'] != 0)]
    return data