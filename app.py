import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
from wordcloud import WordCloud

st.title("WhatsApp Chat Analytics Dashboard")
st.write("Welcome to the dashboard 🚀")

uploaded_file = st.file_uploader("Upload WhatsApp Chat (.txt)", type="txt")

if uploaded_file:
    st.success("File uploaded! Streamlit is working.")
