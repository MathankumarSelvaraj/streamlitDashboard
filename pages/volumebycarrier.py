import streamlit as st # app lib
import plotly.express as px #plots
import pandas as pd #data manipulation
import pygwalker as pyg #dataexploration
from pygwalker.api.streamlit import StreamlitRenderer
#from home import df,df_table, prepare_monthly_data , main
from home import AirExportVolumeDashboard
#page setting
st.set_page_config(page_title="Volume By Carrier", page_icon=":bar_chart:", layout="wide")

data_path = r"datasets\airExportVolume2023.csv"
dashboard = AirExportVolumeDashboard(data_path)

# Access the df variable
df = dashboard.df

grouped_data = df.groupby('Carrier legalName').agg({'_id': 'count', 'Considerable Charging Unit': 'sum'}).reset_index()
grouped_data.columns = ['Carrier legalName', 'Total Shipments', 'Volume']

st.dataframe(grouped_data.iloc[::1])


