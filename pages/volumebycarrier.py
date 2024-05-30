import streamlit as st # app lib
import plotly.express as px #plots
import pandas as pd #data manipulation
#import pygwalker as pyg #dataexploration
#from pygwalker.api.streamlit import StreamlitRenderer
#from home import df,df_table, prepare_monthly_data , main
from home import AirExportVolumeDashboard
#page setting
#st.set_page_config(page_title="Volume By Carrier", page_icon=":bar_chart:", layout="wide")

data_path = r"datasets/airExportVolume2023.csv"
dashboard = AirExportVolumeDashboard(data_path)

# Access the df variable
df = dashboard.df
col1, col2 = st.columns(2)
import streamlit as st

# Sample list of airlines
airlines = df["Carrier legalName"].dropna().unique()

# Initialize session state for checkbox states if not already done
if 'checkbox_states' not in st.session_state:
    st.session_state.checkbox_states = {air: False for air in airlines}

# Function to filter airlines based on the search query
def filter_airlines(query, airlines):
    return [air for air in airlines if query.lower() in air.lower()]

# with st.expander(label="Select an Airline"):
#     # Text input for filtering
#     query = st.text_input(label="Filter")
    
#     # Filter the list of airlines based on the query
#     filtered_airlines = filter_airlines(query, airlines)
    
#     # Display checkboxes for the filtered airlines
#     for air in filtered_airlines:
#         st.session_state.checkbox_states[air] = st.checkbox(label=f"{air}", value=st.session_state.checkbox_states[air])
    
#     # Get the list of selected airlines
#     selected_airlines = [air for air, checked in st.session_state.checkbox_states.items() if checked]
    
    # Print the selected airlines
    #st.write("Selected Airlines:", selected_airlines)

#df = df.query("'Carrier legalName' in @selected_airlines")


    

grouped_data = df.groupby('Carrier legalName').agg({'Shipment#': 'count', 'Considerable Charging Unit': 'sum'}).reset_index()

grouped_data.columns = ['Carrier legalName', 'Total Shipments', 'Volume In Kgs']

# st.write(selected_airlines)
#df_chart.index = month_names_chart

top_10 = grouped_data.sort_values('Volume In Kgs', ascending=True).tail(10)
with col1:
    st.dataframe(grouped_data.sort_values('Volume In Kgs', ascending=False),hide_index=True,height=2550)

fig = px.bar(top_10, x='Volume In Kgs', y='Carrier legalName', orientation='h', title='Top 10 Categories by Value',text_auto='.2s')

# Streamlit app
st.title('Top 10 Horizontal Bar Chart')
with col2:
    st.plotly_chart(fig)

# Rotate the x-axis labels for better readability
#fig.tick_params(axis='x', rotation=45)

# Customize the chart appearance (optional)
#fig.spines['top'].set_visible(False)
#fig.spines['right'].set_visible(False)
#fig.grid(axis='x')

#st.pyplot(fig)
