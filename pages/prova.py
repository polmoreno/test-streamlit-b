import streamlit as st
import pandas as pd


df = pd.DataFrame({'Item': ['Bagel', 'Coffee', 'Smart TV'], 'Price (Coins)': [125, 110, 7000]})

st.table(df)

selected_reward = st.selectbox("Choose a reward", df.Item, 0)

selected_reward_price = df.loc[df.Item == selected_reward]["Price (Coins)"].iloc[0]

st.write(f'Price: {selected_reward_price}')