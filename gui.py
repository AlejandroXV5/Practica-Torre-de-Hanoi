# gui.py
import tkinter as tk
from tkinter import messagebox
import time
import random
from game import HanoiGame
from ai_solver import AISolver
from utils import format_time, show_confirmation, show_results

# Constantes para evitar duplicación de literales
FONT_NAME = "Segoe UI"
MOUSE_CLICK_EVENT = "<Button-1>"

class HanoiGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Torres de Hanói - IA")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        self.root.configure(bg="#000000")

        # Paleta de colores
        self.colors = {
            "bg": "#000000",
            "fg": "#ffffff",
            "accent": "#f9e2af",
            "peg": "#89b4fa",
            "disk_base": ["#ff5733", "#33ff57", "#3357ff", "#f3ff33", "#ff33f3", "#33fff3", "#cba6f7", "#f5c2e7"]
        }

        # Canvas principal
        self.canvas = tk.Canvas(self.root, bg=self.colors["bg"], highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Variables del juego
        self.game = None
        self.solver = AISolver()
        self.selected_peg = None
        self.mode = None
        self.animation_speed = 500
        self.is_demo_running = False
        self.is_paused = False  # Control de pausa
        self.peg_highlight = None
        self.anim_id = None
        self.pause_btn_id = None  # Referencia al botón de pausa

        # Fuentes
        self.font_title = (FONT_NAME, 28, "bold")
        self.font_btn = (FONT_NAME, 14)

        # Bind de redimensionado
        self.root.bind("<Configure>", self.on_resize)
        self.show_menu()

    def on_resize(self, event):
        """Redibuja el tablero si la ventana cambia de tamaño"""
        if self.mode in ["player", "demo"] and self.game:
            self.draw_board()

    def create_rounded_button(self, x, y, width, height, text, command, bg_color, fg_color="white"):
        """Crea un botón con bordes redondeados usando Canvas"""
        radius = 15
        self.canvas.create_rectangle(x + radius, y, x + width - radius, y + height, fill=bg_color, outline="")
        self.canvas.create_rectangle(x, y + radius, x + width, y + height - radius, fill=bg_color, outline="")
        self.canvas.create_arc(x, y, x + 2 * radius, y + 2 * radius, start=90, extent=90, style="pieslice", fill=bg_color)
        self.canvas.create_arc(x + width - 2 * radius, y, x + width, y + 2 * radius, start=0, extent=90, style="pieslice", fill=bg_color)
        self.canvas.create_arc(x, y + height - 2 * radius, x + 2 * radius, y + height, start=180, extent=90, style="pieslice", fill=bg_color)
        self.canvas.create_arc(x + width - 2 * radius, y + height - 2 * radius, x + width, y + height, start=270, extent=90, style="pieslice", fill=bg_color)
        btn_id = self.canvas.create_text(x + width // 2, y + height // 2, text=text, font=self.font_btn, fill=fg_color)
        self.canvas.tag_bind(btn_id, MOUSE_CLICK_EVENT, lambda e: command())
        return btn_id

    def show_menu(self):
        """Muestra el menú principal"""
        self.canvas.delete("all")
        self.selected_peg = None
        self.mode = None
        self.is_demo_running = False
        self.is_paused = False
        w = max(self.canvas.winfo_width(), 900)
        h = max(self.canvas.winfo_height(), 700)
        self.canvas.create_text(w // 2, h // 3, text="TORRES DE HANÓI", font=self.font_title, fill=self.colors["accent"])
        self.canvas.create_text(w // 2, h // 3 + 50, text="Inteligencia Artificial", font=(FONT_NAME, 16), fill=self.colors["fg"])
        self.create_rounded_button(w // 2 - 100, h // 2, 200, 50, "Jugar", self.ask_difficulty, "#a6e3a1")
        self.create_rounded_button(w // 2 - 100, h // 2 + 70, 200, 50, "Demostración", lambda: self.ask_difficulty("demo"), "#f9e2af")
        self.create_rounded_button(w // 2 - 100, h // 2 + 140, 200, 50, "Salir", self.root.quit, "#f38ba8")

    def ask_difficulty(self, mode="player"):
        """Pantalla de selección de dificultad"""
        self.canvas.delete("all")
        self.mode = mode
        w = max(self.canvas.winfo_width(), 900)
        h = max(self.canvas.winfo_height(), 700)
        self.canvas.create_text(w // 2, h // 3 - 100, text="Selecciona Dificultad", font=self.font_title, fill=self.colors["accent"])
        self.create_rounded_button(w // 2 - 100, h // 2 - 50, 200, 50, "3 discos (Fácil)", lambda: self.start_game(3), "#a6e3a1")
        self.create_rounded_button(w // 2 - 100, h // 2 + 20, 200, 50, "6 discos (Medio)", lambda: self.start_game(6), "#f9e2af")
        self.create_rounded_button(w // 2 - 100, h // 2 + 90, 200, 50, "8 discos (Difícil)", lambda: self.start_game(8), "#f38ba8")
        back_id = self.canvas.create_text(w // 2, h // 2 + 180, text="← Regresar", font=(FONT_NAME, 12), fill="#89b4fa")
        self.canvas.tag_bind(back_id, MOUSE_CLICK_EVENT, lambda e: self.show_menu())

    def start_game(self, num_discs):
        """Inicia el juego con el número de discos"""
        self.game = HanoiGame(num_discs)
        self.game.is_running = True
        self.game.start_time = time.time()
        self.selected_peg = None
        self.is_demo_running = True
        self.is_paused = False
        self.canvas.delete("all")
        self.canvas.unbind(MOUSE_CLICK_EVENT)
        self.canvas.bind(MOUSE_CLICK_EVENT, self.on_click)
        self.root.bind("<Escape>", self.ask_exit_game_or_demo)
        self.root.bind("<space>", lambda e: self.toggle_pause())  # Pausa con espacio
        if self.mode == "demo":
            self.run_ai_demo(num_discs)
        else:
            self.draw_board()

    def draw_board(self):
        """Dibuja el tablero y el botón de pausa si está en modo demo"""
        self.canvas.delete("all")
        w = max(self.canvas.winfo_width(), 900)
        h = max(self.canvas.winfo_height(), 700)
        base_y = h * 0.8
        disk_height = 25
        self.pegs_x = [w * 0.2, w * 0.5, w * 0.8]

        # Suelo marrón
        self.canvas.create_rectangle(0, base_y + 10, w, h, fill="#8b4513", outline="#654321")

        # Torres (varillas)
        for x in self.pegs_x:
            self.canvas.create_rectangle(x - 8, base_y - 5, x + 8, base_y, fill="#647d94", outline="")
            self.canvas.create_line(x, h * 0.25, x, base_y - 5, width=8, fill=self.colors["peg"], capstyle="round")

        # Dibujar discos
        for i, peg in enumerate(self.game.pegs):
            for j, disk_size in enumerate(peg):
                width = disk_size * (w // 40)
                y = base_y - (j + 1) * disk_height
                color = self.colors["disk_base"][(disk_size - 1) % len(self.colors["disk_base"])]
                self.canvas.create_rectangle(
                    self.pegs_x[i] - width, y,
                    self.pegs_x[i] + width, y + disk_height,
                    fill=color, outline="white", width=2
                )

        # Información de juego
        if self.game and self.game.is_running:
            elapsed = time.time() - self.game.start_time
            self.canvas.create_text(20, 20, anchor="nw", text=f"🎯 Movimientos: {self.game.moves}",
                                    font=(FONT_NAME, 12, "bold"), fill=self.colors["fg"])
            self.canvas.create_text(20, 50, anchor="nw", text=f"⏱️ Tiempo: {format_time(elapsed)}",
                                    font=(FONT_NAME, 12, "bold"), fill=self.colors["accent"])

        # Botón de Pausa/Continuar (solo en modo demo)
        if self.mode == "demo" and self.is_demo_running:
            btn_text = "⏸️ Pausa" if not self.is_paused else "▶️ Continuar"
            x, y = w - 120, 20
            if self.pause_btn_id:
                self.canvas.delete(self.pause_btn_id)
            self.pause_btn_id = self.canvas.create_text(
                x, y,
                text=btn_text,
                font=(FONT_NAME, 12, "bold"),
                fill="#f38ba8",
                activefill="#cba6f7",
                tags="pause_btn"
            )
            self.canvas.tag_bind("pause_btn", MOUSE_CLICK_EVENT, lambda e: self.toggle_pause())

    def on_click(self, event):
        """Maneja el clic del jugador"""
        if not self.game or self.mode != "player":
            return

        w = self.canvas.winfo_width()
        for i, x in enumerate(self.pegs_x):
            if x - 60 < event.x < x + 60 and event.y < 550:
                if self.selected_peg is None:
                    if len(self.game.pegs[i]) > 0:
                        self.selected_peg = i
                        self.highlight_selected_peg(i)
                else:
                    if self.selected_peg != i:
                        if self.is_valid_move(self.selected_peg, i):
                            if self.game.move(self.selected_peg, i):
                                self.animate_move(self.selected_peg, i)
                                if self.game.is_solved():
                                    self.show_completion_popup()
                            self.clear_selection()
                        else:
                            self.show_invalid_move_feedback(i)
                    else:
                        self.clear_selection()
                break

    def highlight_selected_peg(self, peg_index):
        """Resalta visualmente la torre seleccionada"""
        x = self.pegs_x[peg_index]
        self.peg_highlight = self.canvas.create_rectangle(
            x - 70, 10, x + 70, 60, outline="yellow", width=3, dash=(5, 5)
        )

    def clear_selection(self):
        """Limpia la selección actual"""
        self.selected_peg = None
        self.canvas.delete(self.peg_highlight)
        self.peg_highlight = None

    def is_valid_move(self, from_peg, to_peg):
        """Verifica si un movimiento es válido"""
        if not self.game.pegs[from_peg]:
            return False
        if self.game.pegs[to_peg] and self.game.pegs[to_peg][-1] < self.game.pegs[from_peg][-1]:
            return False
        return True

    def show_invalid_move_feedback(self, peg_index):
        """Muestra retroalimentación visual para movimientos inválidos"""
        x = self.pegs_x[peg_index]
        invalid_highlight = self.canvas.create_rectangle(
            x - 70, 10, x + 70, 60, outline="red", width=3, dash=(5, 5)
        )
        self.root.after(500, lambda: self.canvas.delete(invalid_highlight))

    def animate_move(self, from_peg, to_peg):
        """Animación mejorada del movimiento de un disco"""
        if len(self.game.pegs[from_peg]) == 0:
            print("Error: intento de animar movimiento desde torre vacía")
            return

        w = max(self.canvas.winfo_width(), 900)
        h = max(self.canvas.winfo_height(), 700)
        base_y = h * 0.8
        disk_height = 25
        disk_size = self.game.pegs[to_peg][-1]  # Disco que acaba de moverse
        width = disk_size * (w // 40)
        from_x = self.pegs_x[from_peg]
        to_x = self.pegs_x[to_peg]
        start_y = base_y - len(self.game.pegs[from_peg]) * disk_height
        end_y = base_y - len(self.game.pegs[to_peg]) * disk_height

        temp_disk = self.canvas.create_rectangle(
            from_x - width, start_y, from_x + width, start_y + disk_height,
            fill=self.colors["disk_base"][(disk_size - 1) % len(self.colors["disk_base"])],
            outline="white", width=2
        )

        total_steps = 50  # Más pasos para mayor fluidez
        dx = (to_x - from_x) / total_steps
        dy = (end_y - start_y) / total_steps
        arc_height = 150  # Altura máxima del arco

        def step(step_num):
            if step_num >= total_steps:
                self.canvas.delete(temp_disk)
                self.draw_board()  # Redibuja el tablero después de la animación
                return

            t = step_num / total_steps
            x = from_x + dx * step_num
            y = start_y + dy * step_num - arc_height * (4 * t * (1 - t))  # Movimiento parabólico
            self.canvas.coords(temp_disk, x - width, y, x + width, y + disk_height)
            self.anim_id = self.root.after(15, lambda: step(step_num + 1))  # Intervalo más corto

        step(0)

    def run_ai_demo(self, num_discs):
        """Inicia la demostración automática"""
        self.is_demo_running = True
        self.is_paused = False
        self.route, demo_num = self.solver.get_next_route(num_discs)
        self.current_index = 0
        self.game = HanoiGame(num_discs)
        self.game.is_running = True
        self.game.start_time = time.time()

        w = self.canvas.winfo_width()
        self.canvas.create_text(w // 2, 40, text=f"Demostración #{demo_num}", font=(FONT_NAME, 18, "bold"),
                                fill=self.colors["accent"])
        self.draw_board()
        self.execute_route_step(self.route, 0)

    def execute_route_step(self, route, index):
        """Ejecuta un paso del algoritmo IA"""
        if not self.is_demo_running:
            return

        # Guardamos estado para poder reanudar
        self.route = route
        self.current_index = index

        if index >= len(route):
            elapsed = time.time() - self.game.start_time
            time_str = format_time(elapsed)
            if show_results("Demostración", self.game.num_discs, self.game.moves, time_str, demo_num=index + 1):
                self.show_menu()
            else:
                self.root.quit()
            return

        if self.is_paused:
            return  # Si está pausado, no continuar

        from_peg, to_peg = route[index]
        if self.game.move(from_peg, to_peg):
            self.animate_move(from_peg, to_peg)
            self.root.after(self.animation_speed, self.execute_route_step, route, index + 1)

    def toggle_pause(self):
        """Alterna entre pausa y continuar"""
        if not self.is_demo_running:
            return

        self.is_paused = not self.is_paused
        self.update_pause_button()

        if not self.is_paused:
            # Reanudar desde el índice actual
            self.root.after(self.animation_speed, self.execute_route_step, self.route, self.current_index)

    def update_pause_button(self):
        """Actualiza el texto del botón de pausa"""
        if not self.pause_btn_id or self.mode != "demo":
            return

        btn_text = "⏸️ Pausa" if not self.is_paused else "▶️ Continuar"
        self.canvas.itemconfig(self.pause_btn_id, text=btn_text)

    def ask_exit_game_or_demo(self, event=None):
        """Permite salir con confirmación"""
        if self.is_demo_running:
            if show_confirmation("Salir", "¿Desea salir al menú principal?"):
                self.is_demo_running = False
                if self.anim_id:
                    self.root.after_cancel(self.anim_id)
                self.show_menu()

    def show_completion_popup(self):
        """Muestra mensaje al completar el nivel"""
        if not self.game or not self.game.is_running:
            return

        elapsed = time.time() - self.game.start_time
        time_str = format_time(elapsed)

        if show_results("Jugador", self.game.num_discs, self.game.moves, time_str):
            self.show_menu()
        else:
            self.root.quit()

    def run(self):
        """Inicia el bucle principal de la GUI"""
        self.root.mainloop()