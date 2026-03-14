import pandas as pd
import streamlit as st

st.set_page_config(page_icon ="",page_title="My first app",layout="centered")
st.title("My very first application !!!!!!")
st.header("Header")
st.subheader("subheader")
st.text("Text/Paragraph")

a=000
st.write(a)
# df=pd.read_csv("bankloan.csv")
# df
tab1,tab2,tab3=st.tabs(["Input Widgets","Other widget","columns"])


with tab1:
    st.subheader("Input Header")
    st.text_input("Name:",placeholder="enter your name")
    pwd=st.text_input("Password:",placeholder="enter your pass",type= "password")
    address=st.text_area("Address:",placeholder="enter your address")
    number=st.number_input("Age:",min_value=18,max_value=100)
with tab2:
    st.slider("select the age:",max_value=60,min_value=10,value=10)
    country=st.selectbox("select country",options=["India","China","Africa","USA","UK"])
    gender=st.radio("select the gender",options=["Male","Female","Others"],horizontal=True)
    page=st.pills("menu:",options=["Page1","Pagq2","Page3"],selection_mode="single")
    if page=="Page1":
        st.write("Page1 is selected")
    elif page=="Page2":
        st.write("you have selected page 2")
    else:
        st.write("Page3 is selected")

    page=st.segmented_control("Page:",options=["Home","Prediction","About","contact"])
    if st.button("click me"):
        st.text("maachine learning ")

    file=st.file_uploader("upload",type=["Excel","csv"])
    st.write("------")
with tab3:
    col1,col2=st.columns([2,2],border=2)
    col3,col4=st.columns([2,2],border=2)

    with col1:
        st.text_input("Name:",key="Name1")
        st.slider("age",key="Age1")
    with col2:
        st.pills("Country",options=[1,2,3],key="Country1")
        st.radio("Gender",options=["M","F","O"],key="Gen1")
    with col3:
        st.text_input("Name:",key="Name2")
        st.slider("age",key="Age2")
    with col4:
        st.pills("Country",options=[1,2,3],key="Country2")
        st.radio("Gender",options=["M","F","O"],key="Gen2")

with st.sidebar:
    st.title("my first app")
    st.slider("Age:",key=1)
    st.slider("Age:",key=2)