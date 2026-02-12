import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("WhatsApp Chat Analytics Dashboard")

st.write("Welcome to the dashboard 🚀")


st.title("WhatsApp Chat Analyzer (Minimal Test)")

uploaded_file = st.file_uploader("Upload WhatsApp Chat (.txt)", type="txt")

if uploaded_file:
    st.success("File uploaded! Streamlit is working.")
