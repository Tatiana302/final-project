import streamlit as st
import pandas as pd

# Заголовок страницы
st.title("A Simple Streamlit Web App")

# Получение имени пользователя и вывод приветствия
name = st.text_input("Enter your name", "")
st.write(f"Hello {name}!")

# Получение значений слайдеров и создание DataFrame
x = st.slider("Select an integer X", 1, 100, 1)
y = st.slider("Select an integer Y", 1, 100, 1)
result = {"Сложение": x+y, "Вычитание": x-y, "Умножение": x*y, "Деление": round(x/y,2)}
df = pd.DataFrame(result, index=["Результат"])

# Вывод DataFrame
st.write(df)
