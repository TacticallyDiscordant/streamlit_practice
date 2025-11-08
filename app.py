import pandas as pd
import streamlit as st

st.set_page_config(layout="wide",)
global_data_url = "https://raw.githubusercontent.com/JohannaViktor/streamlit_practical/refs/heads/main/global_development_data.csv"
global_dataset = pd.read_csv(global_data_url, delimiter=',')

st.title("Worldwide Analysis of Quality of Life and Economic Factors")
st.write("""This app enables you to explore the relationships between poverty, life expectancy, and GDP across various countries and years. Use the panels to select options and interact with the data.""")

tab1, tab2, tab3 = st.tabs(["Global Overview", "Country Deep Dive", "Data Explorer"], width="stretch")

with tab3:
    selection_country = st.multiselect("select country", options=global_dataset.country.unique(), default=global_dataset.country.unique())

    year_min, year_max = int(global_dataset["year"].min()), int(global_dataset["year"].max())
    year_range = st.slider("Select year range", min_value=year_min, max_value=year_max, value=(year_min, year_max), step=1)

    frame_data = global_dataset.query(f"country == {selection_country}")
    st.dataframe(data=frame_data, width="stretch")
