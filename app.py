# -*- coding: utf-8 -*-
"""
Created on Sun May  2 10:24:57 2021

@author: Annamalai
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression,LogisticRegression

st.set_page_config(page_title="Streamlit App")
st.header("Streamlit")


@st.cache
def load_data(data):
    try:
        dataset= pd.read_csv(data)
        return dataset
    except:
         return None


menu=st.sidebar.selectbox("Models",['Linear Regression','Exploratory Data Analysis'])

if menu=="Linear Regression":
    
    st.subheader('Simple Linear Regression')
    st.latex(''' y=m*x+c''')
    st.markdown('_With simple linear regression when we have a single input, we can use statistics to estimate the coefficients.This requires that you calculate statistical properties from the data such as means, standard deviations, correlations and covariance. All of the data must be available to traverse and calculate statistics._')
    dataset_load=st.sidebar.file_uploader('Upload the CSV',type=['csv'])
    if dataset_load is not None:
              df=load_data(dataset_load)
              st.dataframe(df)
              if (len(df.columns)>2):
                           ind_var=st.sidebar.multiselect('Independent Variable',df.columns) 
                           dep_var=st.sidebar.selectbox('Dependent Varaible',df.columns)
                           
                           
                           
              ind_var=st.sidebar.selectbox('Independent Variable',df.columns)
              dep_var=st.sidebar.selectbox('Dependent Varaible',df.columns)       
          
              
              if st.sidebar.button('Run'):
                               x,y=df[ind_var].values.reshape(-1,1),df[dep_var].values
                               model_file=LinearRegression()
                               model1=model_file.fit(x,y)
                               
                               fig=go.Figure(px.scatter(df,x=ind_var,y=dep_var,trendline='ols', trendline_color_override='red'))
                               st.plotly_chart(fig)
                               
                               st.success("The slope of the regression line is {}".format(int(model1.coef_)))
                               st.success("The intercept of the regression line is {}".format(int(model1.intercept_)))
                               
                               
                               
                               
                    
                       
                   
elif menu=="Exploratory Data Analysis":
      st.subheader('Exploratory Data Analysis')
      
      dataset_load=st.sidebar.file_uploader('Upload the csv',type=['csv'])
      if dataset_load is not None:
              df=load_data(dataset_load)
              st.dataframe(df)
              
              ind_var=st.sidebar.selectbox('Independent Variables',df.columns)
              
              dep_var=st.sidebar.selectbox('Dependent Variable',df.columns)
       
              plot_type=st.sidebar.selectbox('Plot Type',['scatter plot','Box plot'])
              if plot_type=='scatter plot':
                        mode=st.sidebar.selectbox('Hue',df.columns)
                        if st.sidebar.button('plot'):
                            fig=go.Figure(data=px.scatter(df,x=ind_var,y=dep_var,color=mode))
                            st.plotly_chart(fig)
                            
              elif plot_type=='Box plot':
                      try:
                        mode=st.sidebar.selectbox('Hue',df.columns)
                        if st.sidebar.button('plot'):
                            fig=go.Figure(data=px.box(df,x=ind_var,y=dep_var,color=mode))
                            st.plotly_chart(fig)
                            
                      except:
                             st.write('Invalid input')
    

