import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
from collections import Counter

launch_place_categories = None
model_categories = None

def preprocessing_for_prediction(df: pd.DataFrame) -> pd.DataFrame:
    global launch_place_categories, model_categories
    data = df.filter(['year', 'model', 'launch_place', 'launched', 'destroyed'])
    data.dropna(subset=['launched'], inplace=True)
    model_counts = Counter(data['model'])
    top_models = [model for model, _ in model_counts.most_common(5)]
    data = data[data['model'].isin(top_models)]

    categorical_values = ["model", "launch_place"]

    for val in categorical_values:
        data[val] = data[val].astype('category')
    
    launch_place_categories = data['launch_place'].cat.categories.to_list()    
    model_categories = data['model'].cat.categories

    cat_columns = data.select_dtypes(['category']).columns
    data[cat_columns] = data[cat_columns].apply(lambda x: x.cat.codes)
    
    return data

def get_launch_place_categories():
    return launch_place_categories
    
    
def training_model_for_type(data: pd.DataFrame):
    X_type = data[['year', 'launch_place', 'launched']]
    y_type = data['model']

    X_train_type, X_test_type, y_train_type, y_test_type = train_test_split(X_type, y_type, test_size=0.2, random_state=64)

    rf_model = RandomForestClassifier(n_estimators=70, random_state=42)
    rf_model.fit(X_train_type, y_train_type)

    joblib.dump(rf_model, 'data/rf_model.pkl')

def training_model_for_propability(data: pd.DataFrame):
    X_prob = data[['year', 'launch_place', 'launched']]
    y_prob = data['destroyed'] > 0
  
    X_train, X_test, y_train, y_test = train_test_split(X_prob, y_prob, test_size=0.2, random_state=42)

    rf = RandomForestClassifier(n_estimators=100)
    rf.fit(X_train, y_train)

    joblib.dump(rf, 'data/rf_model_prob.pkl')

   
def perform_prediction_for_model(year: int, launch_place: str, launched:int):
  rf_model = joblib.load('data/rf_model.pkl')
  new_data = pd.DataFrame({
      'year': [year],
      'launch_place': [launch_place],
      'launched': [launched]
  })
  launch_place_code = pd.Series(launch_place_categories).searchsorted(launch_place)
  new_data['launch_place'] = launch_place_code
  model_code = rf_model.predict(new_data)
  if model_code < len(model_categories):
    decoded_value = model_categories[model_code]
  else:
    decoded_value = None
  return decoded_value[0]


def perform_probability_prediction(year: int, launch_place: str, launched: int):
    rf_model = joblib.load('data/rf_model_prob.pkl')
    
    new_data = pd.DataFrame({
        'year': [year],
        'launch_place': [launch_place],
        'launched': [launched]
    })
    launch_place_code = pd.Series(launch_place_categories).searchsorted(launch_place)
    new_data['launch_place'] = launch_place_code

    probabilities = rf_model.predict_proba(new_data)
    
    return probabilities[0][1]