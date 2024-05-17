import streamlit as st
import plotly.express as px
import pandas as pd
from streamlit_option_menu import option_menu
from numerize.numerize import numerize
import time
from streamlit_extras.metric_cards import style_metric_cards
st.set_option('deprecation.showPyplotGlobalUse', False)
import plotly.graph_objs as go
from streamlit_dynamic_filters import DynamicFilters
import datetime



st.set_page_config(page_title=" Air Volume Dashboard", page_icon=":bar_chart:", layout="wide")
st.header("Volume By Month")

df = pd.read_csv(r'D:\Dashboard\Steamlitworks\airExportVolumeDashboard\datasets\airExportVolume2023.csv')
df['createdDate'] = pd.to_datetime(df['createdDate'])
df['year'] =df["createdDate"].dt.year
df['month'] = df['createdDate'].dt.month
df= df.query('year != 2020')

#filters
#  #Year Filter
# Year = st.sidebar.selectbox (
#             "select the year:",
#             options =df['year'].unique(),
#             #default=df['year'].unique()
#         )
# airline = st.sidebar.multiselect(
#     "Select the Airline",
#     options = df['Carrier legalName'].unique()
    
#     )
# hhg= st.sidebar.selectbox("HouseHold Goods (Yes only)", df['isHouseholdGoods'].unique())


# if not Year and not airline and not hhg:
#     # Show all data if no filters are selected
#     df_selection = df
# else:
#     # Apply selected filters
#     df_selection = df
#     if Year:
#         df_selection = df_selection[df_selection['year'].isin(Year)]
#     if airline:
#         df_selection = df_selection[df_selection['Carrier legalName'].isin(airline)]
#     if hhg:
#         df_selection = df_selection[df_selection['isHouseholdGoods'] == hhg]


# dynamic_filters = DynamicFilters(df=df, filters=['year', 'Carrier legalName', 'isHouseholdGoods'])

# dynamic_filters.display_filters(location='sidebar')
# dynamic_filters.display_df()
# filter_df(except_filter='Item')

#st.dataframe(df_selection)



# Assuming you have your DataFrame named 'df'

import streamlit as st
import pandas as pd

# Sample data
# data = {'Category': ['A', 'A', 'B', 'B', 'C', 'C', 'C', 'D', 'D', 'D', 'D'],
#         'Color': ['red', 'blue', 'blue', 'black', 'black', 'green', 'blue', 'yellow', 'white', 'green', 'purple'],
#         'Value': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]}
# df = pd.DataFrame(data)

# Initialize filters in session state (if not already set)
# if 'selected_year' not in st.session_state:
#     st.session_state['selected_year'] = None
# if 'selected_airline' not in st.session_state:
#     st.session_state['selected_airline'] = None

# # Sidebar for filters
# with st.sidebar:
#     year_filter = st.selectbox('Year Filter', df['year'].unique(), key='year_filter')
#     airline_filter = st.selectbox('Airline Filter', df['Carrier legalName'].unique(), key='airline_filter')

#     # Update session state based on filter selections
#     st.session_state['selected_year'] = year_filter
#     st.session_state['selected_airline'] = airline_filter

# # Filter the DataFrame based on session state values
# filtered_df = df.copy()
# if st.session_state['selected_year'] is not None:
#     filtered_df = filtered_df[filtered_df['year'] == st.session_state['selected_year']]
# if st.session_state['selected_airline'] is not None:
#     filtered_df = filtered_df[filtered_df['Carrier legalName'] == st.session_state['selected_airline']]

# # Display the filtered DataFrame
# st.write(filtered_df)

if 'edited_df' not in st.session_state:
    dynamic_filters = DynamicFilters(df, filters=['Year', 'Carrier legalName'], filters_name='my_filters')
else:
    dynamic_filters = DynamicFilters(st.session_state['edited_df'], filters=['Year', 'Carrier legalName'], filters_name='my_filters')


dynamic_filters.display_filters(location='columns', num_columns=2)

# filtered df
new_df = dynamic_filters.filter_df()

st.session_state['edited_df'] = st.data_editor(new_df, num_rows='dynamic', key='my_key', hide_index=False, use_container_width=True)
