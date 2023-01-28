import streamlit as st
import pandas as pd

st.title('A Simple Streamlit Web App')
name = st.text_input('Enter your name', '')
st.write(f'Hello {name}!')
x = st.slider('Select an integer X', 1, 100, 1)
y = st.slider('Select an integer Y', 1, 100, 1)
df = pd.DataFrame({'Сложение': [x + y], 'Вычитание': [x - y], 'Умножение': [x * y], 'Деление': [round(x / y, 2)]}, index=['Результат'])
st.write(df)
