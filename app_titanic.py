#IMPORTANTE TENER STREAMLIT INSTALADO PARA QUE FUNCIONE

#importamos librerias para el proyecto
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

#pr configuración de página simple
st.set_page_config(page_title = 'TITANIC DASHBOARD', page_icon=':shark:', layout='wide')

#textos de la página
st.title('TITANIC DASHBOARD')

#menu
st.sidebar.title('MENU')
st.sidebar.button ('Inicio')
st.sidebar.button ('Análisis de datos')
st.sidebar.button ('Gráficos')
st.sidebar.button ('3D')

#datos
df = pd.read_csv("Data/titanic_final.csv")

#funciones utiles y gráficos
#gráfico de barras
def bar_chart(data,s,y):
    fig = px.bar(data, x=s, y=y)
    return fig

#funcion para gráficos 3d
def scatter_3d(data,x,y,z):
    fig = px.scatter_3d(data, x=x, y=y, z=z)
    return fig
    
    
#tabs
tab1, tab2, tab3, tab4 = st.tabs(['Libre', 'Análisis de datos', 'Gráficos', '3D'])
with tab1:
    #creamos columnas dentro de la tabla
    col1,col2,col3 = st.columns(3)
    with col1:
        pie__chart = px.pie(df,'sex')
        st.plotly_chart(pie__chart) 
    with col2:
        pie__chart = px.pie(df,'alive')
        st.plotly_chart(pie__chart) 
    with col3:
        pie__chart = px.pie(df,'pclass')
        st.plotly_chart(pie__chart)          
with tab2:
    st.dataframe(df)
with tab3:
    st.text('Aquí van los gráficos')
    #gráfico de barras
    st.subheader ('Gráfico de Barras')
    graph1 = bar_chart (df, 'pclass', 'sex')
    st.plotly_chart(graph1) 
    
with tab4:
    st.text('Aquí relacionamos 3 datos con una gráfica 3d')
    st.subheader ('Gráfico eD')
    graph2 = scatter_3d(df, 'age', 'alone', 'pclass')
    st.plotly_chart(graph2) 
    


