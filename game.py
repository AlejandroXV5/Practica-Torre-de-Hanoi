class HanoiGame:
    def __init__(self, num_discs):
        self.num_discs = num_discs
        self.pegs = [[i for i in range(num_discs, 0, -1)], [], []]
        self.moves = 0
        self.is_running = False
        self.start_time = None

    def move(self, from_peg, to_peg):
        """Mueve un disco de una torre a otra si es válido"""
        if not self.pegs[from_peg]:
            print("Error: intento de mover desde una torre vacía")
            return False
        if self.pegs[to_peg] and self.pegs[to_peg][-1] < self.pegs[from_peg][-1]:
            print("Error: movimiento inválido (disco más grande sobre uno más pequeño)")
            return False
        disk = self.pegs[from_peg].pop()
        self.pegs[to_peg].append(disk)
        self.moves += 1
        return True

    def is_solved(self):
        """Verifica si el juego está resuelto"""
        return len(self.pegs[0]) == 0 and len(self.pegs[1]) == 0