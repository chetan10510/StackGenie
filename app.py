import streamlit as st
import pandas as pd
from google.cloud import bigquery

# ---- STREAMLIT APP ----
st.set_page_config(page_title="Release Notes Dashboard", layout="wide")
st.title("Google Cloud Release Notes Dashboard")

# ---- CONNECT TO BIGQUERY ----
# Make sure your service account JSON file is in the project folder
client = bigquery.Client.from_service_account_json("D:/ACADEMICS/AI-ML/StackGenie/gcp/resolute-future-470007-a4-8f1239adae36.json")



# ---- QUERY DATA ----
query = """
SELECT
  published_at AS timestamp,
  description AS message,
  release_note_type AS log_level,
  product_name,
  product_version_name
FROM
  `bigquery-public-data.google_cloud_release_notes.release_notes`
ORDER BY
  published_at DESC
LIMIT 100
"""
df = client.query(query).to_dataframe()

# ---- FILTERS ----
products = df['product_name'].unique()
selected_product = st.selectbox("Select Product", products)
filtered_df = df[df['product_name'] == selected_product]

st.subheader(f"Release Notes for {selected_product}")
st.dataframe(filtered_df)

# ---- CHARTS ----
st.subheader("Release Note Type Distribution")
st.bar_chart(filtered_df['log_level'].value_counts())
