###Librerie
import datetime as dt
import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
from PIL import Image
from IPython.core.display import display,HTML
import datetime as dt
from dateutil.relativedelta import relativedelta
import string
import math


def calcoloMinimo():
    global minRatingGen
    global minRatingFiltered
    global diff
    minRatingGen=11
    for i in tab['IMDB_Rating']:
        if float(i)<=minRatingGen:
            minRatingGen=i

    minRatingFiltered=11
    for i in df_filtered['IMDB_Rating']:
        if float(i)<=minRatingFiltered:
            minRatingFiltered=i

    diff=minRatingFiltered-minRatingGen

def metaMinimo():
    global minGen
    global minFiltered
    global diffMeta

    minGen=999
    
    for i in tab['Meta_score']:
        if i != "<NA>":
            if float(i)<=minGen:
                    minGen=i

    minFiltered=999
    for i in df_filtered['Meta_score']:
        if i != "<NA>":
            if float(i)<=minFiltered:
                    minFiltered=i

    diffMeta=minFiltered-minGen

def GrossMinimo():
    global minGenG
    global minFilteredG
    global diffG

    minGenG=int(9999999999)
    
    for i in tab['Gross']:
            if(str(i)!="nan"):
                a=i.replace(',','')
                num=int(a)
                
                if num<=minGenG:
                    minGenG=num


    minFilteredG=int(99999999999)
    for i in df_filtered['Gross']:
        if(str(i)!="nan"):
            a=i.replace(',','')
            num=int(a)
            if num<=minFilteredG:
                minFilteredG=num

    diffG=minFilteredG-minGenG

css_prova="""
<style>
[data-testid="stImage"]{
    padding-left: 40%;
    padding-right: 40%;
}
[data-testid="collapsedControl"]{
    color: white;
   
}
css-17nby6i.e1fqkh3o6{
    color: white;
   
}

[data-testid="stAppViewContainer"]{
    background-image: url(https://free4kwallpapers.com/uploads/originals/2022/07/16/-colorful-abstract-background-wallpaper.jpg);
    background-repeat: no-repeat;
    background-position: center;
    background-size: cover;
}
[id="dashboard-imdb"]{
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
p{
    color: white;
}

[data-testid="stMetricValue"]{
    color: red;
    font-size: 50px;
    font-weight: bolder;
}

[data-testid="stHorizontalBlock"]{
    background-color: darkblue;
    border-radius: 20px;
    padding: 20px;
}
.css-1hverof:visited{
    color:black;
}
.css-17lntkn{
    color:black;
}
.css-17nby6i:visited{
    background-color: rgb(255 255 255) !important
}

h2{
    color: limegreen;
    font-weight: bold !important;
}



</style>
"""


###Informazioni Pagina
st.set_page_config(
    page_title="Imdb Dashboard",
    page_icon="📽",
    layout="wide"
)


st.title("Dashboard IMDB")

local_filename = 'imdb_top_1000.csv'

tab = pd.read_csv(local_filename)
tab.drop(['Poster_Link'], axis = 1, inplace = True)



### Filter sidebar
st.sidebar.header("Filtri")


###calcolo inizio e fine anno

min=min(tab['Released_Year'])
max=max(tab['Released_Year'])


values = st.sidebar.slider(
    'Seleziona range temporale rilascio',
    min, max, (min, max))


title = st.sidebar.text_input('Seleziona titolo film', '')
actor = st.sidebar.text_input('Seleziona attore', '')

if (len(title) != 0 & len(actor)!=0):
    df_filtered = tab[
        (tab['Released_Year'] >= values[0]) &
        (tab['Released_Year'] <= values[1]) &
        (tab['Series_Title'] == title) &
        ((tab['Star1'] == actor) | (tab['Star2'] == actor) | (tab['Star3'] == actor) | (tab['Star1'] == actor))
        ]
    calcoloMinimo()
    metaMinimo()
    GrossMinimo()

elif len(title) != 0:
    df_filtered = tab[
        (tab['Released_Year'] >= values[0]) &
        (tab['Released_Year'] <= values[1]) &
        (tab['Series_Title'] == title)
        ]
    calcoloMinimo()
    metaMinimo()
    GrossMinimo()

elif len(actor) != 0:
    df_filtered = tab[
        (tab['Released_Year'] >= values[0]) &
        (tab['Released_Year'] <= values[1]) &
        ((tab['Star1'] == actor) | (tab['Star2'] == actor) | (tab['Star3'] == actor) | (tab['Star1'] == actor))
        ]
    calcoloMinimo()
    metaMinimo()
    GrossMinimo()

else :
    df_filtered = tab[
        (tab['Released_Year'] >= values[0]) &
        (tab['Released_Year'] <= values[1])
        ]
    calcoloMinimo()
    metaMinimo()
    GrossMinimo()


st.dataframe(df_filtered)

col1, col2, col3 = st.columns(3)

with col1:
   st.metric(label="Minimo IMDB Rating", value=str(minRatingFiltered), delta=str(round(diff,2))+"   Rispetto la media del Dataset")

with col2:
   st.metric(label="Minimo Meta Score", value=str(minFiltered), delta=str(round(diffMeta,2))+"   Rispetto la media del Dataset")

with col3:
   st.metric(label="Minimo Gross", value=str(minFilteredG), delta=str(round(diffG,2))+"   Rispetto la media del Dataset")



st.markdown(css_prova, unsafe_allow_html=True)