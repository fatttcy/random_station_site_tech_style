from flask import Flask, render_template, jsonify
import pandas as pd
import random

app = Flask(__name__)

stations_df = pd.read_csv('stations.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random_station')
def random_station():
    station = stations_df.sample(1).iloc[0]
    return jsonify({
        'station_name': station['station_name'],
        'city': station['city'],
        'address': station['address']
    })

if __name__ == '__main__':
    app.run(debug=True)