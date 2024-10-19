from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  
app = Flask(__name__)

# Маршрут для головної сторінки
@app.route('/')
def members():
    return jsonify({"members": ["m", "m1", "m2"]})

if __name__ == '__main__':
    app.run(debug=True)
