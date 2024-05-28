import streamlit as st

# Sample data
carriers = [f'Carrier {i}' for i in range(1, 71)]  # 70 carriers
years = [2021, 2022, 2023, 2024]  # 4 years

# Helper function to handle the multiselect with "Select All" option
def multiselect_with_select_all(label, options):
    # Checkbox to select all
    select_all = st.checkbox(f"Select all {label}")
    if select_all:
        selected_options = options
    else:
        selected_options = st.multiselect(f"Select {label}", options, default=options)
    return selected_options

# Title
st.title("Carrier and Year Filter Example")

# Multiselect filters with select all option
selected_carriers = multiselect_with_select_all('Carriers', carriers)
selected_years = multiselect_with_select_all('Years', years)

# Display the selected filters
st.write("Selected Carriers:", selected_carriers)
st.write("Selected Years:", selected_years)

# Sample display of filtered data (for demonstration purposes)
filtered_data = {
    "Carriers": selected_carriers,
    "Years": selected_years,
}
st.write("Filtered Data", filtered_data)
