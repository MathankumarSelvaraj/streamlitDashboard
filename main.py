import streamlit as st # app lib
import plotly.express as px #plots
import pandas as pd #data manipulation

#page setting
st.set_page_config(page_title="AIR 7 SEAS Air Export Volume Dashboard", page_icon=":bar_chart:", layout="wide")

st.title("AIR 7 SEAS Air Export Volume Dashboard")
#reading data
df = pd.read_csv(r'D:/airExportVolumeDashboard/datasets/airExportVolume2023.csv')

#varibale defining
sumOfVolume= df["Considerable Charging Unit"].sum()
df['Crea'] = pd.to_datetime(df['Crea'])
distintYear = df['Crea'].dt.year.unique()
destinationCountry=df["Destination country"].unique()

#--SIDEBAR FOR FILTER
st.sidebar.header("Please Filter Here:")
destinationCountry = st.sidebar.multiselect(
    "Select the country:",
    options=destinationCountry
)

year = st.sidebar.selectbox(
    "select the year:",
    options = distintYear
)

#df_selection = df.query ("destinationCountry == @destinationCountry & year == @year")

st.metric(label="Total Volume",value =sumOfVolume,delta=None)