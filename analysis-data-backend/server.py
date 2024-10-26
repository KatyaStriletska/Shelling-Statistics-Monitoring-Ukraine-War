import json
import os
from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from map_data_processing import load_and_process_map_data
from map_visualization import shelling_map_visualization
from data_processing import load_and_process_data
from visualization import plot_total_launched_and_destroyed_per_year, chart_most_common_weapons_per_year

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

@app.route('/graph2')
def get_graph2():
    file_path = "data/missile_attacks_daily.csv"
    df_massive_attacks = load_and_process_data(file_path)
    year = request.args.get('year', default=2024, type=int)
    graph = chart_most_common_weapons_per_year(df_massive_attacks, year)
    return jsonify(json.loads(graph))

@app.route("/ukraine_map", methods=['GET'])
def get_ukraine_map():
    data = load_and_process_map_data()
    ukraine_map = shelling_map_visualization(data)
    map_file = os.path.join(os.getcwd(), "ukraine_shelling_map.html")
    ukraine_map.save(map_file)
    return send_file(map_file)

    
    
if __name__ == '__main__':
    app.run(debug=True)
