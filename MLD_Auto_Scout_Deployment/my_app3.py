# Streamlit Documentation: https://docs.streamlit.io/

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image  # to deal with images (PIL: Python imaging library)

df= pd.read_csv("Ready_to_ML.csv")
def main():
    st.title("Dictionary Data Input")

    # Initialize an empty dictionary
    my_dict = {}

    # Get user input for each key-value pair
    my_dict["type"] = st.selectbox("Type", ["Used", "New"])
    my_dict["power_kW"] = st.number_input("Power (kW)", min_value=0)
    my_dict["make_model"] = st.text_input("Make and Model", "")
    my_dict["engine_size"] = st.number_input("Engine Size", min_value=0)
    my_dict["mileage"] = st.number_input("Mileage", min_value=0)
    my_dict["age"] = st.number_input("Age", min_value=0)
    
    # Display the resulting dictionary
    st.write("Resulting Dictionary:", my_dict)

if __name__ == "__main__":
    main()


# To load machine learning model
import pickle
filename = "my_model"
model=pickle.load(open(r"C:\Users\halil\Desktop\samwolfnurhal/my_model", "rb"))


# Prediction with user inputs
predict = st.button("Predict")
result = model.predict(df)
if predict :
    st.success(result[0])



   
