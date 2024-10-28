import json
import os
from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from map_data_processing import load_and_process_map_data
from map_visualization import shelling_map_visualization
from data_processing import load_and_process_data, get_data_of_weapon_by_year, get_categories_for_year, merge_two_data, get_category_of_weapon
from visualization import plot_total_launched_and_destroyed_per_year, chart_most_common_weapons_per_year, chart_most_common_category_per_year, plot_total_launched_and_destroyed_per_launch_place, plot_total_launched_and_destroyed_per_category_and_year

app = Flask(__name__)
CORS(app)  

df_massive_attacks = None
df_weapon_groupby_year = None
map_data = None


def initialize_data():
    global df_massive_attacks, df_weapon_groupby_year, map_data, df_weapon_group_by_category
    df_massive_attacks = load_and_process_data()
    df_megre = merge_two_data(df_massive_attacks)
    df_weapon_groupby_year = get_data_of_weapon_by_year(df_megre)
    df_weapon_group_by_category = get_category_of_weapon(df_megre)

@app.route('/graph1')
def get_graph1():
    year = request.args.get('year', default=2024, type=int)
    graph = plot_total_launched_and_destroyed_per_year(df_massive_attacks, year)
    return jsonify(json.loads(graph))

@app.route('/graph2')
def get_graph2():
    year = request.args.get('year', default=2024, type=int)
    category = request.args.get('category', default="UAV", type=str)
    graph = plot_total_launched_and_destroyed_per_category_and_year(year, category, df_weapon_groupby_year)
    return jsonify(json.loads(graph))

@app.route("/graph_launch_place")
def get_graph3():
    return jsonify(json.loads(plot_total_launched_and_destroyed_per_launch_place(df_massive_attacks)))
    
@app.route('/graph2/getCategories')
def get_categories():
    year = request.args.get('year', default=2024, type=int)
    categoriesForYear = get_categories_for_year(df_weapon_groupby_year, year)
    return jsonify(categoriesForYear)


@app.route('/chartModel')
def get_chart1():
    year = request.args.get('year', default=2024, type=int)
    graph = chart_most_common_weapons_per_year(df_massive_attacks, year)
    return jsonify(json.loads(graph))

@app.route('/chartCategory')
def get_chart2():
    year = request.args.get('year', default=2024, type=int)
    graph = chart_most_common_category_per_year(df_weapon_groupby_year, year)
    return jsonify(json.loads(graph))

@app.route('/weapon_table')
def get_weapon_table():
    res = df_weapon_group_by_category.to_dict(orient= 'records')
    return jsonify(res)

@app.route("/ukraine_map", methods=['GET'])
def get_ukraine_map():
    # data = load_and_process_map_data()
    ukraine_map = shelling_map_visualization(df_massive_attacks)
    map_file = os.path.join(os.getcwd(), "ukraine_shelling_map.html")
    ukraine_map.save(map_file)
    return send_file(map_file)


    
if __name__ == '__main__':
    initialize_data()
    app.run(debug=True)
