from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from data_processing import load_and_process_data
from visualization import plot_total_launched_and_destroyed_per_year

app = Flask(__name__)
CORS(app)  

@app.route('/')
def members():
    file_path = "data/missile_attacks_daily.csv"
    df_massive_attacks = load_and_process_data(file_path)
    year = request.args.get('year', default=2024, type=int)

    graph = plot_total_launched_and_destroyed_per_year(df_massive_attacks, year)
    return jsonify(json.loads(graph))

@app.route('/graph1')
def get_graph1():
    file_path = "data/missile_attacks_daily.csv"
    df_massive_attacks = load_and_process_data(file_path)
    year = request.args.get('year', default=2024, type=int)

    graph = plot_total_launched_and_destroyed_per_year(df_massive_attacks, year)
    return jsonify(json.loads(graph))


if __name__ == '__main__':
    app.run(debug=True)
