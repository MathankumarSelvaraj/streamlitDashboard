import streamlit as st # app lib
import plotly.express as px #plots
import pandas as pd #data manipulation
#import pygwalker as pyg #dataexploration
#from pygwalker.api.streamlit import StreamlitRenderer
#from home import df,df_table, prepare_monthly_data , main
from home import AirExportVolumeDashboard
#page setting
st.set_page_config(page_title="Volume By Carrier", page_icon=":bar_chart:", layout="wide")

data_path = r"datasets\airExportVolume2023.csv"
dashboard = AirExportVolumeDashboard(data_path)

# Access the df variable
df = dashboard.df
df["route"] = df["Origin Port"]+" - "+ df["Destination Port"]
grouped_data = df.groupby("route").agg({"Shipment#":"count","Considerable Charging Unit":"sum"}).reset_index


airline = df["Carrier legalName"].unique()

with st.expander(label="Select a Airline"):
    st.text_input(label="Filter")
    with st.container(height=len(airline)):
        for air in airline:
            st.checkbox(label=f"{air}")

grouped_data.columns = ['Route', 'Total Shipments', 'Volume In Kgs']




col1,col2 = st.columns(2)

with col1:
    st.dataframe(grouped_data.sort_values('Volume In Kgs', ascending=False))
#with col2:

