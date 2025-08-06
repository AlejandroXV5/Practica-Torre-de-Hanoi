# utils.py
import time
from tkinter import messagebox

def format_time(seconds):
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{mins:02d}:{secs:02d}"

def show_confirmation(title, message):
    return messagebox.askyesno(title, message)

def show_results(mode, level, moves, time_str, demo_num=None):
    msg = f"Modo: {mode}\nNivel: {level} discos\nMovimientos: {moves}\nTiempo: {time_str}"
    if demo_num:
        msg += f"\nDemostración #: {demo_num}"
    msg += "\n\n¿Volver al menú principal?"
    return messagebox.askyesno("Juego Finalizado", msg)