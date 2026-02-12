import streamlit as st

st.title("WhatsApp Chat Analyzer (Minimal Test)")

uploaded_file = st.file_uploader("Upload WhatsApp Chat (.txt)", type="txt")

if uploaded_file:
    st.success("File uploaded! Streamlit is working.")