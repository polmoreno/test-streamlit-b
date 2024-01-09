from urllib.error import URLError

import pandas as pd
import streamlit as st

st.set_page_config(page_title="TEST #1 TFM")
st.markdown("# TEST #1 TFM")
st.sidebar.header("TEST #1 TFM")

def vcf_filtro_func():
    @st.cache_data
    def get_UN_data():
        st.write("#### VCF FILTRO:")
        vcf_filtro = pd.read_csv("./SNPEFF_VCF.csv")
        return vcf_filtro.set_index("#CHROM")

    try:
        vcf_filtro = get_UN_data()
        chrom = st.multiselect(
            "Choose CHROM", list(vcf_filtro.index.unique()), placeholder="e.g. chr15"
        )
        if not chrom:
            st.write(vcf_filtro)
        else:
            data = vcf_filtro.loc[chrom]
            st.write(data.sort_index())
    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**
            Connection error: %s
        """
            % e.reason
        )

def dataset_filtro_func():
    @st.cache_data
    def get_UN_data():
        st.write("#### DATASET FILTRO:")
        dataset_filtro = pd.read_csv("./DATA_VCF.csv")
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
        if not geneName:
            st.write(dataset_filtro)
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

vcf_filtro_func()
dataset_filtro_func()
