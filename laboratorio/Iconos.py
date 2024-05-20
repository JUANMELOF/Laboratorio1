import tkinter as tk

def load_icons():
    iconos = {
        "play": tk.PhotoImage(file=r"icons\icon\control_play.png"),
        "pausa": tk.PhotoImage(file=r"icons\icon\control_pause_blue.png"),
        "stop": tk.PhotoImage(file=r"icons\icon\control_stop_blue.png"),
        "pasar": tk.PhotoImage(file=r"icons\icon\control_end_blue.png"),
        "devolver": tk.PhotoImage(file=r"icons\icon\control_start_blue.png"),
        "adelantar": tk.PhotoImage(file=r"icons\icon\control_fastforward_blue.png"),
        "retroceder": tk.PhotoImage(file=r"icons\icon\control_rewind_blue.png"),
        "satan": tk.PhotoImage(file=r"icons/icon/satanic.png"),
        "carpeta": tk.PhotoImage(file=r"icons\icon\folder.png")
    }
    return iconos
