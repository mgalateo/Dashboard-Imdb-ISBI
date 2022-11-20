###Librerie
import datetime as dt
import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
from PIL import Image
from IPython.core.display import display,HTML

css_prova="""
<style>
[data-testid="stImage"]{
    padding-left: 40%;
    padding-right: 40%;
}
[data-testid="stAppViewContainer"]{
    background-image: url(https://free4kwallpapers.com/uploads/originals/2022/07/16/-colorful-abstract-background-wallpaper.jpg);
    background-repeat: no-repeat;
    background-position: center;
    background-size: cover;
}
[id="home-imdb"]{
    font-size: 72px;
    color: crimson;
    text-shadow: -1px 0 snow, 0 1px snow, 1px 0 snow, 0 -1px snow;
}

[data-testid="stSidebar"]{
    background-color: dodgerblue;
    opacity: 0.8;
}
[data-testid="stHeader"]{
    background-color: black;
}
[data-testid="stToolbar"]{
    color: white;
}
[data-testid="stMarkdownContainer"]{
    overflow: scroll;
    background: aliceblue;
    width: 1655px !important; 
   
}
td{
    padding: 0px 0px 0px 0px !important;
}
tr{
    padding: 0px 0px 0px 0px !important;
    text-align: left !important;
    font-size: 14px !important;
}
tbody{
    padding: 0px 0px 0px 0px !important;
}
th{
    padding: 0px 0px 0px 0px !important;
}






</style>
"""


###Informazioni Pagina
st.set_page_config(
    page_title="Imdb Dashboard",
    page_icon="📽",
    layout="wide"
)



st.title("Home IMDB")


image = Image.open('./Image/logoIMDB.png')
st.image(image)



###Lettura Dataset
local_filename = 'imdb_top_1000.csv'

df = pd.read_csv(local_filename)
 

thumbnails = []
for url in df['Poster_Link']:
    thumbnail_url = '<img src="'+ url + '"  >'
    thumbnails.append(thumbnail_url)

df['Thombnail']=thumbnails
df.drop(['Poster_Link'], axis = 1, inplace = True)

tabella=df.to_html(escape=False)


st.markdown(tabella, unsafe_allow_html=True)



st.markdown(css_prova, unsafe_allow_html=True)