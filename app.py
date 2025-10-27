import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

st.title("Dashboard IBEX 35 📈")

# Diccionario de empresas del IBEX 35 con sus tickers de Yahoo Finance
ibex_tickers = {
    "IBEX 35 (Índice)": "^IBEX",
    "Banco Santander": "SAN.MC",
    "BBVA": "BBVA.MC",
    "Iberdrola": "IBE.MC",
    "Inditex": "ITX.MC",
    "CaixaBank": "CABK.MC",
    "Cellnex": "CLNX.MC",
    "Naturgy": "NTGY.MC",
    "Repsol": "REP.MC",
    "Ferrovial": "FER.MC",
    "Grifols": "GRF.MC",
    "Acciona": "ANA.MC",
    "Amadeus": "AMS.MC",
    "Aena": "AENA.MC",
    "Mapfre": "MAP.MC"
}

# Selector de empresa
empresa = st.selectbox("Selecciona una empresa del IBEX 35:", list(ibex_tickers.keys()))
ticker = ibex_tickers[empresa]

# Filtro de fechas
col1, col2 = st.columns(2)
with col1:
    fecha_inicio = st.date_input("Fecha de inicio", pd.to_datetime("2024-01-01"))
with col2:
    fecha_fin = st.date_input("Fecha de fin", pd.to_datetime("2024-10-27"))

# Descargar datos
if fecha_inicio < fecha_fin:
    datos = yf.download(ticker, start=fecha_inicio, end=fecha_fin)

    # Mostrar gráfico
    st.subheader(f"Precio de cierre: {empresa}")
    st.line_chart(datos["Close"])

    # Mostrar tabla
    st.write("Datos más recientes:")
    st.dataframe(datos.tail())
else:
    st.error("La fecha de inicio debe ser anterior a la fecha de fin.")
