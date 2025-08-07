import tkinter.messagebox as messagebox

def format_time(seconds):
    """Formatea el tiempo en minutos y segundos"""
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes:02d}:{seconds:02d}"

def show_confirmation(title, message):
    """Muestra un cuadro de diálogo de confirmación"""
    return messagebox.askyesno(title, message)

def show_results(mode, num_discs, moves, time_str, demo_num=None):
    """Muestra los resultados del juego"""
    message = f"Modo: {mode}\n"
    if demo_num:
        message += f"Demostración #{demo_num}\n"
    message += (
        f"Discos: {num_discs}\n"
        f"Movimientos: {moves}\n"
        f"Tiempo: {time_str}\n\n"
        "¿Desea volver al menú principal?"
    )
    return messagebox.askyesno("Resultados", message)