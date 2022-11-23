###Librerie
import datetime as dt
import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
from PIL import Image
from IPython.core.display import display,HTML
import plotly.figure_factory as ff

css_prova="""
<style>
[data-testid="stImage"]{
    padding-left: 40%;
    padding-right: 40%;
}
[data-testid="collapsedControl"]{
    color: white;
   
}
[data-testid="stAppViewContainer"]{
    background-image: url(https://free4kwallpapers.com/uploads/originals/2022/07/16/-colorful-abstract-background-wallpaper.jpg);
    background-repeat: no-repeat;
    background-position: center;
    background-size: cover;
}
[id="plot"]{
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
.css-1hverof:visited{
    color:black;
}
.css-17lntkn{
    color:black;
}
.css-17nby6i:visited{
    background-color: rgb(255 255 255) !important
}
.main-svg{
    border-radius: 100px;
    border-style: solid;
    border-color: #1b96ff;
    border-width: 5px;
    padding: 0px ;
}

h2{
    color: limegreen;
    font-weight: bold !important;
}
#grafici-generi{
    color: lightgreen;
    font-style: italic;
    font-family: monospace;

}
#grafici-incassi{
    color: lightgreen;
    font-style: italic;
    font-family: monospace;

}


</style>
"""


###Informazioni Pagina
st.set_page_config(
    page_title="Imdb Dashboard",
    page_icon="📽",
    layout="wide"
)


st.title("Plot")

local_filename = 'imdb_top_1000.csv'

tab = pd.read_csv(local_filename)
tab.drop(['Poster_Link'], axis = 1, inplace = True)

generi=tab["Genre"].unique()

generivett=[]

n=0
for i in tab["Genre"]:
    stringa=str(i)
    if (',' in stringa):
        genere=stringa.split(',')[0]
        generivett.append(genere)
        
    else:
        generivett.append(i)

dfA=tab

dfA['Genre']=generivett
generiUnici=dfA['Genre'].unique()



qta=[]    
for gen in generiUnici:
    q=generivett.count(gen)
    qta.append(int(q))

arr = np.array(qta)

label=np.array(generiUnici)


dataFrame = pd.DataFrame(list(zip(generiUnici,qta)), columns = ['Genere','Quantita'])

st.title("Grafici generi 🎂")
fig = px.pie(dataFrame, values='Quantita', names='Genere', title='Film per genere')


st.plotly_chart(fig, use_container_width=True)

fig2 = px.histogram(dataFrame, x='Genere', y='Quantita',color="Genere", text_auto=True, title='Film per genere')
st.plotly_chart(fig2, use_container_width=True)

st.title("Grafici incassi 💶")


dataMod=tab
dataMod['Genre']=generivett

vett=[]
for i in tab['Gross']:
            if(str(i)!="nan"):
                a=i.replace(',','')
                num=int(a)
                vett.append(num)
            else:
                vett.append(0)

dataMod['Gross']=vett

fig3 = px.histogram(dataMod, x='Genre', y='Gross',color="Genre", text_auto=True, title='Totale incassi per genere')
st.plotly_chart(fig3, use_container_width=True)

dfAppoggio=pd.DataFrame()
vettMedie=[]
for j in generiUnici:
    dfAppoggio=dataMod[dataMod['Genre']==j]
    media=round(dfAppoggio['Gross'].mean(),2)
    vettMedie.append(media)

dfMedie=pd.DataFrame()
dfMedie['Genere']=generiUnici
dfMedie['Media']=vettMedie


fig4 = px.histogram(dfMedie, x='Genere', y='Media',color="Genere", text_auto=True, title='Media incassi per genere')
st.plotly_chart(fig4, use_container_width=True)


dfAnni=pd.DataFrame()

annoString=[]

for a in tab['Released_Year']:
    annoString.append(str(a))

dfAnni['Gross']=vett
dfAnni['Anno']=annoString

dfAnni.sort_values(by=['Anno'], ascending = True, inplace = True)
#st.line_chart(dfAnni,x='Anno')

fig5 = px.histogram(dfAnni, x="Anno", y="Gross",color="Anno", title='Incassi negli anni')
st.plotly_chart(fig5, use_container_width=True)





st.markdown(css_prova, unsafe_allow_html=True)
