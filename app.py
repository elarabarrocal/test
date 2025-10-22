import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

st.title("Dashboard IBEX 35 📈")

# Cargar datos del IBEX 35
ibex = yf.download("^IBEX", start="2024-01-01")
st.line_chart(ibex["Close"])

st.write("Datos más recientes:")
st.dataframe(ibex.tail())
