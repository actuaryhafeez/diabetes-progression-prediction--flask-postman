# diabetes-progression-prediction--flask-postman
Diabetes Progression Prediction using Machine Learning, Flask and Postman

# Description: 
This project uses a dataset of medical records to predict the progression of diabetes based on a person's age, sex, body mass index, blood pressure, and blood readings. The dataset has been sourced from the work of Bradley Efron, Trevor Hastie, Iain Johnstone, and Robert Tibshirani in their paper "Least Angle Regression". The machine learning model has been built using scikit-learn library in Python and has been deployed as a web app using Flask.


# Machine Learning Model
The linear regression model was built using Python and the scikit-learn library. The model was trained on the data set and saved to disk using the pickle module.

# Flask App
The model is served using a Flask app that listens for POST requests at the /predict_diabetes endpoint. When the app receives a request, it uses the saved model to make a prediction based on the input data and returns the prediction as a JSON object.

# Postman
You can test the Flask app by sending a POST request to the /predict_diabetes endpoint using Postman. The request should contain the input data as a JSON object.

# Files
* diabetes.csv: The data set used to train the machine learning model.
* notebook.ipynb: A Jupyter Notebook that contains the code used to train the machine learning model.
* app.py: The Flask app that serves the machine learning model.
* finalized_model.pkl: The saved machine learning model.
* README.md: This file.

# How to Use
## To install and run this application, follow these steps:

### Clone the repository to your local machine.
    https://github.com/actuaryhafeez/diabetes-progression-prediction--flask-postman.git
### Create a new virtual environment in the project directory.
    python3 -m venv venv
### Activate the virtual environment. 
    source venv/bin/activate
### Jupyter Notebook has also been installed in the virtual environment. Install the necessary dependencies by running the command
    pip install -r requirements.txt.
### Run Jupyter Notebook using the following command to open notebook.ipynb
    jupyter notebook
### Start the Flask server by running the command python app.py in the terminal.
    flask run
### Send a POST request to http://localhost:5000/predict_diabetes using Postman, with the input data as a JSON object. Data is preprocessed. 

    {
        "Age": 0.038076,
        "Sex": 0.050680,
        "BMI": 0.061696,
        "BP": 0.021872,
        "S1": -0.044223,
        "S2": -0.034821,
        "S3": -0.043401,
        "S4": -0.002592
        "S5": 0.019908,
        "S6": -0.017646
    }
    
 ### Postman Request 
 ![postman](https://user-images.githubusercontent.com/55107467/233799799-d45b90b2-da63-4542-9d68-d4abc269b9e4.png)


## Project Structure 

    diabetes-progression-prediction--flask-postman/
        ├── data/
        |   └── diabetes.csv
        │   
        ├── model/
        │   └── finalized_model.pkl
        ├── app.py/
        │  
        ├── notebook.ipynb/
        ├── requirements.txt/
        ├── README.md/

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

This project adheres to the [Open Source Initiative's](https://opensource.org) definition of open source software and the [Open Source Initiative's Approved License List](https://opensource.org/licenses/alphabetical).


# References

Diabetes Data Set: https://www4.stat.ncsu.edu/~boos/var.select/diabetes.tab.txt

Flask: https://flask.palletsprojects.com/

scikit-learn: https://scikit-learn.org/

pickle: https://docs.python.org/3/library/pickle.html
