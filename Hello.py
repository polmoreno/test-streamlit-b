from urllib.error import URLError

import pandas as pd
import streamlit as st

st.set_page_config(page_title="TFM - Bernat Moreno Batlle")
st.markdown("# DISEÑO E IMPLEMENTACIÓN DE UN PIPELINE BIOINFORMÁTICO PARA ANÁLISIS GENÓMICO EN LA ASOCIACIÓN VACTERL")
st.subheader('Bernat Moreno Batlle')

st.sidebar.header("TFM - Bernat Moreno Batlle")

def dataset_filtro_func():
    @st.cache_data
    def get_UN_data():
        st.write("#### Number of effects by impact and region:")
        dataset_filtro = pd.read_csv("./DATA_VCF.csv")
        return dataset_filtro.set_index("#GeneName")
    try:
        dataset_filtro = get_UN_data()
        geneName = st.multiselect("Choose GeneName", list(dataset_filtro.index.unique()), placeholder="e.g. A2M")
        bioType = st.multiselect("Choose BioType", list(dataset_filtro["BioType"].unique()), placeholder="e.g. rRNA")
        st.markdown("""
            <style>
                div[data-testid="column"] {
                    width: fit-content !important;
                    flex: unset;
                }
                div[data-testid="column"] * {
                    width: fit-content !important;
                }
            </style>
            """, unsafe_allow_html=True)
        #highButton, lowButton, moderateButton, modifierButton = st.columns([1,1,1,1])
        ifhigh = ["LOW", "MODERATE", "MODIFIER"]
        iflow = ["HIGH", "MODERATE", "MODIFIER"]
        ifmoderate = ["HIGH", "LOW", "MODIFIER"]
        ifmodifier = ["HIGH", "LOW", "MODERATE"]
      
        high = list(dataset_filtro["HIGH"].unique())
        low = list(dataset_filtro["LOW"].unique())
        moderate = list(dataset_filtro["MODERATE"].unique())
        modifier = list(dataset_filtro["MODIFIER"].unique())
        
        highButton = st.button("HIGH")
        lowButton = st.button("LOW")
        moderateButton = st.button("MODERATE")
        modifierButton = st.button("MODIFIER")

        if highButton:
            data = dataset_filtro.loc[dataset_filtro["HIGH"].isin(high)]
            if bioType and highButton:
                bioData = dataset_filtro.loc[dataset_filtro["BioType"].isin(bioType)]
                ifhigh = [col for col in bioData.columns if col not in ifhigh]
                bioData[ifhigh]
            else:
                ifhigh = [col for col in data.columns if col not in ifhigh]
                data[ifhigh]
        elif lowButton:
            data = dataset_filtro.loc[dataset_filtro["LOW"].isin(low)]
            if bioType and lowButton:
                bioData = dataset_filtro.loc[dataset_filtro["BioType"].isin(bioType)]
                iflow = [col for col in bioData.columns if col not in iflow]
                bioData[iflow]
            else:
                iflow = [col for col in data.columns if col not in iflow]
                data[iflow]
        elif moderateButton:
            data = dataset_filtro.loc[dataset_filtro["MODERATE"].isin(moderate)]
            if bioType and moderateButton:
                bioData = dataset_filtro.loc[dataset_filtro["BioType"].isin(bioType)]
                ifmoderate = [col for col in bioData.columns if col not in ifmoderate]
                bioData[ifmoderate]
            else:
                ifmoderate = [col for col in data.columns if col not in ifmoderate]
                data[ifmoderate]
        elif modifierButton:
            data = dataset_filtro.loc[dataset_filtro["MODIFIER"].isin(modifier)]
            if bioType and modifierButton:
                bioData = dataset_filtro.loc[dataset_filtro["BioType"].isin(bioType)]
                ifmodifier = [col for col in bioData.columns if col not in ifmodifier]
                bioData[ifmodifier]
            else:
                ifmodifier = [col for col in data.columns if col not in ifmodifier]
                data[ifmodifier]
        else:
            if not geneName and not bioType:
                st.write(dataset_filtro)
            elif bioType:
                data = dataset_filtro.loc[dataset_filtro["BioType"].isin(bioType)]
                st.write(data)
            else:
                data = dataset_filtro.loc[geneName]
                if bioType:
                    st.write(data.loc[data["BioType"].isin(bioType)])
                else:    
                    st.write(data.sort_index())
                    geneId = data["GeneId"].iloc[0]
                    st.link_button("See on Ensembl", f"https://www.ensembl.org/Multi/Search/Results?q={geneId}")
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
        st.write("#### Variant Details (VCF file):")
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

dataset_filtro_func()
vcf_filtro_func()