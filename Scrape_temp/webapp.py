import streamlit as st
import plotly.express as px
import sqlite3

connection = sqlite3.connect("tempdata.db")
cursor = connection.cursor()

cursor.execute("SELECT date FROM temperature_data")
date = cursor.fetchall()
date = [item[0] for item in date]

cursor.execute("SELECT temperature FROM temperature_data")
temperature = cursor.fetchall()
temperature = [item[0] for item in temperature]

figure = px.line(x=date, y=temperature,
                             labels={"x": "Date", "y": "Temperature (C)"})

st.plotly_chart(figure)