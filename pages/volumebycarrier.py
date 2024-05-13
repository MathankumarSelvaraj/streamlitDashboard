import streamlit as st # app lib
import plotly.express as px #plots
import pandas as pd #data manipulation
import pygwalker as pyg #dataexploration
from pygwalker.api.streamlit import StreamlitRenderer
from home import df,df_table, prepare_monthly_data , main

#page setting
st.set_page_config(page_title="Volume By Carrier", page_icon=":bar_chart:", layout="wide")

st.dataframe(df_table)