
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.markdown('<style>body { background-color: #1e1e1e; color: white; }</style>', unsafe_allow_html=True)

# Load Excel data
excel_file = "Inventory_fixed.xlsx"

def load_sheet(sheet_name):
    try:
        return pd.read_excel(excel_file, sheet_name=sheet_name)
    except:
        return pd.DataFrame()

df_alerts = load_sheet("Tasks")
df_pat = load_sheet("PAT")
df_stock = load_sheet("Stock")
df_projects = load_sheet("Projects")

st.markdown("<h1 style='color:#f39c12;'>⚙️ WORKSHOP DASHBOARD</h1>", unsafe_allow_html=True)
st.markdown("### Electronic Gaming Operations")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 🔴 Urgent Machine Issues")
    if df_alerts.empty or 'Status' not in df_alerts:
        st.info("No alerts available.")
    else:
        urgent_issues = df_alerts[df_alerts["Status"].str.contains("urgent|tilt|bv full", case=False, na=False)]
        if not urgent_issues.empty:
            st.dataframe(urgent_issues[["Date", "Machine", "Issue", "Status"]])
        else:
            st.success("No current urgent machine issues.")

    st.markdown("### 🧪 PAT Testing Status")
    if df_pat.empty:
        st.info("No PAT data available.")
    else:
        percent_done = round(df_pat["Pass"].str.lower().eq("yes").mean() * 100)
        st.progress(percent_done / 100.0)
        st.write(f"**{percent_done}%** complete")
        st.dataframe(df_pat[["Equipment", "Type", "Location", "Date", "Pass", "Technician"]])

with col2:
    st.markdown("### 📋 Today's Tasks")
    if df_alerts.empty:
        st.info("No tasks available.")
    else:
        st.dataframe(df_alerts[["Date", "Technician", "Machine", "Issue", "Status"]])

    st.markdown("### 🗓️ Upcoming Projects")
    if df_projects.empty:
        st.info("No upcoming projects.")
    else:
        st.dataframe(df_projects[["Project Name", "Start Date", "End Date", "Lead Tech", "Status"]])

    st.markdown("### 📦 Stock Levels")
    if df_stock.empty:
        st.info("No stock data.")
    else:
        st.dataframe(df_stock[["Item", "Category", "Quantity", "Location", "Status"]])
