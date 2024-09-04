import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/insurance.csv')

def filter(df):
    st.write('## Filter Data')
    smokers = st.checkbox('Smokers', value=True)
    if smokers:
        df = df[df['smoker']=='yes']
    else:
        df = df[df['smoker']=='no']
    return df

def scatter(df):
    fig = plt.figure(figsize=(10,8))
    ax = plt.axes(projection='3d')

    x = df['age']
    y = df['bmi']
    z = df['charges']

    ax.scatter(x, y, z)
    st.pyplot(fig)

def stacked(df):
    df.groupby(['smoker','region']).size().unstack().plot(kind='bar', stacked=True)
    st.pyplot(plt)

def parallel(df):
    df['smoker'] = df['smoker'].replace({'no':0, 'yes':1})
    df['sex'] = df['sex'].replace({'male':0, 'female':1})
    df['region']= df['region'].replace({'northwest':0, 'northeast':1, 'southwest':2, 'southeast':3})
    fig = px.parallel_coordinates(df, color="smoker",
                              dimensions = ['age','sex','bmi',
                                            'children',	'region','charges'])
    st.plotly_chart(fig)

def dashboard_body():
    st.title('Insurance Dashboard')
    st.write('This is a simple dashboard for insurance data')
    filter(df)
    st.write('## Data')
    st.write(df)

    st.write('## Scatter Plot')
    scatter(df)

    stacked(df)

    parallel(df)
