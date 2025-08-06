# gui.py
import tkinter as tk
from tkinter import messagebox
import time
from game import HanoiGame
from ai_solver import AISolver
from utils import format_time, show_confirmation, show_results

class HanoiGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Torres de Hanói - IA")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.game = None
        self.solver = AISolver()
        self.selected_peg = None
        self.mode = None
        self.animation_speed = 500  # ms por movimiento en demo
        self.is_demo_running = False

        self.show_menu()

    def show_menu(self):
        self.canvas.delete("all")
        self.selected_peg = None
        self.mode = None

        tk.Label(self.canvas, text="TORRES DE HANÓI", font=("Arial", 24, "bold")).place(relx=0.5, rely=0.2, anchor="center")
        btn_play = tk.Button(self.canvas, text="Jugar", font=("Arial", 16), width=15, command=self.ask_difficulty)
        btn_demo = tk.Button(self.canvas, text="Demostración", font=("Arial", 16), width=15, command=lambda: self.ask_difficulty(mode="demo"))
        btn_exit = tk.Button(self.canvas, text="Salir", font=("Arial", 16), width=15, command=self.root.quit)

        btn_play.place(relx=0.5, rely=0.4, anchor="center")
        btn_demo.place(relx=0.5, rely=0.5, anchor="center")
        btn_exit.place(relx=0.5, rely=0.6, anchor="center")

    def ask_difficulty(self, mode="player"):
        self.canvas.delete("all")
        self.mode = mode

        tk.Label(self.canvas, text="Selecciona Dificultad", font=("Arial", 20)).place(relx=0.5, rely=0.3, anchor="center")

        btn_3 = tk.Button(self.canvas, text="3 discos (Fácil)", font=("Arial", 14), command=lambda: self.start_game(3))
        btn_6 = tk.Button(self.canvas, text="6 discos (Medio)", font=("Arial", 14), command=lambda: self.start_game(6))
        btn_8 = tk.Button(self.canvas, text="8 discos (Difícil)", font=("Arial", 14), command=lambda: self.start_game(8))

        btn_3.place(relx=0.5, rely=0.5, anchor="center")
        btn_6.place(relx=0.5, rely=0.6, anchor="center")
        btn_8.place(relx=0.5, rely=0.7, anchor="center")

    def start_game(self, num_discs):
        self.game = HanoiGame(num_discs)
        self.game.is_running = True
        self.game.start_time = time.time()
        self.selected_peg = None

        self.canvas.delete("all")
        self.canvas.bind("<Button-1>", self.on_click)
        if self.mode == "demo":
            self.root.bind("<Return>", self.ask_exit_demo)
            self.root.bind("<Escape>", self.ask_exit_demo)
            self.run_ai_demo(num_discs)
        else:
            self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")
        w, h = self.canvas.winfo_width(), self.canvas.winfo_height()
        peg_width = 10
        peg_height = h * 0.6
        base_y = h * 0.8
        disk_height = peg_height / (self.game.num_discs + 2)

        self.pegs_x = [w * 0.2, w * 0.5, w * 0.8]

        # Dibujar varillas
        for x in self.pegs_x:
            self.canvas.create_line(x, h * 0.3, x, base_y, width=peg_width, fill="gray")

        # Dibujar discos
        colors = ["#FF5733", "#33FF57", "#3357FF", "#F3FF33", "#FF33F3", "#33FFF3", "#C733FF", "#FFC733"]
        for i, peg in enumerate(self.game.pegs):
            for j, disk_size in enumerate(peg):
                width = disk_size * 20
                y = base_y - (j + 1) * disk_height
                self.canvas.create_rectangle(
                    self.pegs_x[i] - width, y,
                    self.pegs_x[i] + width, y + disk_height,
                    fill=colors[(disk_size - 1) % len(colors)], outline="black"
                )

        # Mostrar movimientos y tiempo
        self.canvas.create_text(10, 10, anchor="nw", text=f"Movimientos: {self.game.moves}", font=("Arial", 12), tag="moves")
        if self.game.is_running and self.game.start_time:
            elapsed = time.time() - self.game.start_time
            self.canvas.create_text(10, 30, anchor="nw", text=f"Tiempo: {format_time(elapsed)}", font=("Arial", 12), tag="time")

        self.root.after(100, self.update_timer)

    def update_timer(self):
        if self.game and self.game.is_running and self.mode == "player":
            elapsed = time.time() - self.game.start_time
            self.canvas.delete("time")
            self.canvas.create_text(10, 30, anchor="nw", text=f"Tiempo: {format_time(elapsed)}", font=("Arial", 12), tag="time")
            self.root.after(100, self.update_timer)

    def on_click(self, event):
        if not self.game or self.mode != "player":
            return

        w = self.canvas.winfo_width()
        peg_width = 60
        for i, x in enumerate(self.pegs_x):
            if x - peg_width < event.x < x + peg_width:
                if self.selected_peg is None:
                    if len(self.game.pegs[i]) > 0:
                        self.selected_peg = i
                        self.canvas.create_rectangle(x - 70, 10, x + 70, 40, outline="yellow", width=2)
                else:
                    if self.selected_peg != i:
                        if self.game.move(self.selected_peg, i):
                            self.draw_board()
                            if self.game.is_solved():
                                elapsed = time.time() - self.game.start_time
                                time_str = format_time(elapsed)
                                if show_results("Jugador", self.game.num_discs, self.game.moves, time_str):
                                    self.show_menu()
                                else:
                                    self.root.quit()
                    self.selected_peg = None
                    self.draw_board()
                break

    def run_ai_demo(self, num_discs):
        self.is_demo_running = True
        route, demo_num = self.solver.get_next_route(num_discs)
        self.game = HanoiGame(num_discs)
        self.game.is_running = True
        self.game.start_time = time.time()

        tk.Label(self.canvas, text=f"Demostración #{demo_num}", font=("Arial", 16), fg="blue").place(relx=0.5, rely=0.1, anchor="center")
        self.draw_board()

        self.execute_route_step(route, 0)

    def execute_route_step(self, route, index):
        if not self.is_demo_running or index >= len(route):
            elapsed = time.time() - self.game.start_time
            time_str = format_time(elapsed)
            if show_results("Demostración", self.game.num_discs, self.game.moves, time_str, demo_num=index):
                self.show_menu()
            else:
                self.root.quit()
            return

        from_peg, to_peg = route[index]
        self.game.move(from_peg, to_peg)
        self.draw_board()
        self.root.after(self.animation_speed, self.execute_route_step, route, index + 1)

    def ask_exit_demo(self, event=None):
        if self.is_demo_running:
            if show_confirmation("Salir del Demo", "¿Desea salir del demo?"):
                self.is_demo_running = False
                self.show_menu()