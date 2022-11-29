import streamlit as st
import pandas as pd
import numpy as np
df = pd.read_csv("football_data.csv")
clubs = st.multiselect('Show Player for clubs?', df['Club'].unique())
nationalities = st.multiselect('Show Player from Nationalities?', df['Nationality'].unique())
# Filter dataframe
new_df = df[(df['Club'].isin(clubs)) & (df['Nationality'].isin(nationalities))]
# write dataframe to screen
st.write(new_df)