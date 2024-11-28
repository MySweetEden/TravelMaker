import random

import pandas as pd
import streamlit as st

st.title("Travel Maker")
df = pd.read_csv("table.csv")

col1, col2, col3 = st.columns(3)

# Initialize session state variables
if "dice1" not in st.session_state:
    st.session_state["dice1"] = None
if "dice2" not in st.session_state:
    st.session_state["dice2"] = None
if "dice3" not in st.session_state:
    st.session_state["dice3"] = None

# Layout with three columns
col1, col2, col3 = st.columns(3)

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

st.dataframe(
    df[
        (
            (df["area1"] == st.session_state["dice1"])
            | (st.session_state["dice1"] == None)
        )
        & (
            (df["area2"] == st.session_state["dice2"])
            | (st.session_state["dice2"] == None)
        )
        & (
            (df["area3"] == st.session_state["dice3"])
            | (st.session_state["dice3"] == None)
        )
    ][["religion1", "religion2", "religion3"]],
    width=500,
)
