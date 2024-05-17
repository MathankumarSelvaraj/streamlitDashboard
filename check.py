import numpy as np
import pandas as pd
import streamlit as st

def load_data():
    return pd.DataFrame(np.random.randint(-100, 100, size=(100, 2)), columns=list("ab"))

def _format_arrow(val):
    return f"{'↑' if val > 0 else '↓'} {abs(val):.0f}%" if val != 0 else f"{val:.0f}%"

def _color_arrow(val):
    return "color: green" if val > 0 else "color: red" if val < 0 else "color: black"

df = load_data()
st.dataframe(df)
styled_df = df.style.format(_format_arrow).applymap(_color_arrow, subset=["a", "b"])
st.dataframe(styled_df)