import tkinter as tk
from tkinter import messagebox

def hallo_sagen():
    messagebox.showinfo(
        "Begrüßung",
        "Hallo Welt!"
    )

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hallo Tkinter!")
    root.geometry("500x200")

    button = tk.Button(
        root,
        text="Drück mich!",
        command=hallo_sagen

    )
    button.pack()

    root.mainloop()