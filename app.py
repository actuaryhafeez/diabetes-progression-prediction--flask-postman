import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle
from flask import Flask, request, jsonify

# Define a Flask app
app = Flask(__name__)

# Define a route to handle POST requests
@app.route('/predict_diabetes', methods=['POST'])
def predict_diabetes():
    # Get the input data from the request
    input_data = request.get_json()

    # Convert the input data into a NumPy array
    input_data = np.array([[input_data['AGE'], input_data['SEX'], input_data['BMI'],
                            input_data['BP'], input_data['S1'], input_data['S2'],
                            input_data['S3'], input_data['S4'], input_data['S5'], input_data['S6']]])

    # Load the saved model and make a prediction
    loaded_model = pickle.load(open('model/finalized_model.pkl', 'rb'))
    prediction = loaded_model.predict(input_data)

    # Return the prediction as JSON
    return jsonify({'prediction': prediction[0]})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
