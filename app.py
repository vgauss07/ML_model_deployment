# Import Libraries
import pandas as pd
import numpy as np
import sklearn
import joblib
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')

def home():
    return render_template('home.html')

@app.route('/predict',methods=['GET', 'POST'])


def predict():
    if request.method == 'POST':
        print(request.form.get('variable'))
        try:
            variable_1 = float(request.form['Hours Studied'])
            variable_2 = float(request.form['Previous Scores'])
            variable_3 = float(request.form['Extracurricular Activities'])
            variable_4 = float(request.form['Sleep Hours'])
            variable_5 = float(request.form['Sample Question Papers Practiced'])
            pred_args =  [variable_1, variable_2, variable_3, variable_4, variable_5]
            pred_arr = np.array(pred_args)
            preds = pred_arr.reshape(1,-1)
            model = open("linear_regression_model.pkl", "rb")
            lr_model = joblib.load(model)
            model_prediction = lr_model.predict(preds)
            model_prediction = round(float(model_prediction),2)
        except ValueError:
            return "Please enter valid values"
    return render_template('predict.html', prediction=model_prediction)

    if __name__ == '__main__':
        app.run(host='0.0.0.0')
