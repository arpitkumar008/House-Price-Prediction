import pickle
import streamlit as st
import pandas as pd

#setup
st.set_page_config(page_icon="",page_title="house price prediction",layout="wide")


#load rf model
with open("RF_model.pkl","rb") as file:
    model=pickle.load(file)


#load datset 
df=pd.read_csv("cleaned_df.csv")


with st.sidebar:
    st.title("House price prediction app")
    
def get_encoded_loc(location):
    for loc,encoded in zip (df["location"],df["encoded_loc"]):
        if location==loc:
            return encoded

# input filed 
col1, col2 = st.columns(2)
with col1:
    location = st.selectbox("📍 Location", options=df["location"].unique())
    sqft = st.number_input("📐 Sqft", min_value=300)

with col2:
    bath = st.selectbox("🛁 No. of bathrooms", options=sorted(df["bath"].unique()))
    bhk = st.selectbox("🛏️ BHK", options=sorted(df["bhk"].unique()))

# encode location
encoded_loc = get_encoded_loc(location)

c1, c2, c3 = st.columns([2.2, 2, 1])

if c2.button("💰 Predict"):
    # prepare input data
    inp_data = [[sqft, bath, bhk,encoded_loc]]

    # prediction
    pred = model.predict(inp_data)
    pred=float(f"{pred[0]:.2f}")

    st.subheader(f"Predicted Price: Rs. {pred*100000}")