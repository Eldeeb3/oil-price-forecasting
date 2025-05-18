import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

st.set_page_config(page_title="Oil Price Forecasting", layout="wide")

st.title("Oil Price Forecaster")
st.write("Forecasting crude oil prices using Facebook Prophet")

# Load data — skip the first 4 metadata rows
df_raw = pd.read_csv("data/oil_prices.csv", skiprows=4)

# Rename columns safely
df_raw.columns = ['ds', 'y']

# Drop any rows with missing values
df_raw = df_raw.dropna()

# Convert types
df_raw['ds'] = pd.to_datetime(df_raw['ds'], errors='coerce')
df_raw['y'] = pd.to_numeric(df_raw['y'], errors='coerce')

# Drop any rows that failed to convert
df = df_raw.dropna()

# Show raw data
st.subheader("Historical Oil Prices")
st.dataframe(df.tail())

# Plot historical prices
st.line_chart(df.set_index('ds')['y'])

# Prophet Forecasting
st.subheader("30-Day Forecast")
model = Prophet()
model.fit(df)

future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

# Plot forecast
fig1 = model.plot(forecast)
st.pyplot(fig1)

# Optional: Forecast components
st.subheader("Forecast Components")
fig2 = model.plot_components(forecast)
st.pyplot(fig2)