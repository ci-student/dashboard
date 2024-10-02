import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Set the option to opt-in to the future behavior
pd.set_option('future.no_silent_downcasting', True)

df = pd.read_csv('inputs/insurance.csv')

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

def filter(df):
    age_input = st.sidebar.select_slider("Age", options=range(0, 100))
    age_filter = df["age"] > age_input
    df_filter = df[age_filter]

def smoker(df):
    smoker_input = st.sidebar.selectbox("Smoker", options=['yes', 'no'])
    smoker_filter = df["smoker"] == smoker_input
    df_filter = df[smoker_filter]

def dashboard_body():
    st.title('Dashboard')
    st.write('This is the dashboard page')
    st.write('Scatter plot of age, bmi and charges')
    age_input = st.sidebar.select_slider("Age", options=range(0, 100))
    age_filter = df["age"] > age_input
    smoker_input = st.sidebar.selectbox("Smoker", options=['yes', 'no'])
    smoker_filter = df["smoker"] == smoker_input
    df_filter = df.loc[age_filter & smoker_filter]
    scatter(df_filter)
    stacked(df_filter)
    parallel(df_filter)