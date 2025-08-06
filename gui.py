# gui.py
import tkinter as tk
from tkinter import ttk, messagebox
from game import HanoiGame  # Asumimos que tienes una clase HanoiGame en game.py
import time

class HanoiGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Torre de Hanoi")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")

        # Inicializar el juego
        self.game = None
        self.selected_tower = None
        self.move_count = 0

        # Colores
        self.colors = [
            "#FF5733", "#33FF57", "#3357FF", "#F3FF33", "#FF33F3",
            "#33FFF3", "#FF8333", "#8333FF"
        ]

        self.setup_ui()

    def setup_ui(self):
        # Título
        title = tk.Label(self.root, text="Torre de Hanoi", font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#2c3e50")
        title.pack(pady=10)

        # Frame para controles
        control_frame = tk.Frame(self.root, bg="#f0f0f0")
        control_frame.pack(pady=10)

        tk.Label(control_frame, text="Discos:", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, padx=5)
        self.disk_var = tk.IntVar(value=3)
        disk_spinbox = ttk.Spinbox(control_frame, from_=1, to=8, width=5, textvariable=self.disk_var)
        disk_spinbox.grid(row=0, column=1, padx=5)

        self.start_btn = tk.Button(control_frame, text="Nuevo Juego", font=("Arial", 10), command=self.start_game, bg="#27ae60", fg="white", width=12)
        self.start_btn.grid(row=0, column=2, padx=10)

        self.solve_btn = tk.Button(control_frame, text="Resolver Automático", font=("Arial", 10), command=self.solve_auto, bg="#e67e22", fg="white", width=18)
        self.solve_btn.grid(row=0, column=3, padx=10)

        # Contador de movimientos
        self.move_label = tk.Label(self.root, text="Movimientos: 0", font=("Arial", 14), bg="#f0f0f0", fg="#2c3e50")
        self.move_label.pack(pady=5)

        # Canvas para dibujar las torres
        self.canvas = tk.Canvas(self.root, width=700, height=400, bg="#ecf0f1", highlightthickness=0)
        self.canvas.pack(pady=10)

        # Mensaje de estado
        self.status_label = tk.Label(self.root, text="Selecciona una torre para comenzar", font=("Arial", 12), bg="#f0f0f0", fg="#7f8c8d")
        self.status_label.pack(pady=5)

        # Inicializar juego
        self.start_game()

    def start_game(self):
        num_disks = self.disk_var.get()
        self.game = HanoiGame(num_disks)
        self.selected_tower = None
        self.move_count = 0
        self.move_label.config(text=f"Movimientos: {self.move_count}")
        self.status_label.config(text="Selecciona una torre para mover un disco")
        self.draw_towers()

    def draw_towers(self):
        self.canvas.delete("all")
        width = 700
        height = 400
        base_y = height - 50
        tower_width = 20
        tower_height = 200
        disk_height = 20
        gap = width // 4

        # Coordenadas de las torres (izquierda, centro, derecha)
        self.tower_x = [gap, 2 * gap, 3 * gap]

        # Dibujar base
        self.canvas.create_rectangle(50, base_y + 10, width - 50, base_y + 20, fill="#7f8c8d")

        for i, x in enumerate(self.tower_x):
            # Dibujar torre
            self.canvas.create_rectangle(x - tower_width // 2, base_y - tower_height, x + tower_width // 2, base_y, fill="#34495e")

            # Dibujar discos
            stack = self.game.towers[i]
            for j, disk_size in enumerate(reversed(stack)):
                disk_w = disk_size * 20  # ancho proporcional al tamaño
                y = base_y - (j + 1) * disk_height - 10
                color = self.colors[disk_size - 1] if disk_size <= len(self.colors) else "#95a5a6"
                self.canvas.create_rectangle(x - disk_w // 2, y, x + disk_w // 2, y + disk_height, fill=color, outline="black")

        # Resaltar torre seleccionada
        if self.selected_tower is not None:
            x = self.tower_x[self.selected_tower]
            self.canvas.create_oval(x - 30, base_y + 30, x + 30, base_y + 60, fill="yellow")
            self.canvas.create_text(x, base_y + 45, text="←", font=("Arial", 14))

    def on_tower_click(self, event):
        x = event.x
        y = event.y
        # Detectar qué torre fue clickeada
        for i, tx in enumerate(self.tower_x):
            if abs(x - tx) < 50 and y < 350:
                self.handle_tower_selection(i)
                return

    def handle_tower_selection(self, tower_index):
        if self.selected_tower is None:
            if len(self.game.towers[tower_index]) > 0:
                self.selected_tower = tower_index
                self.status_label.config(text=f"Seleccionada torre {tower_index + 1}. Elige destino.")
                self.draw_towers()
            else:
                self.status_label.config(text="Torre vacía. Elige otra.")
        else:
            from_tower = self.selected_tower
            to_tower = tower_index
            if from_tower == to_tower:
                self.status_label.config(text="Elige una torre diferente.")
            else:
                if self.game.move_disk(from_tower, to_tower):
                    self.move_count += 1
                    self.move_label.config(text=f"Movimientos: {self.move_count}")
                    self.selected_tower = None
                    self.draw_towers()
                    if self.game.is_solved():
                        self.status_label.config(text="¡Felicidades! Has resuelto el rompecabezas.")
                        messagebox.showinfo("¡Juego completado!", f"¡Lo lograste en {self.move_count} movimientos!")
                else:
                    self.status_label.config(text="Movimiento no válido. Usa un disco más pequeño sobre uno más grande.")
                    self.selected_tower = None
                    self.draw_towers()

    def solve_auto(self):
        from ai_solver import solve_hanoi  # Asumimos que tienes una función solve_hanoi(n, origen, destino, aux)
        self.status_label.config(text="Resolviendo automáticamente...")
        self.root.update()
        time.sleep(1)

        moves = []
        solve_hanoi(self.game.n, 0, 2, 1, moves)  # Origen: 0, Destino: 2, Aux: 1

        for from_tower, to_tower in moves:
            if not self.game.move_disk(from_tower, to_tower):
                break
            self.move_count += 1
            self.move_label.config(text=f"Movimientos: {self.move_count}")
            self.draw_towers()
            self.root.update()
            time.sleep(0.5)  # Pausa para ver el movimiento

        if self.game.is_solved():
            self.status_label.config(text="¡Resuelto automáticamente!")
            messagebox.showinfo("Resuelto", "La IA ha completado el juego.")

    def run(self):
        self.canvas.bind("<Button-1>", self.on_tower_click)
        self.root.mainloop()