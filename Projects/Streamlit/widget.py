import streamlit as str

str.title("Using widgets from Streamlit")

name=str.text_input("Please Enter your Name")

if name:
    str.write(f"Hello, {name}")

age=str.slider("Choose your age",0,100,17)
str.write(f"Your age is {age}")

options=['Python','Java','C','C++','Javascript','PHP','Swift','C#']
selected=str.selectbox("Please Choose Your Options ", options)

str.write(f"Selected options are {selected}")