import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Use st.cache_data for caching data
@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names

# Load the data
df, target_names = load_data()

# Train the model
model = RandomForestClassifier()
model.fit(df.iloc[:, :-1], df['species'])

# Sidebar inputs for user features
st.sidebar.title("Input Features")
sepal_length = st.sidebar.slider(
    "Sepal Length (cm)", 
    float(df[df.columns[0]].min()), 
    float(df[df.columns[0]].max())
)
sepal_width = st.sidebar.slider(
    "Sepal Width (cm)", 
    float(df[df.columns[1]].min()), 
    float(df[df.columns[1]].max())
)
petal_length = st.sidebar.slider(
    "Petal Length (cm)", 
    float(df[df.columns[2]].min()), 
    float(df[df.columns[2]].max())
)
petal_width = st.sidebar.slider(
    "Petal Width (cm)", 
    float(df[df.columns[3]].min()), 
    float(df[df.columns[3]].max())
)

# Prepare input data
input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

# Make prediction
prediction = model.predict(input_data)
predicted_species = target_names[prediction[0]]

# Display the result
st.write("Prediction")
st.write(f"The predicted species is: {predicted_species}")


