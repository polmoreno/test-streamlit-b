from urllib.error import URLError

import pandas as pd
import streamlit as st

st.set_page_config(page_title="TEST #1 TFM")
st.markdown("# TEST #1 TFM")
st.sidebar.header("TEST #1 TFM")

def dataset_filtro_func():
    @st.cache_data
    def get_UN_data():
        st.write("#### DATASET FILTRO:")
        dataset_filtro = pd.read_csv("./DATASET_FILTRO.csv")
        return dataset_filtro.set_index("#GeneName")

    try:
        dataset_filtro = get_UN_data()
        geneName = st.multiselect(
            "Choose GeneName", list(dataset_filtro.index), placeholder="e.g. A2M"
        )
        if not geneName:
            st.write(dataset_filtro)
        else:
            data = dataset_filtro.loc[geneName]
            st.write(data.sort_index())
            geneId= data["GeneId"].iloc[0]
            st.link_button("See on Ensembl", f"https://www.ensembl.org/Multi/Search/Results?q={geneId}")
    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**
            Connection error: %s
        """
            % e.reason
        )

dataset_filtro_func()

#selected_reward = st.selectbox("Choose a reward", df.Item, 0)
#selected_reward_price = df.loc[df.Item == selected_reward]["Price (Coins)"].iloc[0]
#st.write(f'Price: {selected_reward_price}')