import streamlit as st # app lib
import plotly.express as px #plots
import pandas as pd #data manipulation

#page setting
st.set_page_config(page_title="AIR 7 SEAS Air Export Volume Dashboard", page_icon=":bar_chart:", layout="wide")

st.title("AIR 7 SEAS Air Export Volume Dashboard")
#reading data
df = pd.read_csv(r'D:/airExportVolumeDashboard/datasets/airExportVolume2023.csv')

#varibale defining

df['Crea'] = pd.to_datetime(df['Crea'])
distintYear = df['Crea'].dt.year.unique()
destinationCountry=df["Destination country"].unique()

#--SIDEBAR FOR FILTER
st.sidebar.header("Please Filter Here:")
dtCountry = st.sidebar.multiselect(
    "Select the country:",
    options=destinationCountry
)

year = st.sidebar.selectbox(
    "select the year:",
    options = distintYear
)

df_selection = df.query ("`Destination country` == @dtCountry")

groupbycounrty = pd.DataFrame(df.groupby("Destination country").sum("Considerable Charging Unit"))

countrydata = groupbycounrty.sort_values("Considerable Charging Unit",ascending=False)

#Scorecard
if len(dtCountry)>0:
    sumOfVolume= df_selection["Considerable Charging Unit"].sum()
else:
    sumOfVolume= df["Considerable Charging Unit"].sum()

#countrywise table

if len(dtCountry)>0:
    volumebycountry= countrydata
else:
    volumebycountry= countrydata.query("`Destination country` == @dtCountry")


#showing scorecard and countrytable
st.metric(label="Total Volume",value = sumOfVolume,delta=None)
st.dataframe(volumebycountry)