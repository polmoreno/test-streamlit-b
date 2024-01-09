import streamlit as st
import pandas as pd
import numpy as np

#st.title('Test 1 TFM')
#
#DATA_URL = './DATASET_FILTRO.csv'
#
#@st.cache_data
#def load_data(nrows):
#    data = pd.read_csv(DATA_URL, nrows=nrows)
#    lowercase = lambda x: str(x).lower()
#    data.rename(lowercase, axis='columns', inplace=True)
#    return data
#
#data_load_state = st.text('Loading data...')
#data = load_data(10000)
#data_load_state.text("Done!")
#
#if st.checkbox('Show raw data'):
#    st.subheader('Raw data')
#    st.write(data)

#st.markdown("""
#            <style>
#
#                 div[data-testid="column"] {
#                    width: fit-content !important;
#                    flex: unset;
#                }
#                div[data-testid="column"] * {
#                    width: fit-content !important;
#                }
#            </style>
#            """, unsafe_allow_html=True)
#
#col1, col2, col3 = st.columns([1,1,1])
#
#with col1:
#    if st.button('1'):
#        st.write("test")
#    else:
#        st.write("no")
#with col2:
#    st.button('2')
#with col3:
#    st.button('3')


def get_UN_data():
        st.write("#### DATASET FILTRO:")
        dataset_filtro = pd.read_csv("./DATA_VCF.csv")
        return dataset_filtro.set_index("#GeneName")
df = get_UN_data()

columns = st.multiselect("Columns:",df.columns)
filter = st.radio("Choose by:", ("inclusion","exclusion"))

if filter == "exclusion":
    columns = [col for col in df.columns if col not in columns]

df[columns]