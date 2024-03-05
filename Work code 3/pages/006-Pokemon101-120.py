import streamlit as st

with st.container():
    with st.container():
        c1, c2 ,c3 = st.columns(3)
        with c1:
                st.image('pokemon_image01/001_Fushigidane.png', width=200)
                st.link_button("Fushigidane", "https://www.serebii.net/pokemon/bulbasaur/")
        with c2:
                st.image('pokemon_image01/002_Fushigisou.png', width=200)
                st.link_button("Fushigisou", "https://www.serebii.net/pokemon/ivysaur/")
        with c3:
                st.image('pokemon_image01/003_Fushigibana.png', width=200)
                st.link_button("Fushigibana", "https://www.serebii.net/pokemon/venusaur/")
                
        c4,c5,c6 = st.columns(3)
        with c4:
                st.image('pokemon_image01/004_Hitokage.png', width=200)
                st.link_button("Hitokage", "https://www.serebii.net/pokemon/venusaur/")
        with c5:
                st.image('pokemon_image01/005_Lizardo.png', width=200)
                st.link_button("Lizardo", "https://www.serebii.net/pokemon/venusaur/")
        with c6:
                st.image('pokemon_image01/006_Dracaufeu.png', width=200)
                st.link_button("Lizardon", "https://www.serebii.net/pokemon/venusaur/")