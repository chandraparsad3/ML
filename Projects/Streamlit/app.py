import streamlit as str
import pandas as pd

#This is title
str.title("This is just for streamlit Testing")

#This is simple text
str.write("This is simple text")

df=pd.DataFrame({
    'first': [1,2,3,4],
    'second':[7,8,9,10]
})

str.write("This is simple dataframe")
str.write(df)