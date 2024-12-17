import streamlit as st
# from st_pages import Page, show_pages

# # add_page_title()

# show_pages(
#     [ 
#         Page("The-rockommendation/streamlit/index.py", "Home", "💾"),
#         # Page("About.py", "About", "📜"),
#         # Page("FAQ.py", "FAQ", "❔"),
#         # Page("Contact.py", "Contact", "💌") 
#     ]
# )

# Import CSS

def local_css(styles):
    with open(styles) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("styles.css")

st.html("<h1>The Rock'ommendation <br> <span>Le projet</span></h1>")
st.markdown("---")

st.html(
    "<p>Notre équipe de Data Analyst a été mandaté par un cinéma dans la Creuse qui se trouve en difficulté voulant passer le cap du digital.</p>"
)

st.html(
    "<h2>🚀 Objectifs et enjeux :</h2>"
)

st.html(

    "<ol>"
        "<li>Réaliser une <a href='https://google.fr' target='_blank'>étude de marché</a> sur la consommation de cinéma dans la région.</li>"
        "<li>Mettre en avant certains chiffres clés (KPI) comme les acteurs les plus présents, l'âge moyen des acteurs...</li>"
        "<li>Créer une application de recommandation de film en fonction des appréciations du spectateur.</li>"
    "</ol>"
)


st.html(
    "<h2>⚙️ Stack technique : </h2>"
)

col1, col2 = st.columns(2)

with col1: 
    st.html("<h3>Python</h3>")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png")

    st.html("<h3>Pandas</h3>")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSu9xFbA6COOd9Wq-koFEoAFD7wpFgbvdz6Q&s")

with col2:
    st.html("<h3>Scikit Learn</h3")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT3ioErrXCaT2yZgsMaefs8irg9dRTWVk882Q&s")

    st.html("<h3>Streamlit</h3>")
    st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-lighttext.png")
