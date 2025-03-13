import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Streamlit App Inside Docker 🚀")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())

    fig, ax = plt.subplots()
    df.hist(ax=ax)
    st.pyplot(fig)
