import streamlit as st

# Tytuł aplikacji
st.title("Aplikacja 'Kocham Zuzie'")

# Opis aplikacji
st.write("Naciśnij przycisk, aby wyświetlić komunikat.")

# Przycisk
if st.button("Kliknij mnie!"):
    st.success("Kocham Zuzie!")
