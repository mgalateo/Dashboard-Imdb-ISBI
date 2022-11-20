###Librerie
import datetime as dt
import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np



###Informazioni Pagina
st.set_page_config(
    page_title="Imdb Dashboard",
    page_icon="📽",
    layout="wide"
)

###Lettura Dataset
local_filename = 'imdb_top_1000.csv'

df = pd.read_csv(local_filename)




###Stampa tabella interattiva
st.dataframe(df)