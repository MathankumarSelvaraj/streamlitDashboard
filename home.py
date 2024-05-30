import streamlit as st
import plotly.express as px
import pandas as pd
from streamlit_option_menu import option_menu
from numerize.numerize import numerize
import time
import numpy as np
#from streamlit_extras.metric_cards import style_metric_cards
#st.set_option('deprecation.showPyplotGlobalUse', False)
#import plotly.graph_objs as go

import datetime
from datetime import timedelta
import plotly.graph_objects as go

st.set_page_config(page_title="AIR 7 SEAS Air Export Volume Dashboard", page_icon=":bar_chart:", layout="wide")
st.markdown("This visualization uses fabricated data for practice purposes ️. Don't mistake it for real information! ⚠️")
st.header("Volume By Month")

#Load CSS file
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

class AirExportVolumeDashboard:

    def __init__(self, data_path):
        self.data_path = data_path
        self.df = self.load_data()
        print("this method excecited")
        #self.filters = self.setup_filters()

    def load_data(self):
        df = pd.read_csv(self.data_path)
        df['createdDate'] = pd.to_datetime(df['createdDate'])
        df['year'] = df['createdDate'].dt.year
        df['month'] = df['createdDate'].dt.month
        df['date'] = df['createdDate'].dt.date
        df= df.query('year != 2020')

        return df

    #def setup_filters(self):
        #distintYear = self.df['year'].unique()
        # destinationCountry = self.df["Destination country"].unique()
        #distintAirline = self.df["Carrier legalName"].unique()

        # dtCountry = st.sidebar.multiselect(
        #     "Select the country:",
        #     options=destinationCountry,default=default
        # )
        # year = st.selectbox(
        #     "select the year:",
        #     options=distintYear
        # )

        # airline = st.multiselect(
        #     "Select the airline", 
        #     options = distintAirline,
        #     placeholder= "Choose an option"
        #     )
        # return  year,airline

    #def filter_data(self):
        # Check if any filter has selections
        #if all(filter(None, setup_filters)):  # Check if all filters have values
        #df_selection = self.df.query(f" year == @year & Carrier legalName == @airline")
        #else:
  # Handle the case where no filters are selected (optional)
           # df_selection = self.df.copy()  # Use the original data

        #return df_selection

    def calculate_metrics(self):
        
        
        enddate = max(self.df["date"])
        currentyear = enddate.year
        startdate = min(self.df.query("year == @currentyear")["date"])
        endDate_py = enddate -timedelta(days=366)
        startdate_py = startdate - timedelta(days=365)
        metric_df = self.df.query("date >= @startdate and date <= @enddate")
        metric_df_PY = self.df.query("date >= @startdate_py and date <= @endDate_py")
        sumOfVolume = metric_df["Considerable Charging Unit"].sum()
        #sumOfVolume = df.query("year" == datetime.datetime.now().year)["Considerable Charging Unit"].sum()
        sumOfVolumeinTonn = sumOfVolume/1000
        sumOfVolume_py = metric_df_PY["Considerable Charging Unit"].sum()
        sumOfVolumeinTonn_py = sumOfVolume_py/1000
        return sumOfVolume,sumOfVolumeinTonn,sumOfVolume_py,sumOfVolumeinTonn_py

    # def prepare_country_data(self, df):
    #     groupbycounrty = pd.DataFrame(df.groupby("Destination country").sum("Considerable Charging Unit"))
    #     countrydata = groupbycounrty.sort_values("Considerable Charging Unit", ascending=False)
    #     return countrydata.round(2) if self.filters[0] else countrydata

    def prepare_monthly_data(self, df):
         # Use month name for readability
        month_map = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
              7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
        #Monthly table with Change
        df_table = df.groupby([df['month'], df['year']])['Considerable Charging Unit'].sum().unstack().apply(np.ceil)
        yoy_monthly_change = round((df_table / df_table.shift(1, axis=1) - 1) * 100,0)
        for i in range(1, len(yoy_monthly_change.columns)):  # Iterate through year difference columns (excluding the first)
            year = yoy_monthly_change.columns[i]
            prev_year = yoy_monthly_change.columns[i-1]
            # Insert MoM DoD column between current and previous year columns
            df_table.insert(df_table.columns.get_loc(prev_year) + 1, f'{year} Monthly ▲ %', yoy_monthly_change[year])
        month_names_table = df_table.index.get_level_values('month').map(month_map)
        df_table.index = month_names_table
        def _format_arrow(val):
            return f"{'↑' if val > 0 else '↓'} {val:.0f}%" if val != 0 else f"{val:.0f}%"

        def _color_arrow(val):
            return "color: green" if val > 0 else "color: red" if val < 0 else "color: black"
        def _round(val):
            return(round(val,0))
        styled_df = df_table.style.map(
            _color_arrow, 
            subset=["2022 Monthly ▲ %", "2023 Monthly ▲ %","2024 Monthly ▲ %"]
            ).format(
                _format_arrow, 
                subset=["2022 Monthly ▲ %", "2023 Monthly ▲ %","2024 Monthly ▲ %"],
                )
        #Monthly_Chart
        df_chart = df.groupby([df['month'], df['year']])['Considerable Charging Unit'].sum().reset_index("year")
        
        month_names_chart = df_chart.index.get_level_values('month').map(month_map)
        df_chart.index = month_names_chart
        df_chart = pd.DataFrame(df_chart)

      

# Assuming you have already executed the provided code snippet to prepare df_table and month_names_table

# Create a Plotly table
#         fig2 = go.Figure(data=[go.Table(
#         header=dict(values=['Month'] + df_table.columns.tolist(), fill_color='lightblue', align='center'),
#         cells=dict(values=[month_names_table] + [df_table[col] for col in df_table.columns],
#                fill_color='white', align='center'))
#                 ])

# # Update table layout
#         fig2.update_layout(title='Year-over-Year Monthly Changes',
#                   margin=dict(l=20, r=20, t=40, b=20),
#                   height=600)

        

        return styled_df,df_chart

    def create_visualization(self, df_chart):
        
        fig = px.line(df_chart,
                      x=df_chart.index,
                      y=df_chart["Considerable Charging Unit"],
                      color=df_chart["year"],
                      title="Weight by Month and Year",
                      markers=True,
                      line_shape="spline")
        
        fig.update_traces(textposition='top center',  # Place data labels on top center
                   #text=df_chart[df_chart['year'] == 2024]["Considerable Charging Unit"],  # Show labels only for 2024
                   #visible=df_chart['year'] == 2024)
        )
        
        fig.update_yaxes(title_text="Volume in Kgs")
        #fig.update_xaxes(title_text=" ")

        
    
        return fig

    def render_dashboard(self):
        #df_selection = self.filter_data()
        sumOfVolume,sumOfVolumeinTonn,sumOfVolume_py,sumOfVolumeinTonn_py = self.calculate_metrics()
        #countrydata = self.prepare_country_data(df_selection)
        df_table, df_chart = self.prepare_monthly_data(self.df)  # Avoid modifying original data
        fig = self.create_visualization(df_chart)
        
        #col1,col2=st.columns(2,gap="small")
        #with col1:
            #st.metric(label="Total Volume in Kgs", value=round(sumOfVolume, 1), delta=None)
            #st.info('Sum Investment',icon="💰")
        st.sidebar.metric(
            label="Total Volume in Kgs",
            value=f"{round(sumOfVolume, 1):,.0f} KGS",
            delta=f"{round(((sumOfVolume-sumOfVolume_py)/sumOfVolume_py)*100,0):,.0f} % "
        )

        #with col2:
            #st.metric(label="Total Volume in Tonns", value=round(sumOfVolumeinTonn, 1), delta=None)
        st.sidebar.metric(
            label="Total Volume in Tonns",
            value=f"{round(sumOfVolume, 1)/1000:,.0f} TONNS",
            delta = f"{round(((sumOfVolumeinTonn-sumOfVolumeinTonn_py)/sumOfVolumeinTonn_py)*100,0):,.0f} % "
            )

        #st.dataframe(countrydata)
        
        st.dataframe(df_table,use_container_width=True,height=460)
        #st.dataframe(df_chart)
        
        st.plotly_chart(fig,use_container_width=True,sharing= "streamlit",theme="streamlit")
        

if __name__ == "__main__":
    data_path = r"datasets/airExportVolume2023.csv"
    dashboard = AirExportVolumeDashboard(data_path)
    

    
    dashboard.render_dashboard()
