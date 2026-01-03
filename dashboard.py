
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.markdown('''
    <style>
    body { background-color: #121212; color: white; }
    .card {
        padding: 20px; margin-bottom: 20px; border-radius: 10px;
        background-color: #1e1e1e; border: 1px solid #333;
    }
    .section-title {
        font-size: 26px; color: #f39c12; margin-bottom: 10px;
    }
    .icon {
        font-size: 28px; margin-right: 10px;
    }
    </style>
''', unsafe_allow_html=True)

def load_excel_data(sheet_name):
    try:
        return pd.read_excel("Inventory_fixed.xlsx", sheet_name=sheet_name)
    except Exception as e:
        return pd.DataFrame()

df_alerts = load_excel_data("Tasks")
df_pat = load_excel_data("PAT")
df_stock = load_excel_data("Stock")
df_projects = load_excel_data("Projects")

st.markdown("<h1 style='color:#f39c12;'>🎰 Casino Technical Workshop Dashboard</h1>", unsafe_allow_html=True)

# Top grid: Urgent Alerts & Today's Tasks
col1, col2 = st.columns(2)
with col1:
    st.markdown("<div class='card'><div class='section-title'>🔴 Urgent Machine Alerts</div>", unsafe_allow_html=True)
    if not df_alerts.empty and 'Status' in df_alerts:
        urgent = df_alerts[df_alerts["Status"].str.contains("urgent|tilt|bv full", case=False, na=False)]
        if not urgent.empty:
            st.dataframe(urgent[["Date", "Machine", "Issue", "Status"]])
        else:
            st.success("No urgent issues.")
    else:
        st.info("No alerts found.")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'><div class='section-title'>📋 Today's Tasks</div>", unsafe_allow_html=True)
    if not df_alerts.empty:
        st.dataframe(df_alerts[["Date", "Technician", "Machine", "Issue", "Status"]])
    else:
        st.info("No tasks available.")
    st.markdown("</div>", unsafe_allow_html=True)

# PAT Testing Section
st.markdown("<div class='card'><div class='section-title'>🧪 PAT Testing</div>", unsafe_allow_html=True)
if not df_pat.empty:
    percent_done = round(df_pat["Pass"].str.lower().eq("yes").mean() * 100)
    st.progress(percent_done / 100.0)
    st.write(f"**{percent_done}% complete**")
    st.dataframe(df_pat[["Equipment", "Type", "Location", "Date", "Pass", "Technician"]])
else:
    st.info("No PAT testing data found.")
st.markdown("</div>", unsafe_allow_html=True)

# Stock Summary
st.markdown("<div class='card'><div class='section-title'>📦 Stock Summary</div>", unsafe_allow_html=True)
if not df_stock.empty:
    st.dataframe(df_stock[["Item", "Category", "Quantity", "Location", "Status"]])
else:
    st.info("No stock data available.")
st.markdown("</div>", unsafe_allow_html=True)

# Projects
st.markdown("<div class='card'><div class='section-title'>📅 Upcoming Projects</div>", unsafe_allow_html=True)
if not df_projects.empty:
    st.dataframe(df_projects[["Project Name", "Start Date", "End Date", "Lead Tech", "Status"]])
else:
    st.info("No project data found.")
st.markdown("</div>", unsafe_allow_html=True)
