import streamlit as st
import pandas as pd
import string

st.set_page_config(page_title="All Cognates", page_icon="📖")

st.markdown("# All Cognates")
st.sidebar.header("All Cognates")
st.write(
    """Here are all cognates for German and Farsi.  
    `Ratio` is the similarity between the German word and the Farsi pronuciation.
    """
)

@st.cache
def get_cognates_data():
    path = 'data/german_farsi_cognates.csv'
    top_cognates = pd.read_csv(path)
    return top_cognates
    
cognates = get_cognates_data()

all_categories =    list(string.ascii_uppercase)
categories = st.sidebar.multiselect(
        "Choose categories", all_categories, all_categories
)

txt = st.sidebar.text_input('Search word')
# print(txt)
filtered_cognates =  cognates[cognates['src'].str.startswith(tuple(categories))].copy()

if txt and len(txt) > 1:
    filtered_cognates  = filtered_cognates[filtered_cognates['src'].str.contains(txt) ].copy()
st.write("### Cognates German / Farsi")
st.dataframe(filtered_cognates, use_container_width=True)

st.write(f"Found {len(filtered_cognates)} cognates.")