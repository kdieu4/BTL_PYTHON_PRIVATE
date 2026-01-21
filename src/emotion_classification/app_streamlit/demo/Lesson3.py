import streamlit as st
import numpy as np
import pandas as pd

df = pd.DataFrame({
    "Diện tích": [60, 80, 100],
    "Giá (tỷ VND)": [3.2, 4.1, 5.6] 
})

st.dataframe(df)
st.dataframe(df.style.highlight_max(axis=0, subset=['Diện tích', 'Giá (tỷ VND)'], color="Lightgreen"), width=600, height=250)

st.header('Ví dụ với `st.table()`')
st.table(df)

my_json_obj = {
    "Name": "Streamlit App",
    "Version": "1.0",
    "Feature": ["display text", "display data", "interactive widgets"]
}
st.json(my_json_obj)

st.json(my_json_obj, expanded=False)
