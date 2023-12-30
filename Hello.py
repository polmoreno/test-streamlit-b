from urllib.error import URLError

import altair as alt
import pandas as pd

import streamlit as st
from streamlit.hello.utils import show_code

st.set_page_config(page_title="TEST #1 TFM", page_icon="📊")
st.markdown("# TEST #1 TFM")
st.sidebar.header("TEST #1 TFM")


def dataset_filtro_func():
    @st.cache_data
    def get_UN_data():
        st.write("#### DATASET FILTRO:")
        dataset_filtro = pd.read_csv("./DATASET_FILTRO.csv")
        return dataset_filtro.set_index("GeneId")

    try:
        dataset_filtro = get_UN_data()
        geneid = st.multiselect(
            "Choose GeneID", list(dataset_filtro.index), placeholder="e.g. ENSG00000274059"
        )
        if not geneid:
            st.write(dataset_filtro)
        else:
            data = dataset_filtro.loc[geneid]
            st.write(data.sort_index())
    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**
            Connection error: %s
        """
            % e.reason
        )

def vcf_filtro_func():
    @st.cache_data
    def get_UN_data():
        st.write("#### VCF FILTRO:")
        vcf_filtro = pd.read_csv("./VCF_FILTRO.csv")
        return vcf_filtro.set_index("#CHROM")

    try:
        vcf_filtro = get_UN_data()
        chrom = st.multiselect(
            "Choose CHROM", list(vcf_filtro.index), ["chr15", "chr16"]
        )
        if not chrom:
            st.error("Please select at least one CHROM.")
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


dataset_filtro_func()
vcf_filtro_func()