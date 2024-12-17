import streamlit as st

# Import CSS

def local_css(styles):
    with open(styles) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("styles.css")

st.title("Les chiffres clés")

st.markdown("""

    ## 📊 KPI 1 : Les acteurs bla bla bla...
            
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
            
            """)

st.image("img/graph.png", caption="Graphique")

# KPI2

st.markdown("""

    ## 📊 KPI 2 : L'age moyen bla bla bla...
            
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
            
            """)

st.image("img/graph.png", caption="Graphique")
