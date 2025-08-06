# main.py
from gui import HanoiGUI
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = HanoiGUI(root)
    root.mainloop()