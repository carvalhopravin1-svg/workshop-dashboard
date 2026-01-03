import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("🎰 Casino Technical Workshop Dashboard")

# Load Excel sheets
df_tasks = pd.read_excel("Inventory.xlsm", sheet_name="Tasks")
df_pat = pd.read_excel("Inventory.xlsm", sheet_name="PAT")
df_stock = pd.read_excel("Inventory.xlsm", sheet_name="Stock")
df_projects = pd.read_excel("Inventory.xlsm", sheet_name="Projects")
df_eos = pd.read_excel("Inventory.xlsm", sheet_name="EOS_Tasks")

df_pending = df_eos[df_eos["Status"] == "Pending"]

# Display sections
st.header("🔴 Urgent Machine Alerts")
st.warning("No current alerts. Update manually if needed.")

st.header("📋 Today's Tasks")
st.dataframe(df_tasks)

st.header("⚡ PAT Testing")
st.dataframe(df_pat)

st.header("📦 Stock Summary")
st.dataframe(df_stock)

st.header("🗓️ Upcoming Projects")
st.dataframe(df_projects)

st.header("📧 EOS Pending Tasks")
st.dataframe(df_pending)
