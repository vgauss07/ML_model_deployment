# Import Libraries
import pandas as pd
import numpy as np
import sklearn
import joblib
import streamlit

model = open('linear_regression_model.pkl', "rb")
lr_model = joblib.load(model)

def lr_prediction(variable_1, variable_2, variable_3, variable_4, variable_5):
    pred_arr = np.array([variable_1, variable_2, variable_3, variable_4, variable_5])
    preds = pred_arr.reshape(1,-1)
    preds = preds.astype(int)
    model_prediction = lr_model.prediction(preds)
    return model_prediction

def run():
    streamlit.title("Assessment Prediction Model")
    html_temp = """
    
    """
    streamlit.markdown(html_temp)
    variable_1 = streamlit.text_input('Hours Studied')
    variable_2 = streamlit.text_input('Previous Scores')
    variable_3 = streamlit.text_input('Extracurricular Activities')
    variable_4 = streamlit.text_input('Sleep Hours')
    variable_5 = streamlit.text_input('Sample Question Papers Practiced')

    prediction = ""

    if streamlit.button("Predict"):
        prediction = lr_prediction(variable_1, variable_2, variable_3, 
                    variable_4, variable_5)
    streamlit.success(f'The prediction by model: {prediction}')

    if __name__ == '__main__':
        run()

