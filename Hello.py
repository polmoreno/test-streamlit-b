# Importing necessary module for handling URL errors
from urllib.error import URLError

# Importing pandas for data manipulation and streamlit for building web applications
import pandas as pd
import streamlit as st

# Setting page configuration for the Streamlit app (wide mode, window title, page title and subheader)
st.set_page_config(page_title="TFM - Bernat Moreno Batlle", layout="wide")
st.markdown("# DISEÑO E IMPLEMENTACIÓN DE UN PIPELINE BIOINFORMÁTICO PARA ANÁLISIS GENÓMICO EN LA ASOCIACIÓN VACTERL")
st.subheader('Bernat Moreno Batlle')

# Adding a header to the sidebar
st.sidebar.header("TFM - Bernat Moreno Batlle")

# Defining a function for filtering and displaying the dataset "DATA_VCF.csv"
def dataset_filtro_func():
    # Caching the data to improve performance
    @st.cache_data
    def get_data():
        # Displaying the title
        st.write("#### Number of effects by impact and region:")
        # Reading the dataset from a CSV file
        dataset_filtro = pd.read_csv("./DATA_VCF.csv")
        return dataset_filtro.set_index("#GeneName")
    try:
        # Calling the cached function to get the dataset
        dataset_filtro = get_data()
        # Setting the ENSEMBL column with a link
        dataset_filtro["ENSEMBL"] = "https://www.ensembl.org/Homo_sapiens/Gene/Summary?db=core;g="+dataset_filtro["ENSEMBL"]
        # Providing user interface elements for selecting filters
        geneName = st.multiselect("Choose GeneName", list(dataset_filtro.index.unique()), placeholder="e.g. A2M")
        bioType = st.multiselect("Choose BioType", list(dataset_filtro["BioType"].unique()), placeholder="e.g. rRNA")
        high = list(dataset_filtro["HIGH"].unique())
        low = list(dataset_filtro["LOW"].unique())
        moderate = list(dataset_filtro["MODERATE"].unique())
        modifier = list(dataset_filtro["MODIFIER"].unique())
        # Styling for better UI presentation
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
        # Creating columns for buttons to display horizontally
        col1, col2, col3, col4 = st.columns([1,1,1,1])
        # Adding the buttons to each column
        with col1:
            highButton = st.button("HIGH")
        with col2:
            lowButton = st.button("LOW")
        with col3:
            moderateButton = st.button("MODERATE")
        with col4:
            modifierButton = st.button("MODIFIER")
        ifhigh = ["LOW", "MODERATE", "MODIFIER"]
        iflow = ["HIGH", "MODERATE", "MODIFIER"]
        ifmoderate = ["HIGH", "LOW", "MODIFIER"]
        ifmodifier = ["HIGH", "LOW", "MODERATE"]

        # Handling button clicks and filtering the data accordingly
        if highButton:
            data = dataset_filtro.loc[dataset_filtro["HIGH"].isin(high)]
            if bioType and highButton:
                bioData = dataset_filtro.loc[dataset_filtro["BioType"].isin(bioType)]
                # Updating the list of columns to exclude impact on the DataFrame 
                ifhigh = [col for col in bioData.columns if col not in ifhigh]
                # Making the ENSEMBL column clickable
                st.dataframe(
                        bioData[ifhigh],
                        column_config={
                            "ENSEMBL": st.column_config.LinkColumn("ENSEMBL", display_text="^https://www\.ensembl\.org/Homo_sapiens/Gene/Summary\?db=core;g=(.*?)$")
                        },
                    )
            else:
                ifhigh = [col for col in data.columns if col not in ifhigh]
                # Making the ENSEMBL column clickable
                st.dataframe(
                        data[ifhigh],
                        column_config={
                            "ENSEMBL": st.column_config.LinkColumn("ENSEMBL", display_text="^https://www\.ensembl\.org/Homo_sapiens/Gene/Summary\?db=core;g=(.*?)$")
                        },
                    )
        elif lowButton:
            data = dataset_filtro.loc[dataset_filtro["LOW"].isin(low)]
            if bioType and lowButton:
                bioData = dataset_filtro.loc[dataset_filtro["BioType"].isin(bioType)]
                # Updating the list of columns to exclude impact on the DataFrame 
                iflow = [col for col in bioData.columns if col not in iflow]
                # Making the ENSEMBL column clickable
                st.dataframe(
                        bioData[iflow],
                        column_config={
                            "ENSEMBL": st.column_config.LinkColumn("ENSEMBL", display_text="^https://www\.ensembl\.org/Homo_sapiens/Gene/Summary\?db=core;g=(.*?)$")
                        },
                    )
            else:
                iflow = [col for col in data.columns if col not in iflow]
                # Making the ENSEMBL column clickable
                st.dataframe(
                        data[iflow],
                        column_config={
                            "ENSEMBL": st.column_config.LinkColumn("ENSEMBL", display_text="^https://www\.ensembl\.org/Homo_sapiens/Gene/Summary\?db=core;g=(.*?)$")
                        },
                    )
        elif moderateButton:
            data = dataset_filtro.loc[dataset_filtro["MODERATE"].isin(moderate)]
            if bioType and moderateButton:
                bioData = dataset_filtro.loc[dataset_filtro["BioType"].isin(bioType)]
                # Updating the list of columns to exclude impact on the DataFrame 
                ifmoderate = [col for col in bioData.columns if col not in ifmoderate]
                # Making the ENSEMBL column clickable
                st.dataframe(
                        bioData[ifmoderate],
                        column_config={
                            "ENSEMBL": st.column_config.LinkColumn("ENSEMBL", display_text="^https://www\.ensembl\.org/Homo_sapiens/Gene/Summary\?db=core;g=(.*?)$")
                        },
                    )
            else:
                ifmoderate = [col for col in data.columns if col not in ifmoderate]
                # Making the ENSEMBL column clickable
                st.dataframe(
                        data[ifmoderate],
                        column_config={
                            "ENSEMBL": st.column_config.LinkColumn("ENSEMBL", display_text="^https://www\.ensembl\.org/Homo_sapiens/Gene/Summary\?db=core;g=(.*?)$")
                        },
                    )
        elif modifierButton:
            data = dataset_filtro.loc[dataset_filtro["MODIFIER"].isin(modifier)]
            if bioType and modifierButton:
                bioData = dataset_filtro.loc[dataset_filtro["BioType"].isin(bioType)]
                # Updating the list of columns to exclude impact on the DataFrame 
                ifmodifier = [col for col in bioData.columns if col not in ifmodifier]
                # Making the ENSEMBL column clickable
                st.dataframe(
                        bioData[ifmodifier],
                        column_config={
                            "ENSEMBL": st.column_config.LinkColumn("ENSEMBL", display_text="^https://www\.ensembl\.org/Homo_sapiens/Gene/Summary\?db=core;g=(.*?)$")
                        },
                    )
            else:
                ifmodifier = [col for col in data.columns if col not in ifmodifier]
                # Making the ENSEMBL column clickable
                st.dataframe(
                        data[ifmodifier],
                        column_config={
                            "ENSEMBL": st.column_config.LinkColumn("ENSEMBL", display_text="^https://www\.ensembl\.org/Homo_sapiens/Gene/Summary\?db=core;g=(.*?)$")
                        },
                    )
        else:
            if not geneName and not bioType:
                # Making the ENSEMBL column clickable
                st.dataframe(
                    dataset_filtro,
                    column_config={
                    "ENSEMBL": st.column_config.LinkColumn("ENSEMBL", display_text="^https://www\.ensembl\.org/Homo_sapiens/Gene/Summary\?db=core;g=(.*?)$")
                    },
                )
            elif bioType:
                data = dataset_filtro.loc[dataset_filtro["BioType"].isin(bioType)]
                # Making the ENSEMBL column clickable
                st.dataframe(
                    data,
                    column_config={
                    "ENSEMBL": st.column_config.LinkColumn("ENSEMBL", display_text="^https://www\.ensembl\.org/Homo_sapiens/Gene/Summary\?db=core;g=(.*?)$")
                    },
                )
            else:
                data = dataset_filtro.loc[geneName]
                if bioType:
                    st.write(data.loc[data["BioType"].isin(bioType)])
                else:    
                    # Making the ENSEMBL column clickable
                    st.dataframe(
                        data,
                        column_config={
                            "ENSEMBL": st.column_config.LinkColumn("ENSEMBL", display_text="^https://www\.ensembl\.org/Homo_sapiens/Gene/Summary\?db=core;g=(.*?)$")
                        },
                    )
    except URLError as e:
        # Displaying an error message if there is a URL connection error
        st.error(
            """
            **This demo requires internet access.**
            Connection error: %s
        """
            % e.reason
        )

# Defining a function for filtering and displaying the dataset "SNPEFF_VCF.csv"
def vcf_filtro_func():
    @st.cache_data
    def get_data():
        # Displaying the title
        st.write("#### Variant Details (VCF file):")
        # Reading the dataset from a CSV file
        vcf_filtro = pd.read_csv("./SNPEFF_VCF.csv")
        return vcf_filtro.set_index("#CHROM")

    try:
        # Calling the cached function to get the SNPEFF_VCF data
        vcf_filtro = get_data()
        # Setting the ENSEMBL column with a link
        vcf_filtro["ENSEMBL"] = "https://www.ensembl.org/Homo_sapiens/Location/View?r="+vcf_filtro.index+":"+vcf_filtro["POS"].apply(str)
        # Providing user interface elements for selecting filters
        chrom = st.multiselect(
            "Choose CHROM", list(vcf_filtro.index.unique()), placeholder="e.g. chr15"
        )
        # Handling CHROM selection and displaying the filtered data
        if not chrom:
            # Making the ENSEMBL column clickable
            st.dataframe(
                vcf_filtro,
                column_config={
                    "ENSEMBL": st.column_config.LinkColumn("ENSEMBL", display_text="Ubicación")
                },
            )
        else:
            data = vcf_filtro.loc[chrom]
            # Making the ENSEMBL column clickable
            st.dataframe(
                data,
                column_config={
                    "ENSEMBL": st.column_config.LinkColumn("ENSEMBL", display_text="Ubicación")
                },
            )
    except URLError as e:
        # Displaying an error message if there is a URL connection error
        st.error(
            """
            **This demo requires internet access.**
            Connection error: %s
        """
            % e.reason
        )

# Calling the functions to display the filtered datasets
dataset_filtro_func()
vcf_filtro_func()