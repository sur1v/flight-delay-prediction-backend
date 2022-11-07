import pickle5 as pickle
import numpy as np

from flask import Flask, request, jsonify, make_response

# Load model
file = open("pickle_model.pkl","rb")
model = pickle.load(file)
file.close()

# Prediction function
def predict_single(flight, model):
    y_pred = model.predict(flight)
    return y_pred[0]

app = Flask(__name__)

# Prediction route and method
@app.route('/predict', methods=['POST'])
def predict():
    flight_json = request.get_json()
    flight_data  = np.fromstring(flight_json['data'], dtype=int, sep=',').reshape(1, -1)

    prediction = predict_single(flight_data, model)

    # Result and veredict, according to model.pdf
    # clase '1' o 'Atraso', clase '0' o 'No Atraso'
    if prediction >= 1:
        result = {
            'delay': bool(prediction),
            'verdict': 'Atraso',
        }
    else:
        result = {
            'delay': bool(prediction),
            'verdict': 'No Atraso',
        }

    return make_response(jsonify(result), 200)

# Run at port 8000/TCP
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
