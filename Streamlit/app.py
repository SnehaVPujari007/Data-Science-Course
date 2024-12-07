import streamlit as st
import pandas as pd  
import numpy as np


## Title of the application

st.title("Hello StreamLit")

## Display a Simple Text
st.write("This is a Simple Text")

## Create a simple DataFrame

df = pd.DataFrame(
    {
        'first column' : [1,2,3,4] ,
        'second column' : [10,20,30,40]
    }
)

## Display the DataFrame

st.write("Here is the DataFrame")

st.write(df)


## Create a Line Chart

chart_data  = pd.DataFrame(
    np.random.randn(20,3) , columns = ['a','b','c']
)


st.line_chart(chart_data)

