import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Top Cognates German/Farsi Streamlit Demo",
    page_icon="🧊",
)

@st.cache
def get_top_cognates_data():
    path = 'data/german_farsi_top_cognates.csv'
    top_cognates = pd.read_csv(path)
    return top_cognates

st.markdown("# German/Farsi Top Cognates")

st.markdown(
    """
    [Here](https://tim.blog/2014/03/21/how-to-learn-a-foreign-language-2) are some great tips from Tim Ferriss on how to learn new languages.  
    
    > Tipp #1: Learn the right words, the right way.  
    > **Tipp #2: Learn cognates: your friend in every single language**  
    > Tipp #3: Interact in your language daily without traveling.
    ...
    
    As I could not find a page that had all cognates for German/Persian, I build one.  
    
"""
)


    
top_cognates = get_top_cognates_data()

st.write("### Top Cognates German / Farsi")
st.table(top_cognates)