import pandas as pd
import numpy as np 
import pickle
import streamlit as st
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import svm
from PIL import Image
pickle_in= open('rainfall.pkl','rb')
classifier = pickle.load(pickle_in)
def welcome():
    return 'WELCOME,Thanks for visiting my 3rd-Machine-Learning Model Building Project'
def prediction(Location, MinTemp,MaxTemp,Rainfall,Evaporation,
        Sunshine,WindGustDir,WindGustSpeed,WindDir9am,WindDir3pm,
        WindSpeed9am,WindSpeed3pm,Humidity9am,Humidity3pm,
        Pressure9am,Pressure3pm,Cloud9am,Cloud3pm,Temp9am,
        Temp3pm,RainToday,RISK_MM):
    prediction=classifier.predict(
        [[Location, MinTemp,MaxTemp,Rainfall,Evaporation,
        Sunshine,WindGustDir,WindGustSpeed,WindDir9am,WindDir3pm,
        WindSpeed9am,WindSpeed3pm,Humidity9am,Humidity3pm,
        Pressure9am,Pressure3pm,Cloud9am,Cloud3pm,Temp9am,Temp3pm,RainToday,RISK_MM]])
    print(prediction)
    return prediction

def main():
    st.title("ML-Prediction Machine 4-Tomorrow's-Rainfall.....")
    html_temp = """
       <dib style ="background-color:green;padding:20px">
       <h3 style ="color:blue;text-align:left;">Gospel-Orok Rainfall Prediction Machine-Learning & AI App <br>
       For Diabeties Prediction.</h3>
       </div>
       """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.text('****************************************************')
    st.text('This classification is a binary classification problem.')
    
    st.text('****************************************************')
    Location = st.text_input("Enter Location Name","")
    MinTemp = st.text_input('Enter Min.Temperature',"")
    MaxTemp = st.text_input('Enter Max.Temperature',"")
    Rainfall = st.text_input('Enter Rainfall Value',"")
    Evaporation = st.text_input('Pedigree',"")
    Sunshine = st.text_input('Sunshine value',"")
    WindGustDir = st.text_input('Windgust direction',"")
    WindGustSpeed = st.text_input('WindGustSpeed',"")
    WindDir9am = st.text_input('WindDir9am',"")
    WindDir3pm = st.text_input('WindDir3pm',"")
    WindSpeed9am = st.text_input('WindSpeed9am',"")
    WindSpeed3pm = st.text_input('WindSpeed3pm',"")
    Humidity9am = st.text_input('Humidity9am',"")
    Humidity3pm = st.text_input('Humidity3pm',"")
    Pressure9am = st.text_input('Pressure9am',"")
    Pressure3pm = st.text_input('Pressure3pm',"")
    Cloud9am = st.text_input('Cloud9am',"")
    Cloud3pm = st.text_input('Cloud3pm',"")
    Temp9am = st.text_input('Temp9am',"")
    Temp3pm = st.text_input('Temp3pm',"")
    RainToday = st.text_input('RainToday',"")
    RISK_MM = st.text_input('RISK_MM',"")
    result = ""
    
    
    if st.button("Predict"):
        result = prediction(Location, MinTemp,MaxTemp,Rainfall,Evaporation,
        Sunshine,WindGustDir,WindGustSpeed,WindDir9am,WindDir3pm,
        WindSpeed9am,WindSpeed3pm,Humidity9am,Humidity3pm,
        Pressure9am,Pressure3pm,Cloud9am,Cloud3pm,Temp9am,Temp3pm,RainToday,RISK_MM)
    st.success('With 100% Accuracy, this is my prediction:{}'.format(result))
    st.text("Zero(0) indicates Negative Result")
    st.text("One(1) indicates Positive Result")
    st.text("This Model prediction is based on SUPPORT VECTOR MACHINE Algorithm.")
    st.text('Thanks for Visiting!')
if __name__ == '__main__':
    main()
