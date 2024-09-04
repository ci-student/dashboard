import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt

df = pd.read_csv('data/insurance.csv')

def scatter(df):
    fig = plt.figure(figsize=(10,8))
    ax = plt.axes(projection='3d')

    x = df['age']
    y = df['bmi']
    z = df['charges']

    ax.scatter(x, y, z)
    st.pyplot(fig)

def pearson(df):
    df_corr = df.corr(method='pearson')
    mask = np.zeros_like(df_corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    sns.heatmap(df_corr,annot=True,mask=mask,cmap='viridis',annot_kws={"size": 8},linewidths=0.5)
    plt.ylim(df_corr.shape[1],0);
    plt.title('Pearson Correlation')
    st.pyplot()

def dashboard_body():
    st.title('Insurance Dashboard')
    st.write('This is a simple dashboard for insurance data')

    st.write('## Data')
    st.write(df)

    st.write('## Scatter Plot')
    scatter(df)

    pearson(df)

    st.write('## Altair Plot')
    chart = alt.Chart(df).mark_circle().encode(
        x='age',
        y='bmi',
        size='charges'
    ).interactive()
    st.altair_chart(chart)

    st.write('## Plotly Plot')
    fig = px.scatter_3d(df, x='age', y='bmi', z='charges', size='charges')
    st.plotly_chart(fig)