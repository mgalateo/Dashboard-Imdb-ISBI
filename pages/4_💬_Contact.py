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

[data-testid="collapsedControl"]{
    color: white;
   
}
[data-testid="stAppViewContainer"]{
    background-image: url(https://free4kwallpapers.com/uploads/originals/2022/07/16/-colorful-abstract-background-wallpaper.jpg);
    background-repeat: no-repeat;
    background-position: center;
    background-size: cover;
}
[id="contact"]{
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

h2{
    color: limegreen;
    font-weight: bold !important;
}

img{
    border-radius: 125px;

}
img:hover{
    scale: 1.1;
}
#spazio{
    padding:10px;

}
#gitHub{
    text-align: center;


}
h3{
    color: snow;
}
@media only screen and (max-width: 600px) {
    img{
        width: 400px !important;
    }

}

</style>
"""
bottone="""
<div>
    <div id="spazio">
    <div>
    <div id="gitHub">
        <a href="https://github.com/mgalateo/Dashboard-Imdb-ISBI"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0zoEI0fhI8N5-2qC35jCUOfpXBZz9FjBEJxqY80CvzdRX8Zrzo6CC-C0MQQpkz8aYDIM&usqp=CAU" /></a>
        <h3>Premi per visualizzare la repository</h3>  
    </div>
</div>
"""


###Informazioni Pagina
st.set_page_config(
    page_title="Imdb Dashboard",
    page_icon="📽",
    layout="wide"
)


st.title("Contact")

imageC = Image.open('./Image/Contatti.png')
st.image(imageC, width=1411)



st.markdown(bottone,unsafe_allow_html=True)

st.markdown(css_prova, unsafe_allow_html=True)

st.snow()