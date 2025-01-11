import random

import geopandas as gpd
import pandas as pd
import streamlit as st
from shapely import wkt
from streamlit_folium import st_folium

st.title("Travel Maker")
df = pd.read_csv("gdf.csv")
df["geometry"] = df["geometry"].apply(wkt.loads)
gdf = gpd.GeoDataFrame(df, geometry=df["geometry"], crs="EPSG:4326")


col1, col2, col3 = st.columns(3)

# Initialize session state variables
if "dice1" not in st.session_state:
    st.session_state["dice1"] = None
if "dice2" not in st.session_state:
    st.session_state["dice2"] = None
if "dice3" not in st.session_state:
    st.session_state["dice3"] = None

# Layout with three columns
col1, col2, col3, col4 = st.columns(4)

# Dice 1 Button
with col1:
    if st.button("Roll Dice 1", disabled=st.session_state["dice1"] is not None):
        st.session_state["dice1"] = random.randint(1, 6)
    st.write(f"{st.session_state['dice1']}")

# Dice 2 Button
with col2:
    if st.button("Roll Dice 2", disabled=st.session_state["dice2"] is not None):
        st.session_state["dice2"] = random.randint(1, 6)
    st.write(f"{st.session_state['dice2']}")

# Dice 3 Button
with col3:
    if st.button("Roll Dice 3", disabled=st.session_state["dice3"] is not None):
        st.session_state["dice3"] = random.randint(1, 6)
    st.write(f"{st.session_state['dice3']}")

with col4:
    if st.button(
        "Reset",
        disabled=not (
            (st.session_state["dice1"] is not None)
            & (st.session_state["dice2"] is not None)
            & (st.session_state["dice3"] is not None)
        ),
    ):
        st.session_state["dice1"] = None
        st.session_state["dice2"] = None
        st.session_state["dice3"] = None

filtered_gdf = gdf[
    ((gdf["area1"] == st.session_state["dice1"]) | (st.session_state["dice1"] == None))
    & (
        (gdf["area2"] == st.session_state["dice2"])
        | (st.session_state["dice2"] == None)
    )
    & (
        (gdf["area3"] == st.session_state["dice3"])
        | (st.session_state["dice3"] == None)
    )
]
st_folium(filtered_gdf.explore(), use_container_width=True, height=720)
st.dataframe(filtered_gdf["religion_name"])
