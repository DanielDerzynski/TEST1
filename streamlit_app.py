import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Tworzenie aplikacji tkinter
root = tk.Tk()
root.title("Wykres w Tkinter")

# Funkcja do tworzenia wykresu
def plot_graph():
    # Tworzenie danych do wykresu
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]

    # Tworzenie wykresu
    fig, ax = plt.subplots()
    ax.plot(x, y, label="Kwadrat", color="blue")
    ax.set_title("Wykres funkcji kwadratowej")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()

    # Rysowanie wykresu w tkinterze
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Tworzenie ramki w aplikacji tkinter
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

# Przycisk do rysowania wykresu
btn_plot = ttk.Button(frame, text="Rysuj wykres", command=plot_graph)
btn_plot.pack(pady=10)

# Uruchomienie głównej pętli aplikacji tkinter
root.mainloop()
