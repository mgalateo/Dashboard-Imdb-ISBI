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
    global mediaRatingGen
    global mediaRatingFil
    global diffMedia

    mediaRatingGen=0
    mediaRatingFil=0
    diffMedia=0

    somma=0.0
    n=0
    minRatingGen=11
    for i in tab['IMDB_Rating']:
        somma=somma+(float(i))
        n=n+1
        if float(i)<=minRatingGen:
            minRatingGen=i
    if n !=0:
        mediaRatingGen=somma/n


    somma=0.0
    n=0    
    minRatingFiltered=11

    for i in df_filtered['IMDB_Rating']:
        somma=somma+(float(i))
        n=n+1
        if float(i)<=minRatingFiltered:
            minRatingFiltered=i

    diff=minRatingFiltered-minRatingGen

    if n !=0:
        mediaRatingFil=somma/n
        diffMedia= mediaRatingFil- mediaRatingGen
    else:
        mediaRatingFil=0
        diffMedia=0
        minRatingFiltered=0

def metaMinimo():
    global minGen
    global minFiltered
    global diffMeta
    global mediaMetaGen
    global mediaMetaFil
    global diffMediaMeta


    mediaMetaGen=0
    mediaMetaFil=0
    diffMediaMeta=0

    somma=0.0
    n=0
    minGen=999
    
    for i in tab['Meta_score']:
        if i != "<NA>":
            if(str(i)!="nan"):
                somma=somma+(float(i))
                n=n+1
                if float(i)<=minGen:
                        minGen=i

    if n !=0:
        mediaMetaGen=somma/n

    somma=0
    n=0
    minFiltered=999
    for i in df_filtered['Meta_score']:
        if i != "<NA>":
            if(str(i)!="nan"):
                somma=somma+(int(i))
                n=n+1
                if float(i)<=minFiltered:
                        minFiltered=i

    if n !=0:
        mediaMetaFil=somma/n
        diffMediaMeta=mediaMetaFil-mediaMetaGen
    else:
        mediaMetaFil=0
        diffMediaMeta=0
        minFiltered=0
    diffMeta=minFiltered-minGen

def GrossMinimo():
    global minGenG
    global minFilteredG
    global diffG
    global mediaGrossGen
    global mediaGrossFil
    global diffMediaGross

    mediaGrossGen=0
    mediaGrossFil=0
    diffMediaGross=0
    somma=0
    n=0

    minGenG=int(9999999999)
    
    for i in tab['Gross']:
            if(str(i)!="nan"):
                a=i.replace(',','')
                num=int(a)
                somma=somma+num
                n=n+1
                
                if num<=minGenG:
                    minGenG=num
    
    if n !=0:
        mediaGrossGen=somma/n

    somma=0
    n=0
    minFilteredG=int(99999999999)
    for i in df_filtered['Gross']:
        if(str(i)!="nan"):
            a=i.replace(',','')
            num=int(a)
            somma=somma+num
            n=n+1
            if num<=minFilteredG:
                minFilteredG=num

    diffG=minFilteredG-minGenG
    if n !=0:
        mediaGrossFil=somma/n
        diffMediaGross=mediaGrossFil-mediaGrossGen
    else:
        mediaGrossFil=0
        diffMediaGross=0
        minFilteredG=0

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
[id="minimo-rating"]{
    color: crimson;
}
[id="minimo-score"]{
    color: crimson;
}
[id="minimo-gross"]{
    color: crimson;
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
   st.metric(label="Minimo IMDB Rating", value=str(minRatingFiltered), delta=str(round(diff,2))+"   Rispetto  Dataset non filtrato")

with col2:
   st.metric(label="Minimo Meta Score", value=str(minFiltered), delta=str(round(diffMeta,2))+"   Rispetto Dataset non filtrato")

with col3:
   st.metric(label="Minimo Gross", value=str(minFilteredG), delta=str(round(diffG,2))+"   Rispetto Dataset non filtrato")


###calcolo della media




col4, col5, col6 = st.columns(3)

with col4:
   st.metric(label="Media IMDB Rating", value=str(round(mediaRatingFil,3)), delta=str(round(diffMedia,3))+"   Rispetto Dataset non filtrato")

with col5:
   st.metric(label="Media Meta Score", value=str(round(mediaMetaFil,3)), delta=str(round(diffMediaMeta,3))+"   Rispetto  Dataset non filtrato")

with col6:
   st.metric(label="Media Gross", value=str(round(minFilteredG,3)), delta=str(round(diffG,3))+"   Rispetto Dataset non filtrato")


st.title("Minimo rating")
dfRating = tab[
    (tab['IMDB_Rating'] == minRatingFiltered) 
    ]

st.dataframe(dfRating)


st.title("Minimo score")
dfScore = tab[
    (tab['Meta_score'] == minFiltered) 
    ]

st.dataframe(dfScore)

st.title("Minimo gross")

dfGross=tab

vett=[]
for i in tab['Gross']:
            if(str(i)!="nan"):
                a=i.replace(',','')
                num=int(a)
                vett.append(num)
            else:
                vett.append(0)

#dfGross['GrossINT']=vett

dfGross['Gross']=vett

dfGrossFin=dfGross[
    (dfGross['Gross'] == minFilteredG) 
    ]



st.dataframe(dfGrossFin)




st.markdown(css_prova, unsafe_allow_html=True)