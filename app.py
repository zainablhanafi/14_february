import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd
from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate
# Lire le fichier CSV
df_utilisateurs = pd.read_csv("Comptes_utilisateurs.csv")

dictionnaire_utilisateurs={"usernames" : {}}

#Boucle pour transformer le dataframe en dictionnaire, format pour Authenticate :

for i in range (len(df_utilisateurs)):
    #parcours les lignes du dataframe (itération sur le tableau)
    # - On peut utiliser: for cle, valeur  in df_utilisateurs:.iterrows()
    row= df_utilisateurs.iloc[i]
    #On choisit notre clé de notre premier dictionnaire
    identifiant = row["email"]
    #On remplit notre dictionnaire imbriquée pour l'utilisateur
    #On récupère la valeur de la colonne "name", "password", ... dans la ligne row
    dictionnaire_utilisateurs["usernames"][identifiant] = {
        "name" : row["name"] ,
        "password":row["password"]  ,
        "email" : row["email"],
        "failed_login_attempts" : row["failed_login_attempts"],
        "role" : row["role"],
    }
    
authenticator = Authenticate(
    dictionnaire_utilisateurs,  # Les données des comptes
    "cookie name",         # Le nom du cookie, un str quelconque
    "cookie key",          # La clé du cookie, un str quelconque
    30,                    # Le nombre de jours avant que le cookie expire
)

authenticator.login()

if st.session_state["authentication_status"]:
    with st.sidebar:
        selected = option_menu(None, ["Home",'14 February'],
        icons=['house',"heart"],
        menu_icon="cast", default_index=0, orientation="horizontal")


    if selected == "Home":
        st.title("Welcome to my little CHERRY BLOSSOM corner 💮!")
        st.write("""February 14 is called Valentine’s Day because it was named after Saint Valentine
                 He was a Christian priest in ancient Rome during the 3rd century. According to tradition, the Roman Emperor banned marriages for young soldiers, believing single men made better fighters. Valentine secretly performed weddings for couples in love. When the emperor found out, Valentine was arrested and later executed on February 14.
                 Over time, he was honored as a martyr, and his feast day became associated with love and romance. That’s why February 14 is called Valentine’s Day today. 💌""")
        st.image("image/30.jpeg")

    elif selected == "14 February":
        st.title("February calls for flowers! Here's my bouquet collection—hope it makes you smile 🙈")


        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            st.header("💮")
            st.image("image/2.jpeg")
        with col2:
            st.header("💮")
            st.image("image/1.jpeg")
        with col3:
            st.header("💮")
            st.image("image/3.jpeg")


        col4, col5, col6, col7, col8 = st.columns([1, 1, 2, 1, 1])
        with col4:
            st.header("💮")
            st.image("image/5.jpeg")
        with col5:
            st.header("💮")
            st.image("image/4.jpeg")
        with col6:
            st.header("💮")
            st.image("image/6.jpeg")
        with col7:
            st.header("💮")
            st.image("image/7.jpeg")
        with col8:
            st.header("💮")
            st.image("image/9.jpeg")

        # Troisième rangée
        col9, col10, col11 = st.columns([1, 2, 1])
        with col9:
            st.header("💮")
            st.image("image/8.jpeg")
        with col10:
            st.header("💮")
            st.image("image/11.jpeg")
        with col11:
            st.header("💮")
            st.image("image/10.jpeg")

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")

elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplis')
    st.write("log in :Cherrisblossom,Password :blahblahblah")