import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# 0 configure the page
st.set_page_config(
    page_title="Stock Data App",
    page_icon="🧊",
    layout="wide",
)

# 1 load the data steps
@st.cache_data
def load_data():
    url = 'Data/apple_stock.csv'
    df = pd.read_csv(url, parse_dates=['Date'])
    return df

# 2 build the UI
st.title("Stock Data App")
with st.spinner("Loading data..."):
    df = load_data()

st.header("Apple Stock Prices Dataset")
st.info("Raw data in Data frame")
st.dataframe(df, use_container_width=True)
st.success("Column information in the dataset")
cols = df.columns.tolist()
st.subheader(f'Total columns: {len(cols)} ⏩ {",".join(cols)}')

# 3 add some graphs and widgets
st.header("Basic Data Visualization")

# Graph 1: Line chart for Closing Prices Over Time
fig1 = px.line(df, x='Date', y='Close', title='Apple Stock Closing Prices Over Time')

# Graph 2: Bar chart for Volume Over Time
fig2 = px.bar(df, x='Date', y='Volume', title='Apple Stock Volume Over Time')

# Graph 3: Scatter plot for Opening Prices and Closing Prices
fig3 = px.scatter(df, x='Open', y='Close', title='Scatter Plot: Opening Prices vs Closing Prices')

# Graph 4: Scatter plot for Closing Prices and Volume
fig4 = px.scatter(df, x='Close', y='Volume', title='Scatter Plot: Closing Prices vs Volume')

# Graph 5: Histogram for Closing Prices Distribution
fig5 = px.histogram(df, x='Close', nbins=30, title='Closing Prices Distribution')

# Graph 6: Box plot for Closing Prices
fig6 = px.box(df, x='Close', points="all", title='Box Plot: Closing Prices')

# Graph 7: Line chart for Opening Prices Over Time
fig7 = px.line(df, x='Date', y='Open', title='Apple Stock Opening Prices Over Time')

# Graph 8: Area chart for Closing Prices Over Time
fig8 = px.area(df, x='Date', y='Close', title='Apple Stock Closing Prices Over Time (Area Chart)')

# Graph 9: Bar chart for High Prices Over Time
fig9 = px.bar(df, x='Date', y='High', title='Apple Stock High Prices Over Time')

# Graph 10: Bar chart for Low Prices Over Time
fig10 = px.bar(df, x='Date', y='Low', title='Apple Stock Low Prices Over Time')

# Displaying graphs
st.plotly_chart(fig1, use_container_width=True)
st.plotly_chart(fig2, use_container_width=True)
st.plotly_chart(fig3, use_container_width=True)
st.plotly_chart(fig4, use_container_width=True)
st.plotly_chart(fig5, use_container_width=True)
st.plotly_chart(fig6, use_container_width=True)
st.plotly_chart(fig7, use_container_width=True)
st.plotly_chart(fig8, use_container_width=True)
st.plotly_chart(fig9, use_container_width=True)
st.plotly_chart(fig10, use_container_width=True)

# 4 Adjust layout
t1, t2, t3 = st.tabs(["Bivariate", "Trivariate", 'About'])
num_cols = df.select_dtypes(include=np.number).columns.tolist()

with t1:
    c1, c2 = st.columns(2)
    col1 = c1.radio("Select the first column for Scatter plot", num_cols)
    col2 = c2.radio("Select the second column for Scatter plot", num_cols)
    fig = px.scatter(df, x=col1, y=col2, title=f'{col1} vs {col2}')
    st.plotly_chart(fig, use_container_width=True)

with t2:
    c1, c2, c3 = st.columns(3)
    col1 = c1.selectbox("Select the first column for 3D plot", num_cols)
    col2 = c2.selectbox("Select the second column for 3D plot", num_cols)
    col3 = c3.selectbox("Select the third column for 3D plot", num_cols)
    fig = px.scatter_3d(df, x=col1, y=col2, z=col3, title=f'{col1} vs {col2} vs {col3}', height=700)
    st.plotly_chart(fig, use_container_width=True)

# About Section
with t3:
    st.title("About the App")
    st.write(
        """
        Welcome to the Stock Data App! This web application allows you to explore and visualize the Apple Stock Prices dataset.

        **Data Source:**
        The dataset used in this app contains historical stock prices for Apple Inc. The data includes information such as opening and closing prices, high and low prices, volume, and date.

        **Data Visualization:**
        The app provides various visualizations to help you analyze the stock data, including line charts, bar charts, scatter plots, histograms, box plots, and more. You can explore trends over time, relationships between different variables, and distribution of closing prices.

        **Bivariate and Trivariate Analysis:**
        The "Bivariate" and "Trivariate" tabs allow you to create scatter plots and 3D plots by selecting different columns from the dataset. This enables you to investigate relationships between specific numerical columns.

        **How to Use:**
        - In the "Bivariate" tab, choose two columns to generate a scatter plot.
        - In the "Trivariate" tab, select three columns to create a 3D scatter plot.

        **About the Developer:**
        This app is created using Streamlit, a powerful Python library for creating web applications with minimal code. If you have any questions or feedback, feel free to reach out to the developer.

        Enjoy exploring the Apple Stock Prices dataset!
        Created by: [Mohhammad Fazal]
        """
    )
