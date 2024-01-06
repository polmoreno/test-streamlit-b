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
            "Choose GeneName", list(dataset_filtro.index.unique()), placeholder="e.g. A2M"
        )
        bioType = st.multiselect(
            "Choose BioType", list(dataset_filtro["BioType"].unique()), placeholder="e.g. rRNA"
        )
        low = st.multiselect(
            "Choose LOW", list(dataset_filtro["LOW"].unique()), placeholder="e.g. 1"
        )
        if not geneName and not bioType and not low:
            st.write(dataset_filtro)
        elif bioType and low:
            bioData = dataset_filtro.loc[dataset_filtro["BioType"].isin(bioType)]
            data = bioData.loc[bioData["LOW"].isin(low)]
            st.write(data)
        elif bioType:
            data = dataset_filtro.loc[dataset_filtro["BioType"].isin(bioType)]
            st.write(data)
        elif low:
            data = dataset_filtro.loc[dataset_filtro["LOW"].isin(low)]
            st.write(data)
        else:
            data = dataset_filtro.loc[geneName]
            if bioType and low:
                bioData = data.loc[data["BioType"].isin(bioType)]
                st.write(bioData.loc[bioData["LOW"].isin(low)])
            elif bioType:
                st.write(data.loc[data["BioType"].isin(bioType)])
            elif low:
                st.write(data.loc[data["LOW"].isin(low)])
            else:    
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