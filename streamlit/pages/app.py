import streamlit as st

# Import CSS

def local_css(styles):
    with open(styles) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("styles.css")

# --------------


st.html("<h1>The Rock'mendation</h1>")

st.html("<p>Bienvenu sur notre service de recommandation de films. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>")


# Sélectionner le film

choix_film = st.text_input("👇 Choisissez votre film")


if choix_film:
    selected_film = st.selectbox(
        "",
        choix_film,
        index=None,
        placeholder="Select")

    # Si mon film est sélectionné, j'affiche les suggestions 
    # dans le selecbox
    
    

    if selected_film:
        st.markdown("---")
        titre_film = selected_film

        html_str = f"""
            <h2 class="titre_film">🎬 {titre_film}</h2>
            <p class="caract_film">1990 - Drama</p>
        """

        st.markdown(html_str, unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.image("img/gladiator.jpg", use_container_width=True)

        # with col2:
        #     st.write("")

        with col2:
            st.html("<h3>⭐ Note : 5/5")

            st.html("<h3>🤵 Casting</h3>")

            st.html(
                "<ul>"
                    "<li>Nom acteur</li>"
                    "<li>Nom acteur</li>"
                    "<li>Nom acteur</li>"
                    "<li>Nom acteur</li>"
                    "<li>Nom acteur</li>"
                "</ul>"
            )

        st.html(
            "<h3>📑 Synopsis</h3>"

            "<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>"
        )

        st.markdown("---")

        st.html("<h2>🤙 Nos Rock'mendations</h2>")

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.image("img/gladiator.jpg", use_container_width=True)

            st.write("Titre de mon film")
            st.write("Note : 4/5")
            st.write("1990")

        with col2:
            st.image("img/gladiator.jpg", use_container_width=True)

            st.write("Titre de mon film")
            st.write("Note : 4/5")
            st.write("1990")

        with col3:
            st.image("img/gladiator.jpg", use_container_width=True)

            st.write("Titre de mon film")
            st.write("Note : 4/5")
            st.write("1990")

        with col4:
            st.image("img/gladiator.jpg", use_container_width=True)

            st.write("Titre de mon film")
            st.write("Note : 4/5")
            st.write("1990")

        with col5:
            st.image("img/gladiator.jpg", use_container_width=True)

            st.write("Titre de mon film")
            st.write("Note : 4/5")
            st.write("1990")
            



        





