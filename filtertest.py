import streamlit as st
import pandas as pd

df = pd.read_csv(r'D:\Dashboard\Steamlitworks\airExportVolumeDashboard\datasets\airExportVolume2023.csv')
df['createdDate'] = pd.to_datetime(df['createdDate'])
df['year'] =df["createdDate"].dt.year
df['month'] = df['createdDate'].dt.month
df= df.query('year != 2020')

import streamlit as st
import pandas as pd


# Assuming you have your DataFrame named 'df'

# Extract unique options for filters
year_options = df['year'].unique()
airline_options = df['Carrier legalName'].unique()
hhg_options = df['isHouseholdGoods'].unique()

# Filter selections with initial values (all selected)
year_selected = year_options.copy()  # Copy to avoid modifying original list
airline_selected = airline_options.copy()
hhg_selected = hhg_options[0]  # Default to 'Yes' (assuming first option is 'Yes')

# Sidebar multiselects for filters with checkbox for HHG
year_selected = st.sidebar.multiselect(
    "Select the year:", year_options, default=year_selected
)
airline_selected = st.sidebar.multiselect(
    "Select the Airline", airline_options
)
hhg_selected = st.sidebar.checkbox("HouseHold Goods (Yes only)", hhg_selected)

# Filter logic directly within Streamlit elements
# if len(year_selected) == len(year_options) and len(airline_selected) == len(airline_options) and not hhg_selected:
#     # No filters applied, show all data
#     df_selection = df.copy()
# elif len(year_selected) == 1 and len(airline_selected) == len(airline_options) and not hhg_selected:
#     # Only year filter applied
#     df_selection = df[df['year'].isin(year_selected)]
# else:
#     # Apply all selected filters, including HHG check
#     conditions = []
#     if len(year_selected) < len(year_options):
#         conditions.append(df['year'].isin(year_selected))
#     if len(airline_selected) < len(airline_options):
#         conditions.append(df['Carrier legalName'].isin(airline_selected))
#     if hhg_selected:
#         conditions.append(df['isHouseholdGoods'] == 'Yes')
#     df_selection = df.query(" & ".join(conditions))

# Display DataFrame
#st.dataframe(df_selection)
