import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import datetime

# Tytuł aplikacji
st.title('Interaktywne rysowanie figur geometrycznych')

# Dodajemy suwak do wyboru figury
figure_choice = st.slider('Wybierz figurę: 1 - Trójkąt, 2 - Koło, 3 - Kwadrat', min_value=1, max_value=3, value=1)

# Dodajemy okienko tekstowe do wprowadzania tekstu
text_input = st.text_input('Wpisz tekst do wyświetlenia w figurze:', '')

# Pobieramy aktualny czas
current_time = datetime.datetime.now().strftime('%H:%M:%S')

# Wyświetlamy godzinę w aplikacji
st.write(f"Aktualna godzina: {current_time}")

# Tworzymy wykres
fig, ax = plt.subplots()

# Ustawienia tła wykresu na niebieskie
fig.patch.set_facecolor('skyblue')  # Kolor tła figury wykresu (obszaru)
ax.set_facecolor('skyblue')  # Kolor tła samego obszaru wykresu

# Ustawienia osi
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.axis('off')  # Ukrywamy osie

# Rysowanie figury w zależności od wyboru suwaka
if figure_choice == 1:  # Trójkąt
    # Współrzędne wierzchołków trójkąta
    triangle_x = [-1, 1, 0]
    triangle_y = [-1, -1, 1]
    ax.fill(triangle_x, triangle_y, color='blue', label='Trójkąt')
    ax.plot(triangle_x + [triangle_x[0]], triangle_y + [triangle_y[0]], color='black')
    # Wyświetlanie tekstu w środku trójkąta
    ax.text(0, 0, text_input, color='white', ha='center', va='center', fontsize=12)
elif figure_choice == 2:  # Koło
    # Parametry koła
    circle = plt.Circle((0, 0), 1, color='red', label='Koło', fill=True)
    ax.add_artist(circle)
    # Wyświetlanie tekstu w środku koła
    ax.text(0, 0, text_input, color='white', ha='center', va='center', fontsize=12)
elif figure_choice == 3:  # Kwadrat
    # Współrzędne wierzchołków kwadratu
    square_x = [-1, 1, 1, -1, -1]
    square_y = [-1, -1, 1, 1, -1]
    ax.fill(square_x, square_y, color='green', label='Kwadrat')
    ax.plot(square_x, square_y, color='black')
    # Wyświetlanie tekstu w środku kwadratu
    ax.text(0, 0, text_input, color='white', ha='center', va='center', fontsize=12)

# Wyświetlanie rysunku
st.pyplot(fig)
