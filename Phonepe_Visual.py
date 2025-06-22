import json
import streamlit as st
import pandas as pd
import requests
import psycopg2
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Phonepe Data Visualisation", page_icon=":phone:", layout="wide")
# st.title("Phonepe Data Visualisation")

with st.sidebar:

    selected = option_menu("Main Menu", ["Home", "Data Visualisation", "Top Charts"])

if selected == "Home":
    pass

elif selected == "Data Visualisation":
    tab_1, tab_2, tab_3 = st.tabs(["Aggredated Analysis", "Map Analysis", "Top Analysis"])

    with tab_1:
        method_1 = st.radio("Select The Method", ["Insurance Analysis", "Transaction Analysis", "User Analysis"])

        if method_1 == "Insurance Analysis":
            pass

        elif method_1 == "Transaction Analysis":
            pass

        elif method_1 == "User Analysis":
            pass

    with tab_2:
        method_2 = st.radio("Select The Method", ["Map Insurance", "Map Transaction", "Map User"])

        if method_2 == "Map Insurance":
            pass

        elif method_2 == "Map Transaction":
            pass

        elif method_2 == "Map User":
            pass

    with tab_3:
        method_3 = st.radio("Select The Method", ["Top Insurance", "Top Transaction", "Top User"])

        if method_3 == "Top Insurance":
            pass

        elif method_3 == "Top Transaction":
            pass

        elif method_3 == "Top User":
            pass

elif selected == "Top Charts":
    pass