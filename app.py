import json
import pickle
from flask import Flask, request, jsonify,app,url_for,render_template
import numpy as np
import pandas as pd


app = Flask(__name__)
# Load the trained model
regmodel = pickle.load(open('regmodel.pkl', 'rb'))
# Load the feature scaler (ensure 'scaling.pkl' exists alongside 'model.pkl')
scaler = pickle.load(open('scaling.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data = scaler.transform(np.array(list(data.values())).reshape(1,-1))
    output = regmodel.predict(new_data)
    return jsonify(output[0])

if __name__ == "__main__":
    app.run(debug=True)
    