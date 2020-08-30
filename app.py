import streamlit as st 
import pandas as  pd 
import numpy as np 
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

while True:
    URL='https://www.worldometers.info/coronavirus/'

    r=requests.get(URL)

    soup=BeautifulSoup(r.content,'html5lib')

    totalnumbers=soup.findAll('div',attrs={'id':'maincounter-wrap'})

    nowtime=datetime.now()
    datetimedata=nowtime.strftime("%d/%m/%Y %H:%M:%S")

    data=[datetimedata]
    for result in totalnumbers:
        result=str(result.span.text).replace(",","")
        result=int(result)
        data.append(result)

    dataframe=pd.read_csv('data.csv')

    entries=len(dataframe)

    print("***Storing Datas***")
    dataframe.loc[entries,:]=data

    dataframe.to_csv('data.csv',index=False)

    st.title("COVID-19 WORLDWIDE LATEST TREND ((GMT+5.45) NEPAL)")


    data1=pd.read_csv("data.csv")

    data1=data1.rename(columns={'Date':'index'}).set_index('index')

    #st.dataframe(data)

    if st.button('Generated by Pratik Ghimire'):
        js = "window.open('https://www.linkedin.com/in/pratik-ghimire/')"  # New tab or window
        js = "window.location.href = 'https://www.linkedin.com/in/pratik-ghimire/'"  # Current tab
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)


    st.line_chart(data=data1,width=0,height=450)

    time.sleep(120)