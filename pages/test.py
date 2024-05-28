import streamlit as st
from streamlit_keyup import st_keyup # type: ignore

# Sample list of airlines
airlines = ["American Airlines", "Delta Airlines", "United Airlines", "Southwest Airlines", "JetBlue Airways"]

# Initialize session state for checkbox states if not already done
if 'checkbox_states' not in st.session_state:
    st.session_state.checkbox_states = {air: False for air in airlines}

# Function to filter airlines based on the search query
def filter_airlines(query, airlines):
    return [air for air in airlines if query.lower() in air.lower()]

with st.expander(label="Select an Airline"):
    # Text input for filtering with st_keyup to capture keyup events
    query = st_keyup("Filter")
    
    # Filter the list of airlines based on the query
    filtered_airlines = filter_airlines(query, airlines)
    
    # Display checkboxes for the filtered airlines
    for air in filtered_airlines:
        st.session_state.checkbox_states[air] = st.checkbox(label=f"{air}", value=st.session_state.checkbox_states[air])
    
    # Get the list of selected airlines
    selected_airlines = [air for air, checked in st.session_state.checkbox_states.items() if checked]
    
    # Print the selected airlines
    st.write("Selected Airlines:", selected_airlines)

