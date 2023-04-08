import streamlit as st
import pandas as pd

st.title('A Simple Streamlit Web App')
name = st.text_input('Enter your name', '')
st.write(f'Hello {name}!')
variable_х = st.slider('Select an integer x', 1, 100, 1)
variable_y = st.slider('Select an integer y', 1, 100, 1)
def sum(variable_х, variable_y):
   result = variable_х + variable_y
   return result
def subtract(variable_х, variable_y):
   result = variable_х - variable_y
   return result
def multiply(variable_х, variable_y):
   result = variable_х * variable_y
   return result
def divide(variable_х, variable_y:
   result = variable_х / variable_y
   return result
