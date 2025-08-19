import streamlit as st
import pandas as pd

df = pd.read_csv("fraud_logs_2.csv")

st.title("Fraud Detection Dashboard")
st.dataframe(df)

fraud_count = df[df["prediction"] == 1].shape[0]
total = df.shape[0]

st.metric("Total Transactions", total)
st.metric("Fraudulent Transactions", fraud_count)
